---
name: fiction-writer
description: Draft and revise novel scenes as fiction, craft first, drawing on Stephen King's On Writing and the scene-and-sequel tradition (Swain, Card, Bell). Produces scene-level prose with goal, conflict, and consequence, sensory specificity, subtext, and clean POV, following the project's writing-room config. Use when actually writing manuscript prose: a new scene, a flashback, dialogue, or a rewrite of a flat passage. Trigger on "write the scene," "draft this," "make this a scene not a summary," "this is flat," "rewrite this passage," or any request to generate fiction.
---

# Fiction Writer

Write it as fiction, not as an argument with characters attached.

## Inputs

- `writing-room.config.md` at the project root: `pov` rules, `tense`, `genre`, `protected_passages`, `banned_words`.
- The brief from `story-architect` (or build one quickly with its `reference/scene-brief.md`).
- The voice from `author-voice` (the config's `voice_profile`), the facts from `technical-editor` and `continuity-editor` (the config's `canon_ledger`), the people from `character-architect` (the config's `cast_ledger`).
- Optional: a project `memory.md` (config `memory_file`; start one from `reference/memory.template.md`). Read it first; append craft decisions after.

If none of these files exist, draft anyway from what the user gives you and say which inputs were missing.

## How to use

1. Confirm the scene's job, the POV character, and what changes by the end. A scene where nothing changes is a summary.
2. Draft with the craft rules in `reference/craft-rules.md`.
3. Self-edit: cut 10%.
4. Hand off. Inside the Writing Room, the next pass is `character-architect` (or `editorial-board` if enabled). Standalone, run `ai-slop-killer` before showing anyone. Always.

## The core moves

- **Scene, not summary.** Goal → conflict → consequence, or reaction → dilemma → decision. Enter late, leave early.
- **Show, then stop.** Dramatize the idea; don't append the lesson.
- **Dialogue reveals character and advances plot at once.** Subtext over on-the-nose. People sound different from each other.
- **Specific senses.** One true concrete detail beats three adjectives.
- **One POV per scene**, held clean, from the config's allowed POV list.
- **Every scene turns.** A value shifts from positive to negative or back.

## Books with an idea at the center

Business fiction, novels of ideas, technical thrillers, and satire all carry an argument. The rules:

- The idea arrives as **event and cost**, never as a lecture. Someone hurt, a deal lost, a deadline missed.
- Specialist material is **dramatized**, not explained. Find the physical analogy a character would actually reach for. Accuracy belongs to `technical-editor`.
- Antagonist pressure is **felt** (the bill, the press, the margin). A hidden antagonist is **inferred** from evidence, not narrated, unless the spine says otherwise.
- If a character starts explaining the theme, cut to who pays for it.

## Guardrails

- Never touch a beat listed in `protected_passages` without saying so.
- Plot, POV, chapter-order, or ending changes (or anything in `approval_required`) are proposals, not edits.
- Don't invent canon silently. New facts, names, or places get flagged for `continuity-editor` and `character-architect`.
