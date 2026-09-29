---
name: writing-room
description: Orchestrate a multi-pass editorial pipeline for a novel or long-form fiction project. Takes a scene, chapter, or whole manuscript through the Writing Room skills in a fixed hand-off order (story-architect, fiction-writer, character-architect, technical-editor, realism-editor, continuity-editor, author-voice, ai-slop-killer, manuscript-reviewer), carries each pass's notes forward, and gates the result. Use when the ask is "run the pipeline," "run the writing room," "take this through the editors," "full editorial pass on chapter X," "revise and clean this scene," "all the editors," or any request to put prose through more than one editorial pass.
---

# Writing Room: Pipeline Orchestrator

One job: take a target (a scene, a chapter, a new draft, or the whole manuscript) through the editorial skills **in the right order**, carry each pass's notes to the next, and gate the result. This skill does not edit prose itself. It **calls the other Writing Room skills** and runs any mechanical checks the project defines.

## Step 0: load the project config

Look for `writing-room.config.md` at the project root (or the path the user names). It defines the book title, genre, POV rules, and the paths to the story spine, canon ledger, cast ledger, voice profile, idea backlog, banned words, and which optional passes run by default. Every Writing Room skill reads the same file.

- No config? Offer to create one from `reference/writing-room.config.example.md`, fill what the user tells you, and proceed with defaults for the rest. Don't block on it.
- If the config names an optional `memory_file`, read it before starting and append decisions to it afterward (template: `reference/memory.template.md`).

## The order (fixed; don't reorder on request)

`fiction-writer` drafts or revises first among the prose passes; `ai-slop-killer` is the **mandatory last pass on all prose**. A request that lists the skills in another order is reordered into:

```
[story-architect]  →  fiction-writer  →  [editorial-board]  →  character-architect  →
technical-editor   →  realism-editor  →  continuity-editor  →
[author-voice]     →  ai-slop-killer  →  [manuscript-reviewer]
```

Bracketed passes are optional (the config's `optional_passes` sets the defaults):

- `story-architect` first when the question is "what should this chapter DO."
- `editorial-board` right after `fiction-writer` for a heavier revise pass on dialogue, craft, and technical truth.
- `author-voice` between the content edits and `ai-slop-killer`.
- `manuscript-reviewer` after the gate, to score.

The **core six** are fiction-writer → character-architect → technical-editor → realism-editor → continuity-editor → ai-slop-killer. `technical-editor` can be skipped when the config sets `technical_domain: none`.

Mental model: **craft → cast → facts (domain) → facts (reader) → facts (canon) → clean.**

## How to run

1. **Confirm target and mode** in one question, then go:
   - **DRAFT**: generate a new scene. Start at `story-architect` if the beat isn't decided, else `fiction-writer`.
   - **REVISE**: improve existing prose. Start at `fiction-writer`.
   - **REVIEW**: assess only, no edits. Run every pass as a read, produce one consolidated findings list, end with `manuscript-reviewer`.
2. **Mechanical checks first** (fast, deterministic). If the config sets `checks_command`, run it. Otherwise run the built-in scan in `reference/pipeline.md` (banned words, retired names, house spelling rules). Triage: `FAIL` must be fixed; `REVIEW` flags become input for the relevant pass.
3. **Run the passes in order.** Invoke each skill on the target, hand its notes forward, keep a running diff. Let each pass speak before judging. A later pass may not silently undo an earlier one; if it reverses something, it says so.
4. **`ai-slop-killer` runs LAST, always.** It cleans the tells the content passes introduced.
5. **Gate** (full criteria in `reference/pipeline.md`): 0 FAILs; every REVIEW flag resolved or consciously kept; ledgers updated for any new or changed fact or cast change; `ai-slop-killer` ran last. Then optionally score with `manuscript-reviewer`.

## Whole-chapter and whole-book runs

Fan the reading out to subagents per batch of chapters, run each pass's lens per batch, then consolidate into one report and one set of edits. Don't try to hold a full manuscript in a single pass.

## Output

- If the project is under version control, edits land on a **branch** and are proposed for merge; never commit straight to the main line unless the config's `git_workflow` says otherwise.
- A REVIEW run produces a findings document, no edits.
- After any change, **update the ledgers**: the canon ledger (via `continuity-editor`) for facts, the cast ledger (via `character-architect`) for people. If a name was renamed, merged, or cut, add the old name to the config's `retired_names` so the regression check keeps catching it.
- Respect `approval_required` in the config: changes of the listed kinds (plot, chapter order, POV, ending) are proposed, not applied.

## What this skill is not

- Not a replacement for the individual skills; it sequences them.
- Not a scorer; that's `manuscript-reviewer`, run after the gate.
- Not a drafting tool; that's `fiction-writer`.

## Reference

- `reference/writing-room.config.example.md`: annotated config template.
- `reference/pipeline.md`: pass-by-pass hand-off notes, the built-in mechanical scan, and gate criteria.
- `reference/memory.template.md`: optional running memory file for the project.
