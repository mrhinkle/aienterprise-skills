---
name: agent-doctor-buzz
description: Buzz ACP platform module for Agent Doctor. Relays, agent keys, channels, allowlists, and wrapper/flag pitfalls. Trigger on "buzz doctor," "buzz-acp," "ACP health," or when agent-doctor scopes Buzz.
---

# Agent Doctor — Buzz ACP

Buzz connects agents through an ACP bridge (example shape: `buzz-acp` → agent CLI `acp`). Humans join via Buzz Desktop + network path to the relay (often a private mesh such as Tailscale — keep hostnames out of public docs).

## Health signals

| Signal | Pillar |
| --- | --- |
| ACP job crash-looping (exit 2 on flag parse) | Availability |
| Relay up but agent never answers | Availability / Job reliability |
| Owner-only channel vs collaborator allowlist drift | Config hygiene |
| Key missing / wrong profile | Secrets + availability |
| Restart storms thrashing vault | Secrets (see 1Password module) |

## Common failure: flag shadowing

If the ACP wrapper forwards argv poorly, flags meant for the inner agent (e.g. `-p <profile>`) get parsed by `buzz-acp` itself → immediate exit. **Fix with a shim** that never passes agent-only flags to the outer binary. Propose the shim; apply only when named.

## Collaborators

Buzz typically has **no email invite API** in-agent. Flow:

1. Human sends Desktop invite / redeem link.
2. Collaborator returns pubkey (hex/npub).
3. Add to channel allowlists; switch `--respond-to` / ACL from owner-only → allowlist.
4. Network access to the relay is a separate prerequisite (mesh invite, etc.).

## Rollout discipline

- Prove **one** agent end-to-end (ping + multi-turn) before cloning to N profiles.
- Stagger new ACP processes if each pull hits a secrets manager.
- Messaging-only agents: disable terminal/code tools in the Buzz-facing profile if policy requires.
