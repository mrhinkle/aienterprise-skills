---
name: agent-doctor-telegram
description: Telegram integrations module for Agent Doctor (orchestrator-agnostic). Bot tokens, allowlists, long-poll vs webhook, dedicated ingress vs shared gateway, rate limits. Trigger on "telegram doctor," "telegram bot," or when agent-doctor scopes Telegram.
---

# Agent Doctor — Telegram

Works with Hermes, custom gateways, or any process that owns a Bot API session. Heuristics are **integration contracts**, not host-specific paths.

## Setup checklist (human-owned secrets)

- Bot token from BotFather → vault ref (1Password, Bitwarden, or env name) — never commit tokens.
- `ALLOWED_USERS` / home chat IDs are numeric — local config only.
- Transport: **long polling** (default) or **webhook** (HTTPS URL + secret token). Mixing both on one bot = flaky receive.

## Integration contract

| Rule | Why |
| --- | --- |
| One active getUpdates/webhook consumer per bot token | Second poller steals updates |
| Allowlist required in production | Open bots get probed |
| Doctor reports prefer outbound send (or Slack relay) until inbound is proven | Don’t block doctor on half-setup Telegram |
| Dedicated ingress when shared orchestrator gateway must stay messaging-off | Same isolation pattern as Slack Socket Mode |

## Activation reality

Setting `telegram.enabled: true` in an orchestrator profile often **does nothing** until the process that polls/webhooks reloads.

Options (human names one):

1. One-time reload of the **dedicated** Telegram-owning process, or
2. Dedicated systemd/launchd/container: profile-scoped gateway **without** replacing the shared fleet gateway.

## Health signals

| Signal | Pillar | Typical deduction |
| --- | --- | --- |
| enabled but no poller/webhook process | Availability | −15 |
| Token missing / vault resolve fail | Secrets + Availability | −15 |
| Allowlist empty in production | Config hygiene | −10 |
| Two consumers on same bot token | Config hygiene | −20 |
| Webhook TLS/secret misconfigured | Availability | −10 |
| 429 / retry storm from Telegram API | Job reliability | −5–10 |

## Doctor reports

If Telegram inbound is deferred, ship narratives via Slack outbound relay or local files. Interactive Telegram is a separate named apply after bot + vault + process story exists.

## Config sketch

```yaml
telegram:
  mode: deferred | dedicated-bot | disabled
  vault_ref_env: TELEGRAM_BOT_TOKEN
  allowed_users: []
  transport: long_polling
  webhook_url_env: null
```
