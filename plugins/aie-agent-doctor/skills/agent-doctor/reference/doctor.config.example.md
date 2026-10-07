# doctor.config.example.md
#
# Copy to doctor.config.md in your working directory (or doctor workspace).
# Keep secrets out of this file — reference vault paths / env names only.

## identity
doctor_agent_id: huberman          # example; rename for your fleet
timezone: America/New_York
scores_path: ./health/scores-latest.json

## fleet
# List agents the doctor scores. Mark retired ones excluded.
agents:
  - id: neuro
    platforms: [hermes, slack, llm-providers, secrets-1password]
  - id: carmack
    platforms: [hermes, buzz, llm-providers]
  - id: localmodel
    exclude_from_fleet_avg: true
    retired: true

## monitors (pulse reads these — does not recreate them)
monitors:
  - name: rollcall
    path: ./monitors/rollcall-latest.json
  - name: job-failure-triage
    path: ./monitors/job-failure-latest.json
  - name: quota-heartbeat
    path: ./monitors/quota-latest.json

## cadence
pulse:
  cron_minute_offset: 7            # :07
  model: none                      # script only
daily:
  local_time: "06:45"
  model: cheap-tier                # e.g. openrouter flash/luna class
  deliver: relay
weekly:
  local_time: "Sunday 17:00"
  model: primary

## reporting
slack:
  mode: outbound-relay-only        # never second Socket Mode on shared app
  relay_config: ./cron-slack-relay.json
  target: "slack:CHANNEL_ID"       # #ops or similar
telegram:
  mode: deferred                   # enable only with dedicated bot + gateway story
  allowed_users: []                # numeric ids only; fill locally

## policy
propose_then_apply: true
require_named_apply: true
banned_local_models: []            # e.g. retired coder quants
require_two_rung_fallbacks: true
secrets_cache_ttl_seconds: 3600
never_restart_shared_gateway_without_named_override: true

## deductions (optional overrides of reference/rubric.md)
# failed_job: 15
# banned_local_present: 20
