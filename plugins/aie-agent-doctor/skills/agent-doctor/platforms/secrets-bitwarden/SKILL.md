---
name: agent-doctor-secrets-bitwarden
description: Bitwarden / secrets-vault module for Agent Doctor. Vault unlock and auth status, required item reachability, and never-plaintext rules — parallel to 1Password. Trigger on "bitwarden doctor," "bw status," "vault locked," or when agent-doctor scopes Bitwarden.
---

# Agent Doctor — Secrets (Bitwarden)

Parallel to the 1Password module: treat the vault as infrastructure. **Unauthorized or locked when the fleet expects Unlocked** is an Availability failure.

## Rules

- Skills and public repos: **refs / item ids / field names only** — never secret values.
- Doctor proposals may name the item id or name, not the credential.
- Prefer a single documented CLI/API path in `doctor.config.md`.

## Auth / unlock posture

| Status | Meaning | Score |
| --- | --- | --- |
| Unauthenticated | No session | Availability −20; propose `apply bitwarden-login` |
| Locked | Session exists, vault locked | Availability −15; propose `apply bitwarden-unlock` (human-owned) |
| Unlocked | Ready | OK |
| Unexpected logout mid-window | Job reliability + secrets | −10 + proposal |

Doctor **must not** unlock with a password/PIN in automation unless a human named an apply that explicitly authorizes a documented unlock helper. Prefer interactive human unlock.

## Required items

```yaml
secrets:
  provider: bitwarden   # or: onepassword | bitwarden | both
  bitwarden:
    status_command: "bw status"   # example; site-local
    required_items:
      - id_or_name: "agent-openrouter"
        agents: [orchestrator, worker-a]
      - id_or_name: "agent-slack-bot"
```

Pulse checks **reachability** (item exists / accessible) without printing field values. Missing item → Config hygiene −10–15; unresolved ref used by a live agent → Availability −10.

## Health signals

| Signal | Pillar |
| --- | --- |
| Unauthenticated / Locked in expected window | Availability |
| Required item missing | Config hygiene |
| Plaintext token in agent config | Config hygiene critical (−20+) |
| Unlock thrash / repeated prompts | Job reliability + secrets |
| Pulse cannot run status command | Availability −10 |

## Dual-provider fleets

If both 1Password and Bitwarden are in play, declare `secrets.provider: both` and required items per provider. Score each independently.

## Applies

Named patch keys only. Never print secrets into chat or `scores-latest.json`.
