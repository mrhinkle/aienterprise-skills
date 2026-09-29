---
name: character-architect
description: Develop, cast, and audit a novel's characters so the ensemble stays tight and every named character earns their place. Applies four gates (function, want and need, tag, choice under pressure), round-vs-flat discipline, and naming rules against confusable names, and keeps a cast ledger. Use when adding a character, deciding whether someone should be a name or a role, naming anyone, checking a character's function and arc, or auditing the cast for blur. Trigger on "add a character," "is this character earning their place," "name this person," "too many characters," "cast audit," "name audit," "should this be a role instead of a name," or when a character's throughline feels lost.
---

# Character Architect

One job: keep the cast tight and legible. Every named character serves a distinct function, carries a recognizable tag, and has a name a reader can't confuse with anyone else's. The common failure in ensemble novels is *too many similar people*: same function, same-sounding names, same shape. This skill stops that before it reaches the page.

## Inputs

- `writing-room.config.md` at the project root: `cast_ledger`, `max_round_characters` (default 7), `max_new_named_per_scene` (default 3), `retired_names`, `sanctioned_name_reuse`, `pov.characters`.
- The **cast ledger** at `cast_ledger`: who exists, role, tag, want and need, arc, naming notes. Read it before adding or renaming anyone; update it whenever the cast changes. No ledger yet? Build one from `reference/cast-ledger.template.md`.
- Optional: a project `memory.md` (config `memory_file`, or `reference/memory.template.md`).

## The four gates (a character earns a name only by clearing all four)

1. **Function.** What distinct dramatic or thematic job does this person do that no one else does? If their purpose folds into someone already on the page without breaking a scene, **merge or cut** (the merge test). Define them by opposition to the others: weakness, want, value, stance on the book's argument (Truby's character web).
2. **Want and need.** Every character wants something, "even if it is only a glass of water" (Vonnegut). Majors also have a **need**, an internal flaw or misbelief the story forces them to face, kept distinct from the external want (Truby; Cron). Example: *wants* to save the family business; *needs* to stop treating people as line items.
3. **Tag.** One recognizable trait, object, speech rhythm, or vulnerability that identifies them without the name (a pencil always behind one ear; a habit of answering questions with questions; a counter they keep in their head). No tag, not built yet.
4. **Revealed by choice under pressure.** Don't describe character; force a decision with stakes and let the choice show it (McKee).

## Cast discipline

- **Round vs. flat.** Roundness, the capacity to surprise convincingly and change, is reserved for the few who carry arcs (at most `max_round_characters`). Everyone else is deliberately, vividly **flat**: one sharp quality, no arc (Forster). Flat is how a complex novel stays readable.
- **Name only what matters.** A name signals importance. Functionaries who move one scene get a **role-label**: "the night nurse," "the procurement officer," "the dispatcher."
- **Composite the crowd.** Show a populated room with two or three named types (the skeptic, the true believer, the careerist), not a roster.
- **Space the entrances.** No more than `max_new_named_per_scene` new names per scene, each given room to land a tag.
- **One handle per person** throughout, unless a POV reason is deliberate.
- **POV discipline.** Only characters in `pov.characters` get interiority.

## Naming

Full rules and the audit procedure are in `reference/naming-and-audit.md`. The short version:

- No two prominent characters share a first initial where avoidable.
- If a letter must repeat, vary syllable count, length, stress, and end-sound.
- No clusters of same-rhythm, same-ending surnames or first names.
- No rhymes, no near-identical names, no name-vs-place near misses.
- Reuse a name only on purpose, and record it in `sanctioned_name_reuse`.

## Hand-off and updates

- Recommend; execute renames, merges, or cuts only with the author's sign-off.
- After any change: update the cast ledger, tell `continuity-editor` so the canon ledger follows, and add old names to the config's `retired_names`.
- Inside the Writing Room, the next pass is `technical-editor`. Any prose you touch still ends with `ai-slop-killer`.

## Sources

Forster, *Aspects of the Novel*; Egri, *The Art of Dramatic Writing*; McKee, *Story*; Truby, *The Anatomy of Story*; Cron, *Story Genius*; Maass, *Writing the Breakout Novel*; Propp, *Morphology of the Folktale*. Practitioner heuristics on large casts and confusable names from K.M. Weiland, Janice Hardy, Anne R. Allen, and Writer's Digest.
