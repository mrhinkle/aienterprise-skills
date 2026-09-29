# Ledger Rules — keeping the canon ledger usable

A canon ledger is only useful if it can be read in one sitting. Ledgers fail by turning into a diary of every revision pass until nobody can find the current value of anything. These rules prevent that.

## Current state, not history

- The tables hold what is true **now**. When a fact changes, overwrite the row.
- History goes in the change log at the bottom, one line per change.
- When the change log gets long (more than a screen or two), move older entries to an archive file next to the ledger. The continuity editor reads the tables, not the archive, unless investigating an old decision.

## One fact, one home

- People's names, roles, and arcs belong to the cast ledger. The canon ledger records only facts about them that other chapters depend on (ages, dates, who knows what).
- Real-world technical facts belong to the technical reference. The canon ledger records the book's inventions and their rules.
- If a fact appears in two places, pick one and link to it from the other.

## Status discipline

- `CANON` — it's in the manuscript. Cite the chapter.
- `PLANNED` — approved for a future draft. Don't flag its absence as a contradiction.
- `OPEN` — undecided. Don't let new prose settle it silently; raise it with the author.

## What earns a row

Log a fact when any of these is true:
- Another chapter depends on it.
- It's a number, a date, a name, an origin, or a rule.
- It was argued about once. If it was argued about, it will drift.

Don't log: descriptive color no one will reference again, or decisions about style.

## When the manuscript and ledger disagree

1. Check the change log: maybe the ledger is stale.
2. If the ledger is right, the manuscript has a contradiction: report it.
3. If the manuscript is right (a deliberate later change the ledger missed), update the ledger and log the change.
4. If you can't tell, mark `UNSURE` and ask. Never guess which one the author meant.

## Retired names and superseded facts

- When a character or place is renamed, cut, or merged, add the old name to `retired_names` in the config so searches keep catching it.
- When a fact is superseded, keep only the new value in the table; the old one lives in the change log.

## Same change, same commit

The edit that establishes or changes a fact and the ledger update that records it should land together. A ledger updated "later" is a ledger that's already wrong.
