# Agent health score rubric

Score each agent **0–100**. Fleet score = average of included agents (respect `exclude_from_fleet_avg`).

## Bands

| Band | Range | Meaning |
| --- | --- | --- |
| Green | 90–100 | Healthy; only polish left |
| Yellow | 70–89 | Degraded; schedule fixes |
| Orange | 40–69 | Impaired; prioritize |
| Red | 0–39 | Broken or unsafe; stop the line |

## Pillars (weights sum to 100)

| Pillar | Weight | Good means |
| --- | --- | --- |
| **Availability** | 25 | Process/gateway up; profile reachable; expected check-in/rollcall not rejected; messaging ACP/bot up if required |
| **Job reliability** | 25 | Last-24h cron/job success; no stuck runs; triage monitors themselves healthy |
| **Model / quota** | 20 | Primary reachable; fallbacks only when needed; no sustained 429 storms; provider keys resolving |
| **Config hygiene** | 15 | No banned/broken local fallbacks; two-rung fallbacks where policy requires; secrets cache TTL sane; no host-messaging ban violations |
| **Improve posture** | 15 | Open doctor proposals aged &lt;7 days; no silent drift vs last known-good backup; doctor pulse not stale |

## Default deductions (tune in `doctor.config.md`)

Start at **100**, subtract (floor at 0):

| Signal | Typical deduction |
| --- | --- |
| Failed job in last 24h (each, cap) | −15 (cap −30) |
| Check-in / rollcall rejected | −15 |
| Sustained provider 429 cluster | −10 |
| Banned or retired local model still in path | −20 |
| Expected 2-rung fallbacks, only 1 present | −10 |
| Shared-gateway messaging ban violated | −20 |
| Monitor artifact invalid / unreadable | −10 |
| Pulse stale (&gt;2× cadence) | −5 |
| Cron/job paused unexpectedly (each) | −5 (cap −15) |
| Proposal open &gt;7 days with no human decision | −5 |

Partial credit: if a yellow monitor exists but the underlying system is fine (e.g. bad JSON in an otherwise OK rollcall), prefer −5 to −10 and explain.

## Output schema (`scores-latest.json`)

```json
{
  "scored_at": "ISO-8601 with offset",
  "timezone": "America/New_York",
  "fleet_score": 95.7,
  "fleet_band": "green",
  "agents": [
    {
      "id": "example-agent",
      "score": 90,
      "band": "green",
      "pillars": {
        "availability": 25,
        "job_reliability": 25,
        "model_quota": 20,
        "config_hygiene": 10,
        "improve_posture": 10
      },
      "flags": ["1-rung fallback (2 expected)"],
      "excluded_from_fleet_avg": false
    }
  ],
  "proposals": [
    {
      "key": "two-rung-example",
      "agents": ["example-agent"],
      "summary": "Add second fallback rung",
      "apply_phrase": "apply two-rung-example"
    }
  ]
}
```

## Reporting

- Hourly pulse: write the JSON; optional one-line channel summary via **outbound relay only**.
- Daily/weekly: narrative atop the latest scores; link proposals by key.
