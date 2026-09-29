# Writing Room bundle (`aie-writing-room`)

A fiction writing room in eleven skills. One orchestrator (`writing-room`) takes a scene, chapter, or whole manuscript through the other passes in a fixed order, carries each pass's notes forward, and gates the result. Each pass also works on its own.

Everything specific to your book (title, POV rules, cast, canon, voice, banned words, domain) lives in one file, `writing-room.config.md`, at your project root. Nothing about any particular book is baked in.

## The pipeline

```
[story-architect] → fiction-writer → [editorial-board] → character-architect →
technical-editor → realism-editor → continuity-editor → [author-voice] →
ai-slop-killer → [manuscript-reviewer]
```

Bracketed passes are optional; turn them on under `optional_passes` in the config. `ai-slop-killer` (from the `ai-slop-killer` plugin) is always the last pass on prose, so install both.

## Skills

| Skill | One-line job |
|---|---|
| `writing-room` | Run the full pipeline in order and gate the result |
| `story-architect` | Decide what a scene or chapter must do before it's drafted: job, stakes, throughline, end-of-chapter pull |
| `fiction-writer` | Draft and revise scenes with goal, conflict, consequence, subtext, and clean POV |
| `editorial-board` | A configurable panel of editor personas that improves a passage and reconciles the notes into one revision |
| `character-architect` | Cast and audit characters: function, want and need, tag, choice under pressure, confusable names |
| `technical-editor` | Check domain content (AI, medicine, law, finance, whatever you set) for accuracy and legibility |
| `realism-editor` | Check that dilemmas and everyday mechanics ring true for the intended reader; no strawmen |
| `continuity-editor` | Continuity only: names, facts, timeline, places, objects, world rules, against your canon ledger |
| `author-voice` | Match prose to the author's voice profile; builds the profile from sample chapters if none exists |
| `manuscript-reviewer` | Score against a weighted rubric, then run writer-panel and reader-panel debates |
| `idea-backlog` | Capture and weigh candidate ideas in `IDEAS.md` without acting on them |

## Use it

```text
Run the writing room on chapter 7.
Plan the next chapter before I draft it.
Check chapter 12 for continuity against the canon ledger.
Run the editorial board on this scene.
Score the manuscript and run the reader panel.
Park this idea: what if the lighthouse keeper knew all along?
```

## Inputs / outputs

- **In:** a scene, chapter, or manuscript path, plus `writing-room.config.md`.
- **Out:** revised prose, a pass-by-pass change log, and a gate verdict. The reviewer adds a scorecard and debate transcript. Ledgers (canon, cast, ideas) are updated only with your approval.

## Configure

Copy `plugins/aie-writing-room/skills/writing-room/reference/writing-room.config.example.md` to your project root as `writing-room.config.md`. Key fields:

- `title`, `genre`, `pov`, `tense`: the basics every pass reads.
- `manuscript_glob`, `spine_doc`, `canon_ledger`, `cast_ledger`, `voice_profile`, `reader_profile`, `technical_reference`: paths to your project files. Templates for each ledger ship in the relevant skill's `reference/` folder.
- `banned_words`, `house_rules`, `retired_names`: hard rules enforced as FAIL.
- `technical_domain`: set it to your book's domain, or `none` to skip the technical pass.
- `editorial_panel`, `rubric`, `reviewer_panel`: swap editor seats, rubric dimensions, and reviewer personas per book.
- `optional_passes`, `checks_command`, `git_workflow`: how the orchestrator runs.

## Notes

- Editor and reviewer personas are editing lenses "in the tradition of" authors' published craft advice. They are not the real people.
- Each skill can keep an optional running `memory.md` in your project; a template ships in each skill's `reference/` folder.
- The continuity editor reports contradictions and asks before changing canon. It never "fixes" the ledger to match a mistake in the prose.
