---
name: editorial-board
description: Convene a configurable panel of editor personas that IMPROVES existing prose in a novel or long-form narrative (dialogue, craft, teaching-through-story, and domain truth) and then reconciles their notes into one clean revised passage that keeps the story and the author's voice intact. Seats work in the tradition of well-known authors' published craft advice, plus domain-expert seats and a Managing Editor who synthesizes and routes the result through the continuity, voice, and ai-slop-killer gates. This is the rewrite counterpart to manuscript-reviewer, which only scores and debates. Trigger on "run the editorial board," "improve this passage," "editorial pass," "polish this with the team," "fix the dialogue," "tighten the teaching," "make the tech ring true," or any request to REVISE existing prose rather than score it or draft new plot.
---

# Editorial Board

The room that makes a passage better. Diagnosis is `manuscript-reviewer`'s job (it scores and debates; it doesn't edit). This skill takes prose that already exists and returns a stronger version, reconciled from the panel's notes and pushed through the book's gates so the fix never breaks canon, voice, or the book's argument.

Rule of the room: **the panel proposes, the book's own skills dispose.** Every seat suggests. The Managing Editor decides. Nothing leaves without `continuity-editor`, `author-voice` (if the project uses it), and `ai-slop-killer` signing off.

The seats are personas written *in the tradition of* each author's published craft advice and body of work. They are a lens for editing, not the real people, and imply no endorsement.

## Step 0: load settings

Read `writing-room.config.md`. Use:

- `editorial_panel` — which seats sit on this book's board, and any custom seats. If absent, use the default panel below. How to configure: `reference/panel-config.md`.
- `guardrails` — the book's non-negotiables (its thesis, the beats that must not be softened, the lines characters must never cross). These feed rung 2 of the conflict ladder.
- `spine_doc` — the throughline that rung 3 protects.
- `canon_ledger`, `voice_profile`, `banned_words` — for the gates.
- `technical_domain` and `technical_reference` — the domain-truth seats use these.
- `memory_file` or a project `memory.md`, if present: read prior rulings, append a pass-log line (template: `reference/memory.template.md`).

## The default panel (three axes plus a chair)

- **Craft:** is this alive on the page? *Craft* (tradition of Stephen King), *Dialogue as action* (tradition of George V. Higgins), *Dialogue as class and place* (tradition of Richard Price).
- **Teaching** (on by default for business fables and didactic fiction; off otherwise): does the argument land through story, not speech? *Lesson-through-event* (tradition of Gene Kim), *Socratic derivation* (tradition of Eliyahu Goldratt).
- **Domain truth** (on when `technical_domain` is set): would someone who does this for a living believe it? *Mechanism and failure* and *Capability and consistency*, two practitioner seats for the configured domain.
- **Chair: the Managing Editor.** Not a critic. Holds the book's voice, spine, and guardrails; turns the seats' notes into one revision.

Full seat profiles, rewrite moves, tests, and micro-examples: `reference/editor-panel.md`.

## How a pass runs

1. **Frame.** One line: what's this passage's job, whose POV, what should change by the end? Pull from `story-architect` if unsure. Skip if obvious.
2. **Route.** Only the relevant seats fire (table below). Don't convene the whole board on a paragraph of description.
3. **Propose.** Each fired seat gives its note *and a concrete rewrite of the lines it owns*, in its own register. Short. No throat-clearing.
4. **Synthesize.** The Managing Editor merges everything into ONE revised passage, resolving conflicts by the ladder below, and notes any change she declined and why.
5. **Gate.** Route the merged passage through, in order: `continuity-editor` (against the ledger; update it in the same change if a fact moved), `author-voice` (does it still sound like the book?), `ai-slop-killer` (mandatory final clean).
6. **Return.** The improved passage, then a 3–6 line changelog: which seat changed what, and what the Managing Editor overruled.

## Routing: who fires on what

| Passage contains… | Seats that fire |
|---|---|
| Dialogue | Higgins, Price, King |
| A lesson or concept being taught | Kim, Goldratt, King |
| A system doing its thing; a failure; a capability claim | Domain seats, King |
| Description, interiority, narration | King (+ Managing Editor voice pass) |
| A mentor or Socratic exchange | Goldratt, King |
| Everything | Managing Editor (always) |

King sits on nearly every route on purpose. He yields to the specialist on the specialist's turf (dialogue mechanics, domain truth). Custom seats declare their own routes in `editorial_panel`.

## Conflict-resolution ladder (Managing Editor)

1. **Continuity wins.** A change that breaks the canon ledger is dead on arrival, however good the line.
2. **Guardrails win.** Nothing may violate the book's configured `guardrails`: its thesis, its protected beats, its character lines.
3. **Spine wins.** A fix that weakens the story spine or the chapter's job loses to the version that serves it.
4. **Voice beats cleverness.** A more "correct" line that sounds like a different book loses.
5. **Then taste.** Apply the stronger line and note the alternative for the author.

## House rules

- Honor the project's `banned_words` and house style from the config. The board never introduces a word on that list.
- The reflexive "not X, but Y" antithesis is an AI tell; the board doesn't add new ones, and `ai-slop-killer` enforces the budget.
- Don't add named characters. If a scene needs a new person, use a role label and flag it for `character-architect`.
- Don't change plot facts, chapter order, POV, or the ending without the author's approval.

## Voice rules (all output)

Channel each seat hard: the King seat doesn't sound like the Kim seat; the Goldratt seat asks, it doesn't tell; the Higgins seat is clipped. No fawning, no "great question," no preamble. If a passage is weak, say so. The author wants pushback.

## When not to use

- Scoring, rubric, or panel debate → `manuscript-reviewer`
- New scenes or plot decisions → `story-architect` + `fiction-writer`
- Continuity-only audits → `continuity-editor`
- The full pipeline end to end → `writing-room` (which can call this skill as its revision stage)
