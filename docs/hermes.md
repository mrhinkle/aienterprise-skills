# Hermes operations bundle

The `aie-hermes` plugin contains one skill for keeping a remotely accessed Hermes agent host available, secure, and maintainable without turning routine automation into a new outage risk.

## Install

```text
/plugin marketplace add mrhinkle/aienterprise-skills
/plugin install aie-hermes@aienterprise-skills
```

## aie-hermes-ha

Use it when you want to create or operate recurring monitoring for:

- Host uptime, networking, DNS, disk, memory pressure, and load.
- Tailscale authentication, control connection, and tailnet reachability.
- Hermes core plus Telegram and Slack adapters.
- Daily security posture and update readiness.
- One-attempt, user-level service recovery with verification.

Example:

> Keep this Hermes machine highly available remotely through Tailscale, Telegram, and Slack. Check it every 30 minutes, review security and updates daily, and do not reboot or change credentials without asking me.

With no configuration, the skill uses that same conservative 30-minute/daily split, does not send probe messages, and requires approval for privileged or access-affecting work.

For a stable host, copy `plugins/aie-hermes/skills/aie-hermes-ha/reference/hermes-ha.config.example.md` to `hermes-ha.config.md` in the working directory and replace only the service identifiers and policy values you have verified. Never place credentials in the config file.

## Safety model

The skill discovers the real service manager and Hermes installation before acting. It may restart a confirmed failed user-level Hermes service once, then verifies recovery. It will not automatically reboot, rotate credentials, change Tailscale ACLs or routes, weaken security controls, delete logs or data, or apply an update whose compatibility and rollback are uncertain.
