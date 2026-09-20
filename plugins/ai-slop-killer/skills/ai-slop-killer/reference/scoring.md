# Slop Score — how to grade a passage

A 0–100 score where **lower is cleaner**. Report it before and after the edit so the improvement is visible. A heuristic to force attention, not a precise metric — clustering matters more than any single hit.

## Count the hits

Scan the passage and tally by weight:

**Severe (5 pts each)**
- Negative parallelism ("not X, it's Y") / triple-negation reveal
- Wind-up intro or signposted conclusion
- Unsourced confident factual claim (per config `citations`)
- Any hard-default banlist word (delve, tapestry, leverage, robust, seamless, etc.)
- Grandiose stakes inflation / invented concept label used as established term

**Moderate (2 pts each)**
- Rule-of-three or anaphora pile-up (each extra past the first in a section)
- Rhetorical Q&A / false-suspense transition ("Here's the kicker")
- Pedagogical framing ("Let's break this down," "Think of it as")
- Telling-after-showing / trailing "-ing" superficial analysis
- Vague attribution ("experts say") with no name
- Corporate-AI vocabulary word (elevate, foster, streamline, myriad, pivotal…)
- Header inflation / bold-first-bullet listicle / enumerated prose
- Em-dash overdose (per offending paragraph)
- Low burstiness: a run of 3+ uniform "rectangle" paragraphs (or fragment-spam) — 2 pts per run

**Minor (1 pt each)**
- Hedge/softener, filler connector (moreover, notably, that said…)
- "Designed to / aims to" scaffolding
- Magic adverb (quietly, deeply, fundamentally…)
- Bold-word confetti / stray unicode / quote drift (per offending paragraph)
- Vague quantifier where a number belongs
- False range ("from X to Y")

## Normalize

`score = round( total_points / word_count * 500 )`, capped at 100. This normalizes to points **per 500 words**, matching the bands below and the "clean ≤5 per 500 words" threshold in SKILL.md.

Rough bands (per ~500 words):
- **0–5:** clean. Reads human. Ship it.
- **6–15:** light slop. A few targeted cuts.
- **16–30:** moderate. Noticeable machine cadence; needs a real pass.
- **31+:** heavy. Rework, don't just trim.

## Report format

```
Slop score: 34 → 6  (per 500 words)

Cut / fixed:
- Negative parallelism x3   — rewrote as plain statements
- "leverage" x4             — → "use"
- Wind-up intro             — deleted, opened on the real first line
- Rectangle paragraphs x1   — varied sentence length (high-low)
- Em-dash overdose          — 2 paragraphs re-punctuated
- Unsourced claim           — flagged: "40% of firms…" needs a source

Left on purpose:
- 1 rhetorical question (earns it)
```

If the passage scores ≤5 on the first read, say so in one line and stop — don't manufacture edits.
