---
name: agent-doctor-mission-control
description: Mission Control / ops-dashboard module for Agent Doctor. Read health from dashboards and job boards without duplicating monitors. Trigger on "mission control doctor," "ops dashboard health," or when agent-doctor scopes Mission Control.
---

# Agent Doctor — Mission Control

Treat Mission Control (or any ops dashboard that lists agents, runs, and incidents) as a **read surface**, not a second source of truth that re-runs every probe.

## What to check

- Dashboard reachable; auth via existing session/connector (no credential scraping).
- Agent cards match doctor fleet list (missing/extra agents → hygiene flag).
- Failed/stale runs already shown there should feed **Job reliability** deductions — cite the dashboard row, don't re-execute the job in the pulse.
- Alert rules that page humans should remain human-owned; doctor proposes threshold tweaks as patch keys.

## Anti-patterns

- Scraping screenshots when an API/export exists.
- Auto-acking incidents.
- Creating duplicate schedules inside Mission Control that mirror Hermes cron.

## Proposal shape

Point at the dashboard entity id + the underlying config file/cron to change. Human names `apply <key>`.
