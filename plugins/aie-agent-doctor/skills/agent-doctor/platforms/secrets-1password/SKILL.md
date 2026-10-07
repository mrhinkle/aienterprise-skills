---
name: agent-doctor-secrets-1password
description: 1Password / secrets-manager module for Agent Doctor. Cache TTL, env refs, unlock/auth posture, restart thrash, never-plaintext. Pair with secrets-bitwarden when both vaults are in use. Trigger on "1password doctor," "op cache," "secrets thrash," or when agent-doctor scopes 1Password.
---

# Agent Doctor — Secrets (1Password)

## Rules

- Skills and public repos: **refs only** (`op://…` or env names), never secret values.
- Doctor proposals may name the *ref key*, not the credential.
- Prefer a single helper binary/path shared by agents (document in `doctor.config.md`).
- If Bitwarden is also used, see `platforms/secrets-bitwarden` and set `secrets.provider: both`.

## Auth / resolve posture

| Signal | Score |
| --- | --- |
| `op` / helper cannot authenticate | Availability −20; `apply onepassword-auth` |
| Refs fail to resolve for required env | Availability −10–15 |
| Short TTL (e.g. 300s) + crash-loop = keychain storms | Job reliability + Config hygiene |
| Plaintext token in config | Config hygiene critical |

## Cache TTL

- Default under rate limits: longer TTL (e.g. **3600**).
- New agents: do **not** copy a legacy short override by accident.

## Required items (optional)

```yaml
secrets:
  provider: onepassword
  onepassword:
    required_refs:
      - env: OPENROUTER_API_KEY
        ref: "op://Vault/openrouter/api-key"
        agents: [orchestrator]
```

Pulse verifies refs are declared and resolvable without printing values.

## Applies

TTL / env-ref changes = named patch key with backup. Never print secrets into chat or scores JSON.
