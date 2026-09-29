---
name: realism-editor
description: Pressure-test whether a novel or long-form narrative lands with its intended reader, meaning the dilemmas are ones that reader would recognize, the institutional and everyday mechanics ring true (money, contracts, bosses, bureaucracy, family, workplace), and nobody is a strawman. Reads the book's reader profile from the project config and checks each scene against it. Use for "does this land," "would a real [exec / nurse / cop / teacher / reader of this genre] buy this," "is this realistic," "check the business reality," "is this too clean," or "who is this for."
---

# Realism Editor

The test isn't "is it exciting." It's whether the intended reader reads the scene and thinks, *that's my Tuesday.* This skill checks lived reality: institutions, incentives, costs, and the people inside them. Hard technical accuracy belongs to `technical-editor`; the book's own established facts belong to `continuity-editor`.

## Step 0: load settings

Read `writing-room.config.md`. Use:

- `reader_profile` — path to a file describing who the book is for, the real dilemmas they live, and what lands or doesn't. If missing, offer to draft one from `reference/reader-profile.template.md` (ask two questions: who is the reader, and what do they deal with every week?).
- `genre` — sets the realism bar. A thriller can compress time; a workplace novel can't fake a payroll run.
- `memory_file` or a project `memory.md`, if present: read prior rulings, append new ones (template: `reference/memory.template.md`).

For business or workplace fiction, `reference/worked-example-business-reader.md` is a filled-in profile you can adapt.

## How to run

1. **Name the decision or tension** in the passage in one line: who has to choose what, and what it costs.
2. **Check it against the reader profile:**
   - Is this a dilemma the intended reader actually faces, or one a writer imagined they face?
   - Are the mechanics credible: money, contracts, approvals, schedules, staffing, law, family logistics, whatever this world runs on?
   - Does anyone get a win for free?
   - Is anyone a strawman? A skeptic who is half right is worth more than a villain who is all wrong.
3. **Flag** the usual failures (full list in `reference/realism-checks.md`): utopian or doomer framing, jargon without stakes, flawless demos, cartoon institutions, a too-clean villain or victory, sentimental or contemptuous portrayal of working people, and costs that vanish between chapters.
4. **Propose the grounding fix.** Usually one of: a real trade-off, a real price, a real constraint, a real procedure, or a line of dialogue that sounds like someone who does the job. Keep it small and in the book's register.
5. **Hand off** to `author-voice` (if used), then `ai-slop-killer` as the mandatory final pass. If the fix changes a story fact, route through `continuity-editor`.

## The single question

Would a real person in the reader's position recognize this choice, and feel the cost of getting it wrong?

## Output

```
REALISM EDIT — [target] · reader: [one-line reader profile]

The decision on the page: [one line]
Verdict: LANDS / MOSTLY / DOESN'T LAND

| # | Location (short quote) | Problem | Why the reader won't buy it | Grounding fix |
|---|------------------------|---------|------------------------------|---------------|

Strawman watch: [characters or institutions that are too easy]
Free wins: [anything that should have cost more]
Reader-profile updates proposed: [new dilemmas or "what lands" notes]
```

Keep quotes from the manuscript short. Be blunt; the author wants pushback, not reassurance.

## When not to use

- Is the science, code, medicine, or law correct? → `technical-editor`
- Does it contradict earlier chapters? → `continuity-editor`
- Is the scene alive as fiction (goal, conflict, subtext)? → `fiction-writer` or `editorial-board`
- Scoring the chapter → `manuscript-reviewer`
