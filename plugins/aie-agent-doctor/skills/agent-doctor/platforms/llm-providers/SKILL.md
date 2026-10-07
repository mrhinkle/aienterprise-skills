---
name: agent-doctor-llm-providers
description: OpenRouter and Codex (and similar) module for Agent Doctor. Primary/fallback rungs, quota 429s, optional local-model sizing by RAM/VRAM tier, cheap-tier overrides for frequent jobs. Trigger on "openrouter doctor," "codex quota," "model fallbacks," or when agent-doctor scopes LLM providers.
---

# Agent Doctor — LLM providers (OpenRouter / Codex)

## Two-rung fallbacks

When policy requires it, each agent should have a clear primary plus **two** fallback rungs (provider + model id). One-rung setups score a Config hygiene hit.

```yaml
model:
  provider: <primary-provider>
  default: <primary-id>
fallback_providers:
  - provider: openrouter
    model: <mid-id>
  - provider: openrouter
    model: <flash-id>
```

## Quota hygiene

- Sustained **429** clusters → Model/quota deduction; propose job-level cheap overrides for high-frequency crons.
- Hourly doctor pulse should be **no-LLM** so it does not worsen provider pressure.
- Pooling extra API keys is a separate named apply — only after secrets resolution is stable (1Password / Bitwarden).

## Context utilization

From fleet-observability practice: treat `(input_tokens / model_context_limit) × 100` as a Model/quota sub-signal.

| Utilization | Band hint |
| --- | --- |
| &lt; 80% | OK |
| ≥ 80% | Yellow (−5) |
| ≥ 95% | Red (−15); propose compaction / smaller context jobs |

Maintain a small model→context-limit registry in config or adapter.

## Local models (optional — cloud-agnostic tiers)

Local inference is optional offline capacity, not a whole agent unless you truly need it. Size by **available RAM/VRAM for weights + KV**, leaving headroom for the orchestrator and containers:

| Tier (approx free for model) | Everyday meat | Avoid as always-on |
| --- | --- | --- |
| Small (≤~10 GB) | ~7–9B instruct 4-bit | 30B+, large MoE |
| Mid (~10–24 GB) | ~9–14B instruct 4-bit / QAT | Q8 of 12B+ beside full stack |
| Large (24 GB+) | Mid above, or on-demand ~27B 4-bit alone short context | Multiple large residents |

Skip retired/banned coder quants on the house ban list. Prefer cloud mid-tier fallbacks for reliability.

## Health signals

| Signal | Action |
| --- | --- |
| Primary failing, fallbacks healthy | Yellow; note dependency |
| Banned local still in chain | −20 hygiene; propose drop/replace |
| Keys unresolved | Secrets module (1Password / Bitwarden) |
| Context util ≥80% sustained | Model/quota flag + proposal |
