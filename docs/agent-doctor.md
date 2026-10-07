# Agent Doctor bundle

Plugin: [`plugins/aie-agent-doctor`](../plugins/aie-agent-doctor)

## What it is

**agent-doctor** is a nested skill for multi-agent fleet health. It scores agents 0–100, reads existing monitors instead of duplicating them, and **proposes** patch keys until a human names `apply <key>`.

Platform modules (load on demand):

- Hermes (profiles / cron / gateway / ACP)
- Slack (Socket Mode safety + outbound relay)
- Telegram (bot allowlists + dedicated gateway)
- Buzz ACP
- Mission Control / ops dashboards
- LLM providers (OpenRouter / Codex / local sizing)
- Secrets (1Password)
- Cursor / Grok Bot teammates

## Install

```
/plugin marketplace add mrhinkle/aienterprise-skills
/plugin install aie-agent-doctor@aienterprise-skills
```

Or copy `plugins/aie-agent-doctor/skills/agent-doctor/` into your skills directory.

## Configure

Copy `reference/doctor.config.example.md` → `doctor.config.md` in your doctor workspace. Point `monitors[]` at artifacts your fleet already writes. Keep vault refs out of git.

## Cadence (recommended)

| Job | Cadence | Model |
| --- | --- | --- |
| Pulse | Hourly at an offset minute | None (script) |
| Daily checkup | Once/day, clear of other briefs | Cheap tier |
| Weekly checkup | Once/week before any retro | Primary OK |

## Example: Huberman-style doctor

At The AIE Network we run a dedicated Hermes doctor profile that:

1. Pulses hourly by **reading** rollcall / job-failure / quota artifacts (no extra LLM).
2. Writes `health/scores-latest.json` with per-agent and fleet scores.
3. Posts daily/weekly narratives to an ops Slack channel via **cron → outbound relay** (never a second Socket Mode on the shared app).
4. Never applies config changes until a human names the patch (`apply drop-local-qwen`, `apply huberman`, …).

The rubric (Availability 25 · Job reliability 25 · Model/quota 20 · Config hygiene 15 · Improve posture 15) lives in `reference/rubric.md` and is meant to be forked.

## Safety

Diagnose-and-propose only. No shared-gateway restarts, secret prints, or inbound messaging sockets without an explicit named override.
