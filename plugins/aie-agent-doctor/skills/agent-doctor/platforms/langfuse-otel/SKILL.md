---
name: agent-doctor-langfuse-otel
description: Langfuse and OpenTelemetry GenAI module for Agent Doctor. Map traces/metrics into health pillars; context utilization; optional quality scores. Trigger on "langfuse doctor," "otel genai," or when agent-doctor scopes observability.
---

# Agent Doctor — Langfuse / OpenTelemetry GenAI

Prefer **OTel GenAI semantic conventions** as the portable layer; Langfuse (or others) as a backend.

## Pulse

- Read error rates, invoke durations, token usage via adapter (`otel-genai` / `langfuse`).
- Context utilization ≥80% yellow / ≥95% red (config thresholds).
- Optional Quality pillar from Langfuse scores / LLM-as-judge — never mutate prompts/datasets in pulse.

## Anti-patterns

- Re-running prod traces as live LLM calls every hour.
- Vendor lock-in without an adapter seam.
