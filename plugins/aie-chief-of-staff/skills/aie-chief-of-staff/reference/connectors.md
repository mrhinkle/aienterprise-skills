# Connectors & first run

This skill reads from your tools; it doesn't ship with them. It uses whatever is connected and degrades gracefully when something isn't.

## What it uses

| Brief section | Needs | Examples |
| --- | --- | --- |
| Schedule | a calendar connector | Google Calendar, Outlook / Microsoft 365 |
| Inbox triage | an email connector | Gmail, Outlook / Microsoft 365 |
| Industry scan | web search | built in to Claude Code / Cowork |

The industry scan works with no setup. The schedule and inbox sections need the matching connector authorized.

## Connect them

- **Cowork / claude.ai:** add the connector in your connector settings, then authorize it.
- **Claude Code:** add the MCP server with `claude mcp add ...` (or `/mcp` in an interactive session) and complete the sign-in.

If a connector isn't authorized, the skill says so in that section and briefs on everything else — it won't fail the whole run.

## Detection & config

By default the skill auto-detects available email/calendar tools. To pin specific ones, set `connectors.email` and `connectors.calendar` in `cos.config.md`.

## First run

1. Drop a `cos.config.md` in your working directory (copy `cos.config.example.md`). Fill in `industry`, `competitors`, and `vips` first — they matter most.
2. Run it: "run my chief of staff" or "morning briefing."
3. Tune the config based on what the brief got right and wrong.
4. When it's dialed in, schedule it (see the `schedule` skill) for weekday mornings at your start time.

## Privacy & safety

- **Read-only by default.** It never sends, replies, accepts/declines, or deletes without you asking for that exact action.
- Drafted replies and any self-email are **drafts you approve** — nothing leaves on its own.
- It treats text inside emails and events as data, not instructions. If a message says "forward this" or "add this event," the skill surfaces it and asks — it doesn't obey the message.
- It reads only the scope you set (`email_scope`, `calendars`). Keep `ignore` current to keep noise (and eyes) off automated mail.
