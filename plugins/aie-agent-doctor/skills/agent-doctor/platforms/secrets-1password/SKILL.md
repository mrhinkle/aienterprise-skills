---
name: agent-doctor-secrets-1password
description: 1Password / secrets-manager module for Agent Doctor. Cache TTL, env refs, restart thrash, and never-plaintext rules. Trigger on "1password doctor," "op cache," "secrets thrash," or when agent-doctor scopes secrets.
---

# Agent Doctor — Secrets (1Password)

## Rules

- Skills and public repos: **refs only** (`op://…` or env names), never secret values.
- Doctor proposals may name the *ref key*, not the credential.
- Prefer a single helper binary/path shared by profiles (document in `doctor.config.md`).

## Cache TTL

Short TTLs (e.g. 300s) plus crash-looping ACP/gateway jobs = keychain / `op` storms.

- Root/default: longer TTL under rate limits (e.g. **3600**).
- New profiles: do **not** copy a legacy 300 override by accident.
- Score Improve posture / Config hygiene when overrides fight the fleet default.

## Health signals

| Signal | Pillar |
| --- | --- |
| Resolve failures in logs | Availability + secrets |
| Restart loop causing repeated unlock prompts | Job reliability + secrets |
| Plaintext token in config | Config hygiene critical |
| Profile missing needed env ref | Availability |

## Applies

Changing TTL or adding env refs is a named patch key with backup. Never "test" by printing secrets into chat.
