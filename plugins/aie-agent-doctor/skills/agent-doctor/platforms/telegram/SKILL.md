---
name: agent-doctor-telegram
description: Telegram platform module for Agent Doctor. BotFather tokens, allowlists, long-poll vs webhook, and activation via dedicated gateway. Trigger on "telegram doctor," "telegram bot," or when agent-doctor scopes Telegram.
---

# Agent Doctor — Telegram

## Setup checklist (human-owned secrets)

- Bot token from BotFather → store in vault; reference via secrets manager env map (never commit tokens).
- `ALLOWED_USERS` / home channel IDs are numeric — config locally, not in public skills.
- Default transport: long polling unless webhook URL/port is deliberately set.

## Activation reality

Enabling `platforms.telegram.enabled: true` in a profile often **does nothing** until a gateway serving that profile reloads.

Options:

1. Human names a **one-time shared gateway restart** (explicit override), or
2. Dedicated launchd/systemd: `hermes -p <profile> gateway run` **without** `--replace`, throttled — verify it does not displace the shared fleet gateway.

Prefer (2) when the profile needs always-on Telegram and the fleet already depends on a shared gateway for everything else.

## Health signals

| Signal | Meaning |
| --- | --- |
| enabled true but no bot process | Availability red/yellow |
| Token missing / op resolve fail | Secrets + availability |
| Allowlist empty in production | Hygiene risk (open bot) |
| Webhook misconfigured | Availability |

## Doctor reports

If Telegram is not fully activated, **defer** interactive Telegram and ship doctor narratives via Slack outbound relay (or local files) until the bot + gateway story is named.
