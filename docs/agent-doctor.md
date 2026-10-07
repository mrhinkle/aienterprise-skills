# Agent Doctor bundle

Plugin: `plugins/aie-agent-doctor`

Nested skill for multi-agent fleet health: score 0–100, read monitors/adapters, propose `apply <key>` only.

## Platforms

Orchestrators (Hermes+), Slack, Telegram, Buzz ACP, Mission Control, LLM providers, **Composio**, **1Password**, **Bitwarden**, Cursor teammates, Langfuse/OTel, CrewAI/AutoGen.

## Install

```
/plugin marketplace add mrhinkle/aienterprise-skills
/plugin install aie-agent-doctor@aienterprise-skills
```

## Optional pattern

Huberman-style dedicated doctor: hourly no-LLM pulse, outbound Slack relay, propose-then-apply.
