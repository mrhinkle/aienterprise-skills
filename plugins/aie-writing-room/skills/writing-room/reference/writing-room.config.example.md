# writing-room.config.md (example)

Copy this file to your project root as `writing-room.config.md` and edit it.
Every Writing Room skill reads it. Any field you leave blank falls back to the
default noted beside it. Paths are relative to the project root.

The values below describe an invented example novel. Replace all of them.

```yaml
# ── The book ────────────────────────────────────────────────────────────
title: "The Lighthouse Accounts"        # working title
genre: "literary mystery"                # drives realism and technical passes
audience: "adult general readers"
logline: >                               # one or two sentences; story-architect's anchor
  A harbor-town bookkeeper finds a ledger that shouldn't exist and has to
  decide who in her family she is willing to expose.
central_question: "What do we owe the people who kept our secrets?"

# ── Point of view and tense ─────────────────────────────────────────────
pov:
  mode: "close third"                    # first | close third | omniscient | mixed
  characters: ["Nell", "Arthur"]         # who may hold a POV; others never do
  rules:
    - "One POV per scene; switch only at a scene break."
    - "The antagonist never gets a POV scene."   # example of a mystery rule
tense: "past"                            # past | present

# ── Project files (all optional; skills degrade gracefully) ────────────
manuscript_glob: "chapters/*.md"         # where the prose lives
spine_doc: "docs/STORY-SPINE.md"         # story-architect: premise, thesis, act map
canon_ledger: "docs/canon-ledger.md"     # continuity-editor: facts, timeline, places
cast_ledger: "docs/cast-ledger.md"       # character-architect: who exists, function, tag
voice_profile: "docs/voice-profile.md"   # author-voice: the author's codified voice
ideas_backlog: "IDEAS.md"                # idea-backlog: the running list
memory_file: "docs/writing-room-memory.md"  # optional running notes; omit to disable

# ── House rules (make your own conventions explicit here) ──────────────
banned_words:                            # FAIL in the mechanical scan; ai-slop-killer
  - "suddenly"                           # adds its own default list on top of these
  - "utilize"
  - "very unique"
house_rules:                             # spelling/style rules enforced as FAIL
  - "email, not e-mail"
  - "Write out numbers under 100 in narration."
retired_names: []                        # old names that must never reappear
sanctioned_name_reuse: []                # deliberate collisions, with the reason
chiasmus_limit: 1                        # mirrored-phrase lines allowed per book

# ── Cast limits (character-architect) ──────────────────────────────────
max_round_characters: 7                  # characters allowed a real arc
max_new_named_per_scene: 3

# ── Domain accuracy (technical-editor) ─────────────────────────────────
technical_domain: "maritime insurance and small-town accounting"   # or "none" to skip

# ── Protection and approval ────────────────────────────────────────────
protected_passages:                      # beats no pass may cut or flatten
  - "Ch 3: the night-shift ledger reconciliation"
approval_required:                       # propose, never apply, changes of these kinds
  - plot
  - chapter_order
  - pov
  - ending

# ── Pipeline ───────────────────────────────────────────────────────────
optional_passes:                         # which bracketed passes run by default
  story_architect: false                 # true = always plan the beat first
  editorial_board: false                 # heavier revise pass after fiction-writer
  author_voice: true
  manuscript_reviewer: false             # score after the gate
checks_command: ""                       # e.g. "./tools/check.sh"; blank = built-in scan
git_workflow: "branch-and-pr"            # branch-and-pr | direct | none
```

## Notes on the fields

- **genre / audience** tune what `realism-editor` treats as believable and how much
  exposition `fiction-writer` allows.
- **pov.rules** are enforced by `fiction-writer` while drafting and by
  `continuity-editor` on review.
- **banned_words / house_rules** are your own. `ai-slop-killer` always runs its
  default list too; this list adds to it and never replaces it.
- **retired_names** grows over time. Each time `character-architect` renames or
  merges someone, the old name goes here so it cannot creep back.
- **protected_passages** keep a heavy revise pass from sanding off the scenes the
  book depends on.
- **approval_required** keeps agents from rewriting the plot while "just fixing
  continuity."

## Review and domain settings (editorial-board, technical-editor, realism-editor, manuscript-reviewer)

```yaml
technical_reference: "docs/domain-reference.md"  # technical-editor: what's true in your domain
research_cutoff: "2026-06"                        # facts after this date get flagged for re-checking
reader_profile: "docs/reader-profile.md"          # realism-editor + reader panel
guardrails:                                       # editorial-board rung 3; things no pass may break
  - "The town saves itself; no outside rescuer."
editorial_panel:                                  # see editorial-board/reference/panel-config.md
  seats: [king, higgins, price, domain-mechanism, domain-capability]
  teaching_seats: auto
  domain_seats: auto
  max_seats_per_pass: 5
rubric: ""                                        # optional JSON rubric for manuscript-reviewer; blank = default 8
reviewer_panel: []                                # optional custom reviewer personas
```
