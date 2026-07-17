# Sample run — aie-skill-creator (audit mode)

A condensed audit of a deliberately weak skill — the kind that "never triggers." The input skill is fictional; the audit output shape and the fix are exactly what a live run produces.

## Input skill

```yaml
---
name: meeting-notes
description: Helps with meetings.
---
# Meeting Notes
Take good notes and summarize the meeting. Include action items.
```

## Audit output

```
Skill: meeting-notes   Score: 7/20

Fix now:
- Triggerability (0) — "Helps with meetings" matches nothing a person types. Rewrite
  concrete + keyword-rich + trigger phrases. This is why it never fires.
- Clear procedure (0) — two sentences of vibes; a stranger can't follow it. Add a
  numbered loop: ingest transcript → extract decisions → extract action items
  (owner + due date) → draft summary → output format.
- Defined I/O (1) — input (a transcript? a live call? pasted notes?) is never stated;
  output shape is implied, not shown. Add an output template.
- Progressive disclosure (0) — no reference files, but also nothing to defer yet;
  fine to skip until the summary template grows.

Nice to have:
- Safety (1) — harmless as-is, but if it ever drafts follow-up emails, add the
  draft-only gate.
```

## The fix applied (description rewrite — the highest-leverage change)

```yaml
---
name: meeting-notes
description: Turn a meeting transcript or raw notes into a structured summary —
  decisions made, action items with owner and due date, open questions, and a
  3-sentence TL;DR. Works on pasted text, transcript files, or call recordings'
  transcripts. Trigger on "summarize this meeting," "meeting notes," "extract
  action items," "what did we decide," or "write up this call."
---
```

Trigger test: fires on "summarize this meeting" / "extract action items"; does not fire on "schedule a meeting" (different job — calendar, not notes). Cold-run test: run on a 40-minute transcript produced the promised four sections. Score after fixes: 17/20.
