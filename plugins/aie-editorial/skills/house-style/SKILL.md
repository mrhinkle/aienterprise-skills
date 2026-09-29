---
name: house-style
description: Enforce a configurable editorial style guide on any draft, covering banned words, spelling and hyphenation rules, citation format, tone, formatting, and a "reader value" test. Use when someone says "check this against our style guide," "house style," "style check," "brand compliance," "scan for banned words," "fix the citations," "is this on-voice," or before publishing a newsletter, blog post, report, or site copy for a publication with its own rules.
---

# House Style

Every publication has rules that no general-purpose writer knows: words it will not print, a spelling it insists on, how it cites a statistic, what every piece must do for the reader. This skill reads those rules from a config file and applies them, either as a review or as a rewrite.

The rules live in config, not in this skill. Swap the config and the same skill enforces a different publication's style.

## Step 1: Load the config

Look in this order and use the first one found:

1. A path the user names.
2. `house-style.md` in the project root.
3. `.claude/house-style.md`.
4. `reference/house-style.config.example.md` in this skill (the built-in defaults).

Tell the user which config you loaded. If you fell back to the defaults, say so in one line and suggest copying the example to `house-style.md` to customize it.

The config format is documented in `reference/house-style.config.example.md`. Unknown sections are allowed; apply them as written instructions.

## Step 2: Pick the mode

- **Review** (default for "check," "review," "audit"): leave the text alone and return a findings report.
- **Fix** ("fix," "apply," "clean up," "make it compliant"): return the corrected text plus a short change log.
- **Write** (drafting new copy): apply the config while drafting, then run a review pass on your own output before handing it over.

## Step 3: Run the checks

Run every section present in the config, in this order. Mechanical checks first, judgment checks second.

### Mechanical
1. **Banned words and phrases.** Case-insensitive, whole-word, including inflections (a ban on "utilize" also catches "utilized" and "utilizing"). Check headings, captions, alt text, and link text too. For each hit, propose a plain replacement, not a synonym from the same family.
2. **Spelling and hyphenation.** Apply each rule in the config's spelling table. Watch compound modifiers: a rule like "open source is never hyphenated" applies even before a noun ("open source project").
3. **Required terms.** Product names, capitalization, trademarks, as listed.
4. **Citations.** Every statistic, quote, and factual claim that is not common knowledge needs a source in the configured format. Flag unsourced claims, stats without a year, dead or placeholder links, and sources older than the configured freshness window.
5. **Formatting.** Heading levels, list-versus-prose balance, table usage, bold usage, length limits, per the config.

### Judgment
6. **Tone.** Compare against the config's tone description and its "sounds like / never sounds like" pairs. Quote the sentences that miss.
7. **Reader value test.** Answer the config's reader-value question in one sentence for the piece as a whole. If you cannot, that is the top finding. Then check each section: does it serve that answer?
8. **Cross-linking and taxonomy.** If the config defines sections, pillars, or categories, confirm the piece is tagged and links to the required number of others.

## Step 4: Report

For **Review** mode:

```
# House Style Review: <title>
Config: <path>   Verdict: PASS | PASS WITH FIXES | FAIL

## Blocking
| # | Rule | Location | Found | Fix |
|---|---|---|---|---|

## Non-blocking
| # | Rule | Location | Found | Suggestion |
|---|---|---|---|---|

## Reader value
<One sentence answer, or why it cannot be answered.>

## Checklist
- [x] / [ ] one line per config section
```

Blocking = banned words, spelling rules, missing citations on stats, failed reader-value test. Everything else is non-blocking unless the config marks it `blocking: true`.

For **Fix** mode, return the full corrected text, then a change log grouped by rule. Do not change meaning, claims, or structure beyond what a rule requires; flag those instead.

## Step 5: Final prose pass

After house rules are applied, run the `ai-slop-killer` skill on the output if it is installed. Then re-run the banned-word and spelling checks, because a prose pass can reintroduce them. House rules win any conflict.

## Rules for the skill itself

- Never invent a source to satisfy the citation rule. Flag the claim as unsourced and leave a `[citation needed]` marker.
- Do not enforce a rule the config does not contain. General taste goes under "Non-blocking" and is labeled as a suggestion.
- A voice profile (from the `voice-profile` skill) governs rhythm and personality; house style governs mechanics. When they conflict on a banned word or spelling, house style wins. On tone, the voice profile wins for bylined pieces.
- Visual brand rules in the config (colors, fonts) apply only when the task produces styled output (HTML, slides, images).

## Reference files

- `reference/house-style.config.example.md` — the config format, filled with sensible defaults. Copy it to `house-style.md` and edit.
