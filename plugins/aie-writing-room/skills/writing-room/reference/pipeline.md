# Pipeline detail

## Pass-by-pass hand-off

| # | Skill | Optional? | Reads | Hands forward |
|---|-------|-----------|-------|---------------|
| 1 | `story-architect` | yes | spine doc, target | a scene brief: one job, POV, stakes, what changes, end pull |
| 2 | `fiction-writer` | no | brief, voice profile, canon ledger | draft or revised prose |
| 2b | `editorial-board` | yes | draft | one reconciled revised passage |
| 3 | `character-architect` | no | cast ledger, draft | cast notes, naming fixes, ledger updates |
| 4 | `technical-editor` | skip if `technical_domain: none` | draft, domain notes | accuracy fixes for the book's specialist subject matter |
| 5 | `realism-editor` | no | draft | fixes for anything a reader would not believe (behavior, logistics, money, time) |
| 6 | `continuity-editor` | no | canon ledger, draft | contradictions found, ledger updates |
| 7 | `author-voice` | yes | voice profile, draft | voice-matched prose |
| 8 | `ai-slop-killer` | **never** | draft, `banned_words` | clean prose; always last on any prose |
| 9 | `manuscript-reviewer` | yes | gated prose | scores and a revision priority list |

Content passes (3 to 6) fix what they own and flag everything else for its owner. A pass that notices a problem outside its lane writes a note, not an edit.

## Built-in mechanical scan (when no `checks_command` is set)

Run over the target files and classify each hit:

- **FAIL**
  - any word from the config's `banned_words`
  - any name in `retired_names` (a renamed or cut character reappearing)
  - any violation of a `house_rules` spelling rule
- **REVIEW**
  - em-dash density above roughly 1 per 150 words in a passage
  - "not X, but Y" / "it's not X, it's Y" antithesis constructions
  - chiasmus and mirrored-phrase lines (limit set by `chiasmus_limit`, default 1 per book)
  - three-item lists in consecutive sentences
  - a named character absent from the cast ledger
  - a chapter or scene ending that summarizes instead of pulling forward

A simple implementation is a grep per list plus a short script for densities. Projects that outgrow that should point `checks_command` at their own checker.

## Gate criteria

A target passes the Writing Room only when all hold:

1. Mechanical scan: **0 FAILs**.
2. Every REVIEW flag either fixed or consciously kept, with a one-line reason.
3. Canon ledger and cast ledger updated for every new or changed fact, name, or role.
4. Any change of a kind listed in `approval_required` is proposed to the author, not applied.
5. `ai-slop-killer` was the last pass to touch the prose.

Only after the gate: optionally run `manuscript-reviewer` to score.

## REVIEW-mode report shape

```
# Writing Room review: <target> (<date>)
## Mechanical scan    FAIL: n   REVIEW: n
## Findings by pass
### character-architect
- [location] finding → suggested fix
...
## Priority list (top 5, highest payoff for effort first)
```
