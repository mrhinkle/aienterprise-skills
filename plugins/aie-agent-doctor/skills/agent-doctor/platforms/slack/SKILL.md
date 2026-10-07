---
name: agent-doctor-slack
description: Slack integrations module for Agent Doctor. Socket Mode safety, outbound cron relays, channel targets, allowlists, and shared-ingress bans — orchestrator-agnostic. Trigger on "slack doctor," "socket mode," "cron slack relay," or when agent-doctor scopes Slack.
---

# Agent Doctor — Slack

## Hard rule

**One Socket Mode (or equivalent inbound realtime) connection per Slack app.** A second connection on the same app splits events and looks randomly flaky.

If a fleet already has a gateway owning app A, doctor reports must **not** enable Slack on another process that reuses app A’s tokens.

## Preferred pattern: outbound relay

1. Keep inbound Slack **disabled** on doctor / shared-host orchestrator profiles.
2. Cron jobs deliver locally (or to a file).
3. A small relay maps `{agent, job id, target: "slack:CHANNEL_ID"}` → post via the **existing** authorized bot path (single Socket Mode owner, or a trusted outbound webhook/API).
4. Doctor never creates a second inbound socket.

## Integration contract (general)

| Check | Healthy |
| --- | --- |
| Inbound sessions per app | Exactly one |
| Doctor delivery | outbound-relay-only (default) |
| Interactive bot required | Separate Slack app + dedicated process + named override |
| Allowlists | Known user IDs in production |
| Token source | Vault ref (1Password / Bitwarden / env) — never plaintext in skills |
| Composio Slack toolkit (if used) | Active — see Composio module |

## Health signals

| Signal | Pillar |
| --- | --- |
| Relay config missing job entry | Improve posture / Job reliability |
| Target channel invalid | Availability |
| Second Socket Mode detected | Config hygiene (−20) |
| Token unresolved from vault | Secrets + Availability |
| Composio `slack` toolkit needsAuth | Availability (composio module) |

## Reporting

Doctor summaries: one line or short block to an ops channel via relay. No @channel unless severity is red and policy allows.
