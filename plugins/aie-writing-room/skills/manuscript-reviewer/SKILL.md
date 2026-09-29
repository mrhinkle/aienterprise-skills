---
name: manuscript-reviewer
description: Score a novel chapter or full manuscript against a configurable weighted rubric (eight default dimensions, reweightable or replaceable per book), then run simulated review debates with a writer panel (personas in the tradition of well-known authors' published craft advice) and a reader panel (the book's target-reader archetypes). Also runs auto-flag scans, one-on-one critiques, and turns a review into a ranked revision list. Produces feedback, not edits. Trigger on "review the book," "review chapter X," "score the manuscript," "run the panel," "what would [reviewer] say," "reviewers debate," "reader panel," "auto-flag scan," or "build a revision priority list."
---

# Manuscript Reviewer

A menu-driven evaluator for a novel (or long-form narrative nonfiction). Scores against the rubric in `reference/rubric.md`, then runs panel debates between writer personas and target readers. This skill diagnoses; `editorial-board` revises.

## Step 0: load settings

Read `writing-room.config.md`. Use:

- `title`, `genre` — for report headers and to pick sensible panel defaults.
- `manuscript_glob` — where chapters live (folder or glob). If a chapter isn't where expected, ask for the path rather than guessing.
- `rubric` — optional path to a rubric JSON (dimensions and weights). Default: the eight dimensions in `reference/rubric.md`. Example: `reference/rubric.example.json`.
- `reader_profile` — used to build the reader panel. Without it, use the generic archetypes in `reference/reader-panel.md`.
- `reviewer_panel` — optional: which writers sit on the standing panel and bench, and any custom reviewers.
- `memory_file` or a project `memory.md`, if present: read the score history, append new scores (template: `reference/memory.template.md`).

## Always start with the menu

Present this and wait for a choice. Don't assume.

```
[BOOK TITLE] — REVIEWER

  1. Review the whole book            (rubric scores + manuscript-level report)
  2. Review a single chapter          (rubric scores + per-dimension notes)
  3. Reviewers Debate — Writer Panel
  4. Reviewers Debate — Reader Panel
  5. Run BOTH panels + synthesis
  6. One-on-one critique              (any writer or reader persona)
  7. Auto-flag scan only
  8. Revision priority list           (turn a prior review into a fix queue)
  9. Substituted debate               (option 3 with one standing panelist swapped for a bench reviewer)
  0. Quit
```

If the option needs a target (a chapter, a reviewer), ask for it in one short question, then run.

## Source material

- `reference/rubric.md` — default dimensions, bands, decision thresholds, auto-flags, and how to customize per book
- `reference/writer-panel.md` — standing writer panel (five personas)
- `reference/writer-panel-bench.md` — bench of five more, for specific lenses or substitution
- `reference/reader-panel.md` — how to build reader archetypes, with generic defaults and a worked example
- `reference/debate-format.md` — how to run the rounds
- `reference/output-templates.md` — exact shape of each deliverable

## How each option works

**1. Whole book.** Read every chapter in order. Score each quickly (one score per dimension, terse rationale). Book-level scores = per-chapter scores averaged, **weighted by word count**. Run all auto-flags at manuscript level. Output the manuscript report plus top-5 / bottom-5 tables, not one report per chapter. Track progress per chapter; fan batches out to subagents if available.

**2. Single chapter.** Score every dimension; write the per-chapter report. Quote a short line when calling out a problem. End with a 3–5 item fix queue ordered by impact.

**3. Writer panel.** Debate format with the standing writer panel. Three rounds: opening verdict → cross-examination → one concrete revision each.

**4. Reader panel.** Same format with the reader archetypes. Rounds: Did you finish it? → What stuck? → Would you recommend it?

**5. Both + synthesis.** Writers first, then readers. Synthesis: where they agree (real problems), where they disagree (taste calls for the author), the single highest-leverage revision, and the writer-reader gap.

**6. One-on-one.** Any writer (standing or bench) or reader persona. Three paragraphs in their voice, then what they'd cut and keep. If the user hasn't picked, suggest one that fits the chapter's center of gravity (see the bench's "when to call" table).

**7. Auto-flag scan.** Run only the auto-flags from the rubric. Report the ones that fire; if none, say so in one line.

**8. Revision priority list.** From a prior review, pull every fix item. Sort by auto-flag severity, then dimension weight, then effort-to-impact. Numbered list with S/M/L effort and chapters affected.

**9. Substituted debate.** The user picks one standing panelist to bench and one bench reviewer to bring in. Note the swap in the report header.

## Scoring helper

```
python3 scripts/score.py <score per dimension, in rubric order>
python3 scripts/score.py theme=80 story=72 ...            # key=score, any order
python3 scripts/score.py --rubric path/to/rubric.json ...  # custom rubric
python3 scripts/score.py --show [--rubric ...]             # list dimensions and weights
```

Returns the weighted total, a per-dimension table with bands, and chapter- and manuscript-level decisions.

## Voice rules (all output)

- Honor the project's `banned_words` and house style from the config.
- When channeling a reviewer, sound like that persona, not generic feedback. The King persona swears sometimes; the Goldratt persona asks questions; the Doctorow persona names power. Personas are lenses in the tradition of each author's published work, not the real people.
- No fawning, no preamble. If a chapter is weak, say so.
- Quotes from the manuscript stay short (a line, not a paragraph).
- Cite sources for factual claims (comparable titles, market claims).

## When not to use

- Revising prose → `editorial-board`, or `fiction-writer` for new drafting
- Continuity-only checks → `continuity-editor`
- Running the full pipeline → `writing-room`, which can end with this skill as its scoring stage
