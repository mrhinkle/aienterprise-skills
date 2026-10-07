# Optional SLOs / error budgets (Agent Doctor)

Aligns the ops score with LLMOps practice. **Off by default** — enable in `doctor.config` when you have enough traffic.

| SLO | Example target | Warning | Hard floor | Feeds pillar |
| --- | --- | --- | --- | --- |
| Availability | 99.5% agent reachable | 99.0% | 98.0% | Availability |
| Job success (24h) | ≥ 95% | 90% | 80% | Job reliability |
| p95 invoke latency | ≤ org budget | +20% | +50% | Model/quota |
| Context utilization | &lt; 80% | ≥ 80% | ≥ 95% | Model/quota |
| Policy / guardrail violations | ≤ 0.2% | 0.5% | 1.0% | Config hygiene / Quality |
| Quality axes (1–5) | ≥ 4.0 p50 | &lt; 3.7 | &lt; 3.5 | Quality |

**Error budget:** when a hard floor burns for a rolling window, doctor opens a red proposal (`apply freeze-rollouts` style) — still propose-then-apply; never auto-blocks deploys unless CI gate is explicitly configured.
