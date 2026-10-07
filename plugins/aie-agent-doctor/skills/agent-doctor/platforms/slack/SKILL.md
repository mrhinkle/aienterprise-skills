---
name: agent-doctor-slack
description: Slack platform module for Agent Doctor. Socket Mode safety, outbound cron relays, channel targets, and ban patterns for shared gateways. Trigger on "slack doctor," "socket mode," "cron slack relay," or when agent-doctor scopes Slack.
---

# Agent Doctor — Slack

## Hard rule

**One Socket Mode (or equivalent inbound realtime) connection per Slack app.** A second connection on the same app splits events and looks "randomly flaky."

If a fleet already has a gateway owning app A, doctor reports must **not** enable `platforms.slack` on another host profile that reuses app A's tokens.

## Preferred pattern: outbound relay

1. Keep `platforms.slack.enabled: false` on doctor / shared-host profiles.
2. Cron jobs deliver locally (or to a file).
3. A small relay maps `{profile, job id, target: "slack:CHANNEL_ID"}` → post via the **existing** authorized bot path (e.g. docker exec into the gateway that already owns Socket Mode, or a single outbound webhook/API path you already trust).
4. Doctor never creates a second inbound socket.

## Health signals

| Signal | Pillar |
| --- | --- |
| Relay config missing job entry | Improve posture / Job reliability |
| Target channel invalid | Availability |
| Second Socket Mode detected | Config hygiene (−20 style) |
| Token unresolved from vault | Model/quota-adjacent / secrets |

## When interactive Slack *is* required

- Create a **separate Slack app** with its own bot + app-level tokens (vault refs, never plaintext in skills).
- Run a **dedicated** gateway/process for that profile.
- Human must **name** an override if this conflicts with a standing "no host Slack" ban.
- Restrict allowlists to known user IDs.

## Reporting

Doctor summaries: one line or short block to an ops channel via relay. No @channel unless severity is red and policy allows.
