# Canon Ledger — [Book Title]

The single source of truth for what is true in this book **right now**. Copy into your project and set `canon_ledger` in `writing-room.config.md` to its path. The continuity editor reads it before every check and updates it with every change that establishes or alters a fact.

People's names, roles, and arcs live in the cast ledger (`cast_ledger`). This file records the facts about them that other chapters depend on, and everything else.

**Conventions**
- One fact per row. Cite the chapter that establishes it (`ch03`), and the chapters that rely on it if the fact is load-bearing.
- Status: `CANON` (in the manuscript), `PLANNED` (approved, not yet written), `OPEN` (undecided; don't write it into prose yet).
- When a fact changes, edit the row in place and log the change at the bottom. Don't leave the old value in the table.
- Example rows below are invented placeholders. Delete them.

---

## 1. Structure

| Item | Value | Status | Source |
|------|-------|--------|--------|
| Chapter count | 24 numbered chapters + unnumbered epilogue | CANON | outline |
| Archived chapters | old ch19 "The Ferry" (cut; do not reference) | CANON | — |
| POV rule | close third, one POV per chapter | CANON | config |

## 2. Timeline

Order matters more than dates. Record anchor events, then relative gaps.

| # | Event | When (absolute or relative) | Status | Source | Depends on it |
|---|-------|-----------------------------|--------|--------|---------------|
| T1 | The quarry closes | autumn, 12 years before ch01 | CANON | ch02 | ch09, ch15 |
| T2 | Opening scene | a Thursday in late March | CANON | ch01 | — |
| T3 | The flood | 3 weeks after T2 | CANON | ch06 | ch07–ch10 |

**Day-of-week and travel-time notes:** [e.g. the drive from the farm to the county seat is 40 minutes]

## 3. People facts that other chapters depend on

(Names, roles, and arcs: see the cast ledger.)

| Person | Fact | Value | Status | Source |
|--------|------|-------|--------|--------|
| [Protagonist] | age at opening | 38 | CANON | ch01 |
| [Protagonist] | who owns the bakery | her aunt, not her mother | CANON | ch03 |
| [Mentor] | when he learns the secret | end of ch14, not before | CANON | ch14 |

## 4. Places

Keep similar places distinct.

| Place | Key facts | Easily confused with | Source |
|-------|-----------|----------------------|--------|
| East ferry landing | one ramp; closes at 9 p.m. | West landing (two ramps, runs all night) | ch02 |

## 5. Objects

| Object | Origin | Description | Current holder / location | Source |
|--------|--------|-------------|----------------------------|--------|
| The brass compass | inherited from her grandmother (not bought) | lid dented, needle sticks | in her coat pocket from ch05 | ch01, ch05 |

## 6. Numbers

| Quantity | Value | Status | Source | Notes |
|----------|-------|--------|--------|-------|
| Quarry workers laid off | 112 | CANON | ch04 | two years before the flood |
| Council vote | 7–2 | CANON | ch13 | |

## 7. World rules and inventions

Anything invented: technologies, laws, institutions, organizations, magic, protocols. Record the rule and its limits. Real-world plausibility lives in the technical editor's reference; this is the book's own version.

| Invention | Rule | Limit (what it can't do) | Status | Source |
|-----------|------|--------------------------|--------|--------|
| The tide-warning network | predicts surges from buoy data | blind when a buoy goes offline | CANON | ch03 |

## 8. Knowledge state

Who knows what, from when. Prevents characters acting on information too early.

| Secret / revelation | Who knows | From | Source |
|---------------------|-----------|------|--------|

## 9. Terminology and spelling

House spellings and names of things, so they don't drift.

| Term | Use | Don't use | Source |
|------|-----|-----------|--------|
| the Landing | capitalized as a place name | "the landing" (lowercase) after ch02 | ch02 |

## 10. Open questions

Undecided facts. Don't write these into prose until resolved.

- [OPEN] [question] · raised [date] · blocks [chapter]

---

## Change log

Newest first. One line per change: date · fact · old → new · why · chapters touched. Keep this short; move anything older than the current draft to an archive file if it grows.

- [YYYY-MM-DD] · [fact] · [old] → [new] · [reason] · [chapters]
