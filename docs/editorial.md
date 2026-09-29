# Editorial skills (`aie-editorial`)

Four skills for writers and editors: capture a person's voice and write in it, enforce a publication's house style, run a developmental edit on a long manuscript, and explain AI concepts with 1980s analogies.

| Skill | One-line job |
|---|---|
| `voice-profile` | Build a voice profile from someone's transcripts or writing, then draft in that voice |
| `house-style` | Check or fix a draft against a configurable style guide |
| `developmental-editor` | Big-picture edit: editorial letter, chapter map, revision roadmap |
| `retro-analogies` | Plain-English AI explanations with an accurate 1980s pop culture analogy |

## What it does

**`voice-profile`** reads verbatim transcripts, posts, and published writing and distills them into a `voice-profile.md`: rhythm, storytelling moves, values, verbal tics with observed frequency, humor, reference pool, tone by format, banned words, and calibration lines. Every finding cites evidence and carries a confidence score. A privacy pass strips contact details and third-party personal information before the file is saved. In write mode it drafts newsletters, posts, emails, talks, and long-form passages that match the profile, then runs a final prose pass.

**`house-style`** loads your rules from a config file and applies them. Mechanical checks (banned words with inflections, spelling and hyphenation, required terms, citation format and freshness, formatting) run first; judgment checks (tone against "sounds like / never sounds like" pairs, a one-sentence reader value test, taxonomy and cross-linking) run second. Review mode returns a findings table with a PASS / FAIL verdict. Fix mode returns corrected text and a change log.

**`developmental-editor`** reads the whole manuscript, builds a reverse outline with word counts, and works through structural lenses: promise, spine, chapter jobs, proportion, entry and exit, plus fiction lenses (stakes, arc, scene versus summary, the lecture problem) or nonfiction lenses (reader job, argument architecture, evidence, redundancy, actionability). It does not line-edit or ghostwrite.

**`retro-analogies`** explains an AI concept for business learners in four parts: what it is, a 1980s analogy, why it matters in business, and where the analogy breaks. It describes references in its own words and does not reproduce lyrics or dialogue.

## Use it

Install the plugin, then ask in plain language:

```text
Here are six podcast transcripts. Build my voice profile.
Write a 150-word post about our pricing change in my voice.

Check this newsletter against our house style.
Fix the citations and banned words in draft.md.

Give me a developmental edit on the manuscript in ./chapters.
Does this whitepaper hold together?

Explain vector databases to a room of CFOs.
Give me a speaker-ready analogy for context windows.
```

The skills chain. A common pipeline for a bylined book or long piece:

1. `developmental-editor` for structure.
2. A drafting skill, or `voice-profile` in write mode, for new material.
3. A line-editing skill for sentences.
4. `house-style` for mechanics.
5. `ai-slop-killer` as the final prose pass.

## Inputs and outputs

| Skill | Inputs | Outputs |
|---|---|---|
| `voice-profile` (build) | Transcripts, posts, articles; ideally 5,000+ words across 3+ contexts | `voice-profile.md` in the project root, plus a confidence summary |
| `voice-profile` (write) | A brief, a format, and at least one concrete anchor (a number, name, or memory) | Draft in the voice |
| `house-style` | A draft and a `house-style.md` config (falls back to built-in defaults) | Review table with verdict, or corrected text with change log |
| `developmental-editor` | A full manuscript: Markdown folder, .docx, PDF, pasted text, or a document connector | Editorial letter (Markdown) with chapter map and revision roadmap |
| `retro-analogies` | An AI term or concept, optionally an audience and format | Four-part explanation sized for talk, slide, post, or handout |

## Configure per skill

### `voice-profile`

- **Profile location:** defaults to `./voice-profile.md`. Name another path when you ask ("save it to `profiles/dana.md`"); write mode checks the project root and any path you give.
- **Template:** edit `skills/voice-profile/reference/voice-profile.template.md` to add or drop dimensions.
- **Consent:** build profiles only for yourself or for someone who has agreed to it.
- **Example:** `reference/example-profile.md` shows a filled profile for a fictional person.

### `house-style`

- Copy `skills/house-style/reference/house-style.config.example.md` to `house-style.md` in your project root (or `.claude/house-style.md`) and edit it.
- Sections: publication, reader value test, tone, banned words and phrases, spelling and hyphenation, required terms, citations, formatting, taxonomy and cross-linking, visual brand, review checklist. Every section is optional.
- Set `blocking: true` on any section to make its failures block a PASS.
- Unknown sections are applied as plain instructions, so you can add house rules without changing the skill.

### `developmental-editor`

- **Output format:** Markdown by default; ask for another format if you need one.
- **Handoffs:** the roadmap names whatever drafting, line-editing, and style skills you have installed.
- **House rules:** if `house-style.md` exists, the letter follows its banned words and spelling rules.
- **Letter shape:** edit `reference/editorial-letter.template.md` to match how your team gives notes.

### `retro-analogies`

- **Starting pairings:** extend `reference/analogy-bank.md` with references that work for your audience.
- **Decade:** the skill is built around the 1980s. To change eras, edit the reference selection rules in `SKILL.md` and swap the analogy bank.
- **House rules:** follows `house-style.md` if present.

## Final prose pass

`voice-profile`, `house-style`, and `developmental-editor` call the `ai-slop-killer` skill as a last pass when it is installed. House style and voice-profile banned words are re-checked after that pass, and win any conflict.
