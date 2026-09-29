# Naming rules and the cast audit

## Naming rules

- **Alphabet rule.** No two prominent characters share a first initial where avoidable. Check the initial *before* committing a name.
- **Distinct shape over the letter.** If a letter must repeat, vary syllable count, length, stress, and end-sound. "Jo" and "Jonathan" can coexist; "Marta, Marcus, Margo, Marisa" cannot.
- **No same-origin, same-rhythm clusters.** A run of surnames with the same ending or cadence (for example Carlson, Nelson, Hanson, Olson) blurs in the reader's head even when it is realistic for the setting. Diversify the surname palette and vary first initials. Distinctiveness beats realism.
- **No rhymes or shared endings** in names that appear together (Kaylee and Bailey; Dorian and Florian).
- **No near-identical names, ever.** One-letter or one-syllable differences (Anya and Ania) will be misread.
- **Watch name-vs-place collisions.** A daughter named Florence in a book that visits Florence needs a reason.
- **Reuse a name only on purpose.** A deliberate collision (an impostor using a real person's name, a child named after a dead parent) is a plot point. Record it in the config's `sanctioned_name_reuse` with the reason. Every other duplicate is a bug.
- **Retired names stay retired.** Anything renamed or cut goes into `retired_names` so the mechanical scan fails on it.

## Cast audit procedure

1. **Scan** the manuscript (`manuscript_glob`) for named characters, frequency, and chapter spread. A quick start: grep for capitalized two-word sequences and dialogue attributions, then dedupe against the cast ledger.
2. **Cluster** by first initial, by surname ending or culture of origin, and by shape (syllables, length). Flag any cluster of three or more.
3. **Classify** each flagged name from the ledger: major (keep), recurring supporting (consider a rename to break the cluster), or walk-on (convert to a role-label).
4. **Merge test** every pair that shares a function.
5. **Check the round count** against `max_round_characters`. Anyone round who shouldn't be gets flattened in the ledger.
6. **Recommend**, with a table:

```
| Name | Class | Problem | Recommendation | Chapters touched |
```

7. **Execute only with sign-off.** Then update the cast ledger, notify `continuity-editor`, and append old names to `retired_names`.
