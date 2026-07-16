# Availability checklist

Use this checklist for the fast monitoring path. Adapt commands to the discovered operating system and installation; do not assume labels or paths.

## Host

- Confirm the host is awake and has not entered an unexpected sleep/reboot loop.
- Confirm network routing and DNS work without relying on only one public endpoint.
- Check disk space on the Hermes data, log, and system volumes.
  - Warn at 20% free or 20 GiB free, whichever is reached first.
  - Mark critical at 10% free or 10 GiB free, whichever is reached first.
- Check memory pressure and swap growth. Prefer the OS pressure signal over a raw free-memory percentage.
- Compare load with available CPU cores and recent history. Sustained load matters more than a single spike.
- Confirm time synchronization; large clock drift can break Tailscale and API authentication.

Never delete files automatically to recover disk space. Identify the largest safe candidates and request approval.

## Tailscale

- Locate the installed CLI/app and service before checking it.
- Prefer structured status output when supported.
- Confirm the local node is authenticated, connected to the control plane, and has a usable tailnet address.
- Check recent daemon logs for repeated disconnects, key expiry, DNS failures, route conflicts, or update failures.
- Verify only the minimum critical peer information needed. Do not print the full peer inventory or keys.
- Treat a healthy daemon with an unusable route as degraded, not healthy.

Do not change ACLs, DNS, routes, exit-node settings, key expiry, or account settings. Restart Tailscale only if it is clearly local, safe, and not the sole working access path.

## Hermes core

- Discover the actual service definition from `launchd`, `systemd`, the container runtime, or the documented Hermes launcher.
- Confirm desired state, current state, PID, start time, restart count, and recent exit status.
- Inspect recent logs for crash loops, deadlocks/timeouts, dependency errors, storage failures, and configuration parse errors.
- Use a documented local health endpoint if one exists. Do not invent or expose a new network listener for monitoring.
- Flag a service that repeatedly restarts even if it happens to be running at check time.

## Telegram adapter

- Confirm the configured Hermes Telegram worker is running.
- Determine whether it uses long polling or webhooks and validate the matching path.
- Look for authentication failures, webhook delivery errors, polling conflicts, DNS/TLS failures, rate limits, and repeated reconnects.
- Do not call a polling API in a way that competes with the production worker.
- Do not send a message unless a private health-check chat is explicitly configured.

## Slack adapter

- Confirm the configured Hermes Slack worker is running.
- Determine whether it uses Socket Mode or an events endpoint and validate the matching connection.
- Look for invalid-auth responses, missing scopes, rate limits, WebSocket churn, signature failures, and unacknowledged event retries.
- Do not change app scopes, reinstall the app, rotate tokens, or post a message without explicit approval or a configured health channel.

## Recovery decision table

| Condition | Automatic action | Stop condition |
| --- | --- | --- |
| Confirmed stopped user-level Hermes service | Restart once through its existing service manager, then verify | Second failure or unclear service ownership |
| Adapter wedged with clear local process failure | Restart only that adapter once, then verify logs and connection | Authentication, configuration, or repeated failure |
| Tailscale local component failed | Restart only if another access path is working or the risk is otherwise explicitly accepted | Sole access path, ACL/routing issue, or key expiry |
| Disk critically low | Alert with evidence and likely safe candidates | Never delete automatically |
| Credential or scope failure | Alert and name the credential/permission class without revealing values | Never rotate or broaden access automatically |
| Update required | Add to maintenance backlog | Do not upgrade in the fast loop |

Track consecutive failures by component. Escalate repeated failures instead of creating a restart loop.
