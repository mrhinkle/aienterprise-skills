# Hermes HA configuration example

Copy this file to `hermes-ha.config.md` in the working directory and replace the placeholders. Do not put tokens, passwords, signing secrets, or private message content in it.

```yaml
host:
  operating_system: discover
  maintenance_window: "Sunday 02:00-04:00 local time"

schedule:
  fast_interval_minutes: 30
  deep_interval_hours: 24

services:
  hermes_core: discover
  telegram_adapter: discover
  slack_adapter: discover
  tailscale: discover

thresholds:
  disk_warning_percent_free: 20
  disk_critical_percent_free: 10
  consecutive_failures_before_escalation: 2

health_probes:
  telegram_destination: none
  slack_destination: none

repairs:
  restart_confirmed_user_services_once: true
  restart_tailscale: false
  apply_low_risk_patch_updates: false

state:
  path: discover-safe-local-state-path
  retain_message_content: false
  retain_credentials: false
```

Use exact service identifiers only after verifying them on the target host. Keep health destinations set to `none` unless they were created specifically for automated probes.
