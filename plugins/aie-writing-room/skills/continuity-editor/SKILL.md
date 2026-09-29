---
name: continuity-editor
description: Check a novel or long-form narrative for continuity only, meaning names, facts, timeline, places, relationships, objects, rules of the world, and chapter numbering, against the project's canon ledger and the manuscript itself. Does not touch style, story, or voice. Reports contradictions with chapter references and the canonical value, and keeps the ledger current when a fact is established or changed. Use after any edit, before any merge, or to audit a chapter or the whole book. Trigger on "check continuity," "is this consistent," "does this contradict," "canon check," "audit the facts," "update the ledger," or "what did we establish about X."
---

# Continuity Editor

One job: does this contradict anything already true in the book? Style, story, and voice are out of scope. Only canon. Real-world accuracy is `technical-editor`'s job; this skill guards the book's own facts, including invented ones.

## Step 0: load settings

Read `writing-room.config.md`. Use:

- `canon_ledger` — path to the canon ledger. If it doesn't exist, offer to create one from `reference/canon-ledger.template.md` and seed it from the chapters you're about to check.
- `cast_ledger` — the character list (owned by `character-architect`); use it for names, roles, and relationships. Don't duplicate it in the canon ledger.
- `manuscript_glob` — where the chapters live (a folder or glob), so you can search them.
- `retired_names` — names that were cut or renamed and must not reappear.
- `memory_file` or a project `memory.md`, if present: read open questions, append a pass line (template: `reference/memory.template.md`).

## How to run

1. **Inventory the passage.** List every name, role, date, day, time gap, age, place, distance, object, number, relationship, and world rule it asserts or implies. Implied counts: "two winters after the fire" asserts an order of events.
2. **Check each item** against the canon ledger, then search the manuscript for the same name or term to catch facts the ledger missed. Check the cast ledger for people and `retired_names` for anything that should be gone.
3. **Classify each hit:**
   - `CONTRADICTION` — conflicts with canon. Give both chapter references and the canonical value.
   - `DRIFT` — not a hard conflict, but wording that will read as a change (a ring "inherited" in one chapter, "bought" in another).
   - `NEW` — establishes something not yet in the ledger.
   - `RETIRED` — uses a retired name or superseded fact.
   - `UNSURE` — the ledger is silent or ambiguous; ask the author.
4. **Report**, don't rewrite. Propose the minimal fix (usually a word or a number), and fix only with the author's sign-off. Never "improve" prose here.
5. **Update the ledger** in the same change as the edit that caused it: add `NEW` facts, and when a fact changes, edit the canonical row and add a line to the ledger's change log. The ledger stays a record of what is true now, not a diary (see `reference/ledger-rules.md`).

## What to watch hardest

- **People:** names and spellings, jobs and titles, who founded or owns what, ages, family ties, who knows what by which chapter.
- **Timeline:** order of events, gaps between them, days of the week, seasons, how long travel takes.
- **Objects and places:** where a thing came from, what it looks like, who has it now; which place is which when several are similar.
- **Numbers:** counts, money, votes, casualties, distances. Numbers drift fastest.
- **World rules:** anything invented (a technology, law, magic system, institution) and its limits.
- **Structure:** chapter numbering, part titles, and any unnumbered or archived chapters.
- **Knowledge state:** a character acting on information they haven't learned yet.

## Output

```
CONTINUITY CHECK — [target] · ledger: [canon_ledger] · [date]

| # | Location | Asserts | Canon says (source) | Class | Proposed fix |
|---|----------|---------|---------------------|-------|--------------|

Ledger updates: [rows to add or change, with the chapter that establishes them]
Questions for the author: [UNSURE items]
```

If nothing conflicts, say so in one line and list any `NEW` facts to log.

## Whole-book audits

Work chapter by chapter in order, building a scratch timeline as you go. Fan batches of chapters out to subagents if available, then reconcile their findings against one ledger. Report the timeline alongside the contradictions.

## When not to use

- Is the domain content accurate in the real world? → `technical-editor`
- Would the intended reader believe it? → `realism-editor`
- Should this character exist, or be renamed? → `character-architect`
- Style, voice, or AI tells → `author-voice`, then `ai-slop-killer`
