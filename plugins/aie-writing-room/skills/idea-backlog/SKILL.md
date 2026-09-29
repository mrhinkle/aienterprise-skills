---
name: idea-backlog
description: Capture and evaluate candidate ideas and revisions for a novel or long-form project in a running backlog file (IDEAS.md by default) without acting on them. Assigns IDs, records source, type, and effort, and weighs each idea against the story spine, scene-over-lecture, cost vs. payoff, and continuity before giving a verdict. Use when the author says "add an idea," "log this for later," "park this," "what's on the idea list," "groom the backlog," "evaluate the backlog," or when a review or audit surfaces a change worth remembering but not doing now. Trigger on "idea," "backlog," "park this," "for later," "what should we still do."
---

# Idea Backlog: capture and evaluate

One job: make sure no good idea for the book is lost, and that none reaches the manuscript without being weighed first. **Capturing an idea is not committing to it.** This skill grooms the list; it never edits a chapter.

## Inputs

- `writing-room.config.md` at the project root: `ideas_backlog` (default `IDEAS.md` at the project root), `spine_doc`, `canon_ledger`, `approval_required`.
- If the backlog file doesn't exist, create it from `reference/IDEAS.template.md`.

## Capture (an idea just appeared)

1. Open the backlog; assign the next integer ID.
2. Add one row: **Idea** (one line) · **Source** (who or what raised it, plus date) · **Type** (`S` structural / `L` line or voice / `C` continuity) · **Effort** (`S` / `M` / `L`) · **Status** = `captured` · **Verdict/notes** (blank, or a one-line hook).
3. Cite the source. Touch no chapter. Stop.

## Evaluate (weigh ideas for inclusion)

Run each candidate through this gate, then set Status and Verdict:

- **Spine.** Does it serve the spine doc (the central question, the causal chain, the themes)? If it fights the spine, reject.
- **Scene, not lecture.** Does it argue through scene and consequence? Ideas that add explanation lose.
- **Cost vs. payoff.** Weigh Effort against the dimension it lifts (Theme, Story, Character, World, Voice, Dialogue, Pacing, Hook; or the rubric `manuscript-reviewer` uses for this project). Do high-payoff, low-effort first.
- **Continuity.** Check the canon ledger. If the idea changes canon, note the ledger update it would force.
- **Approval.** If it is a change of a kind listed in `approval_required` (plot, POV, chapter order, ending), the verdict can be no stronger than `needs-decision` until the author signs off.
- **Verdict.** `accepted` (ready to queue), `deferred` (good, not now; say why), `rejected` (say why), or `needs-decision` (waiting on the author). Update the row.

## Status lifecycle

`captured` → `evaluating` → `accepted` → `done` (shipped), or `deferred` / `rejected` / `needs-decision`.

## Rules

- Never apply a manuscript change from this skill. Planning is `story-architect`'s job, drafting is `fiction-writer`'s, editing belongs to the editors, and the `writing-room` skill runs accepted ideas through the pipeline.
- One running file. Do not fork it.
- Keep entries terse; the detail lives in the source review or audit, referenced by date.
- An idea is `done` only once the change is actually in the manuscript.
