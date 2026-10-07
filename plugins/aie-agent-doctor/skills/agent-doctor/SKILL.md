---
name: agent-doctor
description: Fleet / multi-agent health doctor. Diagnoses availability, job reliability, model/quota, config hygiene, improve posture; optional quality; scores 0–100; proposes patch keys — never applies until a human names the apply. Modules for orchestrators (Hermes+), Slack, Telegram, Buzz, Mission Control, LLM providers, Composio, 1Password, Bitwarden, Cursor teammates, Langfuse/OTel. Trigger on "agent doctor," "fleet health," "health score," "composio connections," "diagnose agents," or "score my agents."
---

# Agent Doctor

**Diagnose and propose.** Do not mutate configs, restart shared gateways, rotate secrets, open OAuth links, or post externally until a human explicitly names the change (`apply <patch-key>`).

Load platform modules under `platforms/*/SKILL.md` on demand. Scoring: `reference/rubric.md`. Cadence: `reference/cadence.md`. Config: `doctor.config.md` (see example + JSON Schema). Adapters: `adapters/README.md`.

## Core heuristics

1. **Propose-then-apply.** Exact before/after; wait for named apply.
2. **Don't duplicate monitors.** Pulses *read* existing outputs / adapter status.
3. **Cheap for frequent, rich for rare.** Hourly = no-LLM.
4. **Messaging safety.** One inbound realtime session per Slack/Telegram app; doctor prefers outbound relay.
5. **Shared gateways are sacred.** No unnamed restarts.
6. **Integrations are scored.** Required Composio toolkits must be Active; vaults (1Password / Bitwarden) authorized/unlocked when expected.
7. **Depersonalize.** Site paths and agent ids live in `doctor.config.md`, not public heuristics.

## Nested platform skills

| Module | Use when |
| --- | --- |
| hermes (orchestrator) | Profiles, cron, gateway, ACP |
| slack / telegram | Messaging integration contracts |
| buzz | Buzz ACP relays / allowlists |
| mission-control | Ops dashboards |
| llm-providers | OpenRouter, Codex, fallbacks, context util |
| composio | Required app connections Active? |
| secrets-1password / secrets-bitwarden | Vault auth + required items |
| cursor-agents | IDE teammates vs orchestrator profiles |
| langfuse-otel / crewai-autogen | Observability / framework health |

## Optional usage pattern (Huberman-style doctor)

A dedicated doctor agent runs hourly no-LLM pulse → `scores-latest.json`; daily/weekly narratives via outbound Slack relay; humans approve with `apply <key>`. Nickname optional.
