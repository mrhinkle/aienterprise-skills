# voice.config.md (example)

Copy this file to `voice.config.md` in the working directory and edit it. The LinkedIn and X skills read it only when it is present. They do not parse this example in place. Delete any field you do not want to set.

```yaml
# Who is speaking. Use a fictional stand-in here; put the real person in your copy.
name: "Alex Rivera"
role: "operator who writes for practitioners"
# How the posts should sound. Short phrases, not a brand manifesto.
tone:
  - "plain-spoken"
  - "specific"
  - "no hype"
# Words and patterns the draft must not use.
banned:
  - "synergy"
  - "circle back"
emoji: false
# LinkedIn skill uses 0-3; X skill uses 0-1. Set 0 to ban them.
hashtags: 0
# How hard to press on citations inside the post.
citations: "name the source in the sentence; full URL only in the source log"
```

Nothing in this file overrides the research rules. A config cannot permit an unsourced statistic.
