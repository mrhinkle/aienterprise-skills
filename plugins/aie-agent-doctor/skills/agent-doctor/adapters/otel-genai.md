# Adapter: otel-genai

Map OpenTelemetry GenAI metrics/spans into pillars:

| Signal | Pillar |
| --- | --- |
| `gen_ai.invoke_agent.duration` p95 regression | Model/quota / Job reliability |
| Error rate on invoke/tool spans | Job reliability |
| `gen_ai.usage.input_tokens / context_limit` | Model/quota (80%/95% thresholds) |
| Missing expected agent resource | Availability |

Read-only via Prometheus, collector API, or backend of choice.
