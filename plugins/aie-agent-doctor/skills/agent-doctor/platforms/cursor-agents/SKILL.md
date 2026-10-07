---
name: agent-doctor-cursor-agents
description: Cursor / Grok Bot teammates module for Agent Doctor. How IDE agents differ from Hermes profiles, handoff etiquette, and avoiding dual-writers on the same host files. Trigger on "cursor agents doctor," "grok bot fleet," "teammate handoff," or when agent-doctor scopes Cursor agents.
---

# Agent Doctor — Cursor / Grok Bot teammates

IDE teammates (Cursor agents, Grok Bot, etc.) are **not** the same runtime as Hermes profiles:

| | Hermes profile | Cursor / Grok teammate |
| --- | --- | --- |
| Process | Host gateway / profile CLI | IDE agent session |
| Cron | Native Hermes cron | Usually none (or external) |
| Buzz | Often via `buzz-acp` | Different path unless explicitly bridged |
| Secrets | Profile `op` maps | Connector / IDE secrets |

## Doctor scope

- Score Hermes profiles with Hermes monitors.
- For teammates: track **handoff health** — clear ownership, no two writers on the same launchd unit / config file, proposals routed to the owner agent.
- Name collisions (a Hermes profile and a Grok teammate both called "ops-doctor") are fine if proposals say **"Hermes ops-doctor profile"** vs **"Grok ops-doctor"**.

## Dual-writer rule

If another agent already owns a live apply (Buzz ACP job, relay patch, etc.), **stand down** on those files. Status updates only. Colliding writers cause the exact outages the doctor exists to prevent.

## Messaging

Teammates talk to humans in IDE chat; fleet ops still prefer Slack outbound relay for durable doctor reports. Don't assume a teammate can restart host gateways.
