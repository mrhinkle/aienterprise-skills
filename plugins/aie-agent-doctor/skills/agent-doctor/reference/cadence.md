# Doctor cadence patterns

## Hourly pulse

**Goal:** cheap, boring, truthful.

- Offset the minute away from `:00 / :15 / :30 / :45` (e.g. `:07`) so you don't stampede shared APIs with other crons.
- **No LLM** (or cheapest possible). Script reads monitor output files / status endpoints already produced by the fleet.
- List exact paths in `doctor.config.md` → `monitors[]`.
- Write `scores-latest.json`. Exit non-zero only on scorer failure, not on yellow agents.
- Do **not** spawn parallel probes that duplicate existing rollcall, job-failure, or quota heartbeats.

## Daily checkup

**Goal:** human-readable prioritization.

- Slot clear of other morning briefs (leave buffer before/after CoS or standup jobs).
- Cheap-tier model override at the **job** level is fine; keep profile primary for interactive work.
- Deliver locally + relay to ops channel (Slack via outbound relay; Telegram only if that bot is profile-owned).
- Top 3 proposals max unless something is red.

## Weekly checkup

**Goal:** trends and debt.

- Place an hour before any weekly learning/retro so the retro can consume the report.
- Primary model OK.
- Include: score trends, aged proposals, config hygiene debt, messaging/gateway risks.

## Anti-patterns

- Sixth watcher that re-hits the same APIs as five existing monitors.
- Enabling inbound Slack Socket Mode on a host profile that shares an app with another gateway.
- Restarting the shared fleet gateway to "pick up" a doctor config change without a named override.
- Hourly LLM summaries that burn Codex/OpenRouter quota.
