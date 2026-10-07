---
name: agent-doctor-composio
description: Composio integrations module for Agent Doctor. Verifies required app connections are Active (COMPOSIO_MANAGE_CONNECTIONS list-only); fails score on missing, expired, or needsAuth. Trigger on "composio doctor," "composio connections," "toolkit auth," or when agent-doctor scopes Composio.
---

# Agent Doctor — Composio

Third-party app connections are part of fleet health. If Gmail/Slack/GitHub/etc. are required for an agent to do its job, a disconnected toolkit is an **Availability** failure — not a footnote.

## Hard rules

1. **Pulse is read-only.** Use connection **list/status** only (`action: "list"`). Never `add`, `rename`, or `remove` during a doctor pulse.
2. **Never invent toolkit slugs.** Required slugs come from `doctor.config` (and optionally from a prior search catalog). Typo’d names look like “missing” and poison scores.
3. **Never execute toolkit tools** from the doctor to “probe” an app. Status is enough.
4. **Propose reconnect; don’t silently OAuth.** Opening auth links is a human-facing apply (`apply composio-reconnect-<toolkit>`), not an hourly side effect.

## Config shape

```yaml
composio:
  enabled: true
  required_toolkits:
    - name: gmail
      agents: [orchestrator]      # optional; default = all non-retired
    - name: slack
    - name: github
  required_aliases: []
```

## What “healthy” means

| Status | Band impact |
| --- | --- |
| Active (connected, usable) | OK |
| Missing (no account for toolkit) | Availability −15 (cap −30 across toolkits) |
| Expired / needsAuth / reconnect | Availability −15 + Config hygiene −5 |
| Wrong alias / unexpected account only | Config hygiene −5 (warn unless policy says otherwise) |

Partial credit: if list API itself is unreachable, −10 Availability and open `apply composio-status-unreachable` — don’t mark every toolkit failed.

## Workflow (pulse)

1. Read `composio.required_toolkits` from config.
2. For each toolkit, list connections (read-only).
3. Map statuses → flags on each scoped agent.
4. Emit proposals: `apply composio-reconnect-gmail`, etc., with evidence (status string, account id **not** secrets).
5. Write flags into `scores-latest.json` (`flags: ["composio:gmail needsAuth"]`).

## Daily/weekly narrative

- Toolkits-by-status table.
- Age open reconnect proposals (&gt;7d → Improve posture hit).
- Never paste OAuth URLs into the scores file.

## Anti-patterns

- Calling `add` in a cron to “keep fresh” (auth-link spam / duplicate accounts).
- Treating Composio as optional when skills hard-depend on those apps.
- Storing Composio API keys in skill markdown.
