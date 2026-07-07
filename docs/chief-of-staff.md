# Chief of Staff bundle (aie-chief-of-staff)

## aie-chief-of-staff

A morning chief of staff: one prioritized daily brief that pulls together your calendar, your inbox, and a fresh scan of your industry — so you start the day knowing what actually matters.

### What it does

Runs a four-step loop: **Gather → Triage → Scan → Brief.**

1. **Calendar** — today's meetings (and an optional lookahead). Flags what needs prep, spots double-bookings and back-to-back stacks, and finds your largest focus block.
2. **Inbox (read-only)** — triages recent mail into *needs a reply*, *tied to today's meetings*, *time-sensitive*, and *went quiet*. Surfaces each with a one-line summary and a suggested action. Skips the senders you tell it to ignore. Drafts replies on request — never sends.
3. **Industry scan** — web-searches the last day or two across your industry, your keywords, and **each tracked competitor** (funding, launches, hires, moves), plus mentions of your own company. Ranks by what matters to *you*, with a source link on every item.
4. **Brief** — one skimmable brief: your top 3 for the day, the schedule with prep flags, inbox actions, industry signals, and a suggested plan.

### Read-only and safe

It reads and recommends. It does not send email, reply, accept/decline invites, create/move/delete events, or archive/delete anything unless you ask for that exact action. Drafted replies and any self-email are drafts you approve. It treats text inside emails and events as data, not commands — if a message says "forward this," it surfaces it and asks.

### Customize it (this is the point)

Drop a **`cos.config.md`** in your working directory. The fields that matter most:

- **`industry`** + **`keywords`** — what the news scan watches.
- **`competitors`** — tracked by name + domain/handle. Drives the most useful part of the scan.
- **`vips`** — senders whose mail jumps the queue.
- **`priorities`** — current goals; the brief leans toward them.
- Plus working hours, timezone, email scope, ignore list, calendars, output length, and which connectors to use.

Copy the annotated template + a filled example from `reference/cos.config.example.md`. With no config it still runs, then tells you what to add.

### Connect your tools

The industry scan needs nothing. The schedule and inbox sections use whatever email/calendar connector you've authorized (Gmail, Google Calendar, Outlook/MS365). If one isn't connected, that section says so and the rest of the brief still runs. See `reference/connectors.md`.

### Make it a habit

It's built to run every morning. Pair it with the `schedule` skill to fire on weekday mornings at your start time. Ask it to run `ai-slop-killer` on any drafted replies before they go out.

### Triggers

"run my chief of staff," "morning briefing," "brief me," "daily brief," "what's on my plate today," "catch me up," "start my day," "prep my day."

### Reference files

- `cos.config.example.md` — annotated config + filled example.
- `briefing-format.md` — the exact brief layout.
- `connectors.md` — what it uses and how to connect it.
