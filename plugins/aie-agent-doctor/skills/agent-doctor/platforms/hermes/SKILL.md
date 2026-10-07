---
name: agent-doctor-hermes
description: Hermes platform module for Agent Doctor. Profiles, cron jobs, shared vs dedicated gateways, ACP wrappers, fallbacks, and propose-then-apply patch discipline. Load when diagnosing Hermes agent fleets. Trigger on "hermes doctor," "hermes health," "profile cron," or when parent agent-doctor scopes Hermes.
---

# Agent Doctor — Hermes

Diagnose Hermes **profiles**, **cron**, **gateway**, and **ACP** wrappers. Propose patch keys; do not apply until named.

## What to check

### Availability
- Expected profile directories exist; config parses.
- Shared host gateway process healthy if the fleet uses one gateway for many profiles.
- Dedicated `hermes -p <profile> gateway run` jobs (if any) are isolated — **no `--replace`** that would steal the shared gateway.
- ACP wrappers: CLI flag passthrough bugs (wrapper eating `-p` / profile flags) show up as immediate exit codes — check logs before blaming the model.

### Job reliability
- Per-profile cron success over last 24h; paused jobs intentional vs accidental.
- Prefer reading existing job-failure / rollcall artifacts over re-invoking `hermes` for every pulse.

### Model / quota
- `model.default` + `fallback_providers` (aim for **two rungs** when policy says so).
- Job-level model overrides for high-frequency crons (cheap tier) so interactive primary quota stays free.
- Retire banned/broken local models from fallback chains (see parent + llm-providers module).

### Config hygiene
- `secrets.onepassword.cache_ttl_seconds` — prefer longer TTL (e.g. 3600) under rate limits; don't copy a short override into new profiles by accident.
- `platforms.slack.enabled` / `platforms.telegram.enabled` — most fleets keep these **false** on shared-gateway hosts; messaging via outbound relay instead.
- Backup config before any apply; patch keys only.

### Improve posture
- Open doctor proposals aged &lt;7d.
- Drift vs last known-good backup of profile configs.

## Safe change patterns

| Intent | Prefer | Avoid |
| --- | --- | --- |
| Doctor Slack reports | cron → outbound relay JSON | Enabling Slack on shared host gateway |
| New interactive bot | Separate Slack/Telegram app + dedicated gateway job | Reusing another profile's Socket Mode app |
| Config pickup | Profile-scoped reload paths documented by Hermes | Unnamed shared `gateway` restart |
| Local model swap | Named apply after install verified | Silent primary flips mid-flight |

## Proposal shape

```
apply <key>
profile: <name>
files: [paths]
before → after: (minimal diff)
risk: gateway | cron | secrets | none
verify: <command or log signal>
```
