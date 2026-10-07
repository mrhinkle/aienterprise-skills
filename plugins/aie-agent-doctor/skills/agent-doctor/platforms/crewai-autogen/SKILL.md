---
name: agent-doctor-crewai-autogen
description: CrewAI / AutoGen / LangGraph health patterns for Agent Doctor. Execution success, tool spans, handoffs, factory health endpoints. Trigger on "crewai doctor," "autogen health," "langgraph fleet," or when agent-doctor scopes those frameworks.
---

# Agent Doctor — CrewAI / AutoGen / LangGraph

## Signals

- Execution success / error rate, p95 duration, cost/tokens when emitted.
- Tool-call and handoff span failures → Job reliability.
- Lightweight `/health` for liveness; deep `/health/debug`-style probes **not** for continuous pulse (too heavy / privileged).
- AutoGen: watch conversation loop limits and repeated tool spans.
- CrewAI Platform automations: Healthy / Warning / Critical buckets as Availability inputs.

Propose framework config changes as patch keys; don’t redeploy from the doctor.
