---
name: agent-doctor-llm-providers
description: OpenRouter and Codex (and similar) module for Agent Doctor. Primary/fallback rungs, quota 429s, local-model sizing, and cheap-tier overrides for frequent jobs. Trigger on "openrouter doctor," "codex quota," "model fallbacks," or when agent-doctor scopes LLM providers.
---

# Agent Doctor — LLM providers (OpenRouter / Codex)

## Two-rung fallbacks

When policy requires it, each profile should have a clear primary plus **two** fallback rungs (provider + model id). One-rung setups score a Config hygiene hit.

Example shape (illustrative ids only):

```yaml
model:
  provider: openai-codex
  default: <primary-id>
fallback_providers:
  - provider: openrouter
    model: <cheap-or-mid-id>
  - provider: openrouter
    model: <flash-id>
```

## Quota hygiene

- Sustained **429** clusters → Model/quota deduction; propose job-level cheap overrides for high-frequency crons.
- Hourly doctor pulse should be **no-LLM** so it does not worsen Codex/OpenRouter pressure.
- Pooling extra API keys is a separate named apply — only after secrets resolution is stable.

## Local models (optional meat)

On a **24 GB** unified-memory Mac-class host, everyday local "meat" is roughly:

- **Default:** ~7–9B instruct at 4-bit (≈5–9 GB with modest context)
- **Alt:** ~12B instruct Q4/QAT
- **On-demand only:** ~27B Q4 alone, short context — never beside a full Docker/agent stack

Skip oversized MoEs, Q8 of mid-size models, and retired coder quants banned by house policy. Prefer cloud fallbacks (e.g. OpenRouter mid-tier) for reliability; local is optional offline narration, not a whole agent unless you truly need it.

## Health signals

| Signal | Action |
| --- | --- |
| Primary failing, fallbacks healthy | Yellow; note dependency |
| Banned local still in chain | −20 hygiene; propose drop/replace |
| Keys unresolved | See secrets module |
| Everyday decisions on wrong local | Propose install+swap as named apply |
