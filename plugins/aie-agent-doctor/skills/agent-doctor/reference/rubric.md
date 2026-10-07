# Agent health score rubric (generalized)

Score each agent **0–100**. Fleet score = average of included agents (respect `exclude_from_fleet_avg`).

## Bands

| Band | Range | Meaning |
| --- | --- | --- |
| Green | 90–100 | Healthy; only polish left |
| Yellow | 70–89 | Degraded; schedule fixes |
| Orange | 40–69 | Impaired; prioritize |
| Red | 0–39 | Broken or unsafe; stop the line |

## Pillars (default weights sum to 100)

| Pillar | Weight | Good means |
| --- | --- | --- |
| **Availability** | 25 | Process/gateway up; expected check-in not rejected; messaging ACP/bot up if required; **required Composio toolkits Active**; **vault unlocked/authorized** when expected |
| **Job reliability** | 25 | Last-24h job success; no stuck runs; triage monitors healthy |
| **Model / quota** | 20 | Primary reachable; fallbacks only when needed; no sustained 429s; context util &lt;80% |
| **Config hygiene** | 15 | No banned local fallbacks; two-rung fallbacks; secrets TTL sane; no shared-ingress messaging violations; Composio needsAuth counted |
| **Improve posture** | 15 | Open proposals aged &lt;7 days; no silent drift; doctor pulse not stale |
| **Quality** (optional) | 0 default | Goal completion / tool accuracy / grounding / plan efficiency (1–5 axes) when `quality.enabled` |

Weights are overridable in `doctor.config` (must sum to 100).

## Default deductions (tune in config)

Start at **100**, subtract (floor at 0):

| Signal | Typical deduction |
| --- | --- |
| Failed job in last 24h (each, cap) | −15 (cap −30) |
| Check-in / rollcall rejected | −15 |
| Sustained provider 429 cluster | −10 |
| Context utilization ≥80% / ≥95% | −5 / −15 |
| Banned or retired local model still in path | −20 |
| Expected 2-rung fallbacks, only 1 present | −10 |
| Shared-ingress messaging ban violated | −20 |
| Monitor artifact invalid / unreadable | −10 |
| Pulse stale (&gt;2× cadence) | −5 |
| Cron/job paused unexpectedly (each) | −5 (cap −15) |
| Proposal open &gt;7 days with no human decision | −5 |
| **Composio toolkit missing / needsAuth / expired** (each, cap) | −15 (cap −30) |
| **Vault unauthenticated (1P or Bitwarden)** | −20 |
| **Vault locked (Bitwarden) in expected window** | −15 |
| **Required vault item/ref missing** | −10–15 |

## Output schema

See `scores.schema.json`. Example timezone: `"UTC"` (override per house).
