# Agent Doctor — signal adapters

Pulse remains **no-LLM**. Adapters only **read** signals and map them into pillar inputs.

## Interface (conceptual)

```text
list_agents(config) -> [agent_id]
read_signals(agent_id, config) -> {
  availability: [...flags],
  job_reliability: [...],
  model_quota: [...],
  config_hygiene: [...],
  improve_posture: [...],
  quality?: [...]
}
```

Ordered `adapters[]` in doctor.config; later adapters merge flags (union). Scorer applies deductions from `reference/rubric.md` + config overrides.

## Bundled adapters

| type | Reads | Writes |
| --- | --- | --- |
| `file-monitors` | Local JSON/artifacts | nothing |
| `otel-genai` | Prometheus/OTel metrics (`gen_ai.*`) | nothing |
| `langfuse` | Langfuse API / OTLP-backed project | nothing |
| `helicone` | Proxy cost/latency/429 | nothing |
| `github-actions` | Workflow run conclusions | nothing |
| `crewai-health` | CrewAI health/automation metrics | nothing |
| `composio-connections` | Composio connection **list** only | nothing |
| `secrets-vault` | 1Password and/or Bitwarden status + required item reachability | nothing |

## Safety

- No adapter may print secret values.
- `composio-connections` must not call `add`/`remove`.
- `secrets-vault` must not unlock without a named human apply.
