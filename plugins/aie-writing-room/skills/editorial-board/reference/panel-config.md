# Configuring the Panel

The default board suits most novels with dialogue, and adds teaching and domain seats when the book needs them. Change it in `writing-room.config.md` under `editorial_panel`. The board reads that block at the start of every pass.

## Config shape

```markdown
## editorial_panel
- seats: king, higgins, price, kim, goldratt, domain-mechanism, domain-capability
- teaching_seats: on            # on | off | auto (auto = on for business fables / didactic fiction)
- domain_seats: auto            # on | off | auto (auto = on when technical_domain is set)
- custom_seats:
  - name: Pacing (tradition of Elmore Leonard)
    lens: leave out the part readers skip
    fires_on: description, transitions
    test: would a reader skim this paragraph?
- max_seats_per_pass: 5

## guardrails
- [The book's thesis, e.g. "the town saves itself; no outside rescuer"]
- [A protected beat, e.g. "the ch12 failure must come from the system working as designed"]
- [A character line, e.g. "the mentor never gives a direct answer"]
```

If the block is missing, use the default panel with `auto` for both optional groups.

## Swapping seats by genre

The three-axis structure (craft, teaching, domain truth) is portable. Swap seats to fit the book:

| Book | Suggested changes |
|------|-------------------|
| Literary fiction | Teaching off. Consider a sentence-level seat (tradition of a prose stylist you admire). |
| Thriller / technothriller | Domain seats on. Add a pacing seat focused on the ticking clock. |
| Crime / procedural | Keep Higgins and Price. Domain seats on for police, legal, or forensic procedure. |
| Business fable | Teaching on. Keep Kim and Goldratt; domain seats for the industry. |
| Historical | Domain seats become period-accuracy seats (material culture; institutions and law of the era). |
| Narrative nonfiction | Teaching on; domain seats on; the Price seat checks quoted speech against sources rather than inventing idiom. |

## Writing a custom seat

A seat needs five things:

1. **Name and tradition.** "In the tradition of [author]" for a craft seat drawn from published advice, or a practitioner role for a domain seat. Don't claim to be the person.
2. **Lens.** One or two sentences: what this seat sees that others miss.
3. **Rewrite moves.** Two to four concrete things it does to a line.
4. **A test.** One question that tells you whether the passage passes.
5. **Routes.** Which kinds of passage make it fire.

Keep seats distinct. If two seats would give the same note, merge them.

## Guardrails: how to write them

Guardrails are the Managing Editor's rung 2. Good guardrails are specific and checkable:

- A thesis stated as a line the book must not cross ("the book argues for X, not Y; watch for drift toward Y").
- Protected beats with a chapter reference and why they matter.
- Character lines ("she never apologizes on the page before chapter 20").
- Tone boundaries ("no cartoon villains; every antagonist is half right").

Avoid vague guardrails ("keep it good"); the board can't apply them.
