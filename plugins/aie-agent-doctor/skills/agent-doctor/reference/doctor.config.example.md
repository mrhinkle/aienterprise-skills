# doctor.config.example.md
#
# Copy to doctor.config.md in your working directory (or doctor workspace).
# Keep secrets out of this file — reference vault paths / env names only.
# Validate against reference/doctor.config.schema.json when using JSON form.

## identity
doctor_agent_id: fleet-doctor       # rename for your fleet
# optional nickname pattern: some teams call this a "Huberman-style" doctor
timezone: UTC
scores_path: ./health/scores-latest.json

## fleet
agents:
  - id: orchestrator
    platforms: [hermes, slack, llm-providers, secrets-1password]
  - id: worker-a
    platforms: [hermes, buzz, llm-providers]
  - id: retired-local
    exclude_from_fleet_avg: true
    retired: true

## adapters (pulse reads via these — does not recreate probes)
adapters:
  - type: file-monitors
    config:
      monitors:
        - name: rollcall
          path: ./monitors/rollcall-latest.json
        - name: job-failure-triage
          path: ./monitors/job-failure-latest.json
        - name: quota-heartbeat
          path: ./monitors/quota-latest.json
  # - type: langfuse
  #   config: { base_url: "https://cloud.langfuse.com", project: "prod" }
  # - type: otel-genai
  #   config: { prometheus_url: "http://localhost:9090" }
  # - type: helicone
  #   config: { base_url: "https://api.helicone.ai" }
  # - type: github-actions
  #   config: { repo: "org/agents", workflow: "agent-fleet.yml" }

## cadence
pulse:
  cron_minute_offset: 7            # :07 — avoid :00/:15/:30/:45 stampede
  model: none                      # script only
daily:
  local_time: "06:45"
  model: cheap-tier
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
  mode: deferred

## policy
propose_then_apply: true
require_named_apply: true
banned_local_models: []
require_two_rung_fallbacks: true
secrets_cache_ttl_seconds: 3600
never_restart_shared_gateway_without_named_override: true
context_util_yellow_pct: 80
context_util_red_pct: 95

## weights (must sum to 100; set quality>0 only when quality.enabled)
weights:
  availability: 25
  job_reliability: 25
  model_quota: 20
  config_hygiene: 15
  improve_posture: 15
  quality: 0

## quality (optional — LLM-as-judge / offline evals)
quality:
  enabled: false
  axes: [goal_completion, tool_accuracy, factual_grounding, instruction_adherence, plan_efficiency]
  target: 4.0
  hard_floor: 3.5

## composio
composio:
  enabled: true
  required_toolkits:
    - name: gmail
    - name: slack
    - name: github

## secrets
secrets:
  provider: both   # onepassword | bitwarden | both | none
  onepassword:
    required_refs: []
  bitwarden:
    status_command: "bw status"
    required_items: []
