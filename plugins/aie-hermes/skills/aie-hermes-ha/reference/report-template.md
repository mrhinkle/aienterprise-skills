# Report template

Use the compact form when healthy and the incident form for any degraded path.

## Healthy

```markdown
Hermes host: HEALTHY
Monitor: {name} — every {fast interval}; deep review every {deep interval}
Paths: Tailscale {status} · Hermes {status} · Telegram {status} · Slack {status}
Capacity: disk {status} · memory {status} · load {status}
Last deep review: {timestamp or not yet run}
Actions: none
```
## Degraded or failed

```markdown
Hermes host: {DEGRADED | FAILED} — {affected path}
Severity: {critical | high | medium | low}
Evidence: {specific, secret-safe observation}
Likely cause: {fact or clearly labeled inference}
Recovery attempted: {action or none}
Verification: {result}
Repeated failures: {count and window}
Approval needed: {exact action, risk, and rollback} or none
Next step: {one concrete action}
```

## Installation handoff

```markdown
Monitor: {name}
Scheduler: {automation tool | launchd | systemd}
Cadence: {fast} / {deep}
State: {path and content description}
Automatic repairs: {allowed list}
Approval gates: {protected actions}
Validation: {manual run result and next scheduled run}
Maintenance backlog: {updates or hardening items}
```
