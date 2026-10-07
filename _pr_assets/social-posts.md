# Revised social posts (generic — no Mac Mini / private host)

## X.com — single post

Open-sourcing Agent Doctor: nested skills that score multi-agent fleets 0–100 (availability, jobs, quota, hygiene, posture). Checks Composio app connections + vault auth (1Password/Bitwarden), Slack/Telegram integration contracts. Diagnose-and-propose only — applies when you name them. github.com/mrhinkle/aienterprise-skills

## X.com — thread (3)

1/ Just open-sourced Agent Doctor — a nested Agent Skill for multi-agent fleets.

Diagnose-and-propose only. Score every agent 0–100. Patch nothing until a human names `apply <key>`.

→ github.com/mrhinkle/aienterprise-skills

2/ Rubric you can fork:
• Availability 25
• Job reliability 25
• Model/quota 20
• Config hygiene 15
• Improve posture 15

Hourly pulse = no LLM. It reads monitors + connection status (Composio toolkits Active? Bitwarden/1Password unlocked?). Daily/weekly get the narrative.

3/ Platforms: orchestrators (Hermes & peers), Slack/Telegram contracts, Buzz ACP, OpenRouter/Codex, Composio, 1Password & Bitwarden, OTel/Langfuse adapters.

One usage pattern: a “Huberman-style” doctor agent — hourly pulse, ops channel via outbound Slack relay (never a second Socket Mode), propose-then-apply.

`/plugin install aie-agent-doctor@aienterprise-skills`

## LinkedIn

Most multi-agent setups fail quietly: a cron pauses, a fallback still points at a retired local model, a Composio Gmail connection slips into needsAuth, Bitwarden locks overnight, two processes fight over the same Slack Socket Mode app — and nobody notices until a human is already late.

We open-sourced **Agent Doctor** in the AIEnterprise Skills marketplace — a nested Agent Skill for Claude Code / Cowork (and the same heuristics you can run on Hermes or any orchestrator that writes monitor artifacts).

It does three things well:

1. **Scores** every agent 0–100 across availability, job reliability, model/quota pressure, config hygiene, and improvement posture.
2. **Reads** the monitors and integration status you already have for the hourly pulse (no sixth LLM watcher burning quota) — including Composio connection lists and vault unlock/auth checks for 1Password and Bitwarden.
3. **Proposes** exact patch keys — and waits. Nothing lands until a human says `apply <key>`.

Platform modules cover orchestrator runtimes, Slack & Telegram integration contracts, Buzz ACP, Mission Control, OpenRouter/Codex, Composio, secrets managers (1Password + Bitwarden), and IDE teammates. Optional adapters point at Langfuse / OpenTelemetry GenAI / Helicone / GitHub Actions. The Slack module’s hard rule matches production scars: never open a second Socket Mode connection on the same app; ship doctor reports through an outbound relay instead.

How some teams use it: a dedicated doctor agent (we nicknamed ours in the Huberman style) pulses hourly, writes `scores-latest.json`, posts daily/weekly narratives to an ops channel, and leaves shared gateways untouched unless a human names an override.

If you are running more than one agent in anger, steal the rubric — then make the doctor earn the right to change anything.

Repo: https://github.com/mrhinkle/aienterprise-skills  
Install: `/plugin install aie-agent-doctor@aienterprise-skills`
