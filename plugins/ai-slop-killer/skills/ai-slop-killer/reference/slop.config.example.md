# slop.config.md — example house-rules file (optional)

Copy this to your working directory as `slop.config.md` and edit. Delete any section to fall back to defaults. Nothing here is required; the skill works with no config at all.

```yaml
# Extra words to hard-ban on top of the documented default banlist.
banned_words:
  - synergize
  - circle back
  - move the needle

# Documented-tell words YOU legitimately use — stops false positives.
allowed_words:
  - open source        # a real term for you; never "flag" it
  - robust             # if it's genuinely the right word in your domain

# Voice to preserve. Name a voice/style skill, or write a short note.
voice: "my-writing-style"      # or e.g. "plain, direct, first-person, dry humor"

# Do factual claims need an inline source?  required | preferred | off
citations: preferred

# Per-channel overrides.
channel_defaults:
  social:   { emoji: allow, max_words: 300 }
  newsletter: { emoji: sparing }
  docs:     { emoji: forbid, headers: allow }
  fiction:  { citations: off, mode: fiction }

# Fiction: metaphors to deploy once then stop repeating (series bibles).
fiction_metaphor_budget:
  - jazz/symphony: 1 per movement
  - <your recurring motif>: 1 per book
```

## Notes
- With **no config**, defaults apply: documented banlist, `citations: preferred`, emoji sparing, preserve whatever voice the text already has.
- `allowed_words` is the pressure valve — every domain has a "robust" or an "ecosystem" that's the correct term. List them and the skill stops nagging.
- Keep the file short. It's house rules, not a style bible.
