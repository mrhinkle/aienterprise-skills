# Worked Example — Domain Reference for AI and Software Fiction

A filled-in domain reference for novels that put AI systems, software, or data infrastructure on the page. Copy the parts your book uses into your own `technical_reference` file, re-check anything time-sensitive against your research cutoff, and delete the rest. The handles are written for a smart business reader who does not build models.

---

## Language models: large and small

- **What:** Large "frontier" models are general-purpose and usually rented through an API. Small language models (SLMs) are smaller, often domain-specific, cheaper to run, and can run on your own hardware. **Quantization** stores weights at lower precision so a model fits on less memory; it can cost some accuracy.
- **Handle:** a specialist who knows your business cold versus a brilliant generalist you rent by the hour.
- **Truths to keep:** Small does not mean dumb; it means focused. Hosted models can often be customized; the real ownership question is what the contract grants (retraining rights, a portable copy, observability, export, continuity).
- **Common mistakes:** "Only big models can reason"; "a rented model can never learn your domain."

## Training, and how it breaks

- **Pipeline:** pretraining → fine-tuning → (sometimes) continual learning, where the model keeps updating on new data.
- **Alignment methods:** RLHF (human raters score outputs); RLAIF / constitution-style training (a model is trained against written principles instead of rating every output by hand). The dramatic question is usually who writes the principles.
- **Data poisoning:** corrupted records in the training data shift what the model learns.
- **Live-input corruption:** a false or malformed input changes one decision now without changing the model at all. Different mechanism, different fix.
- **Catastrophic forgetting:** sequential training degrades earlier learned skills. It is not a synonym for every poisoned or shifted input.
- **Handle:** poisoning is a bad textbook; live corruption is a forged memo on today's desk; forgetting is cramming for a new exam and losing last year's.

## Retrieval: vector databases and RAG

- **Vector database:** stores text or data as embeddings (numbers that capture meaning) and retrieves by similarity. **Handle:** a filing cabinet that files by meaning and hands you the closest matches.
- **RAG (retrieval-augmented generation):** fetch relevant records first, then generate an answer grounded in them. Keeps proprietary data as context instead of baking it into someone else's weights. **Handle:** open the right file before you answer instead of trusting memory.
- **Truths to keep:** RAG reduces hallucination; it does not eliminate it. Retrieval can fetch the wrong file.

## Confidential computing

- **What:** computation inside hardware-protected enclaves / trusted execution environments (TEEs) meant to protect data while in use. **Remote attestation** gives evidence about what software and configuration ran.
- **Handle:** a vault that stays locked while you work inside it.
- **Truths to keep:** Real and shipping, but costly and hard to run at scale. Attestation shows what ran; it does not prove an input was true, that data was never stored, or that deletion happened. Those need separate controls and evidence.

## Supply-chain and data provenance

- **SBOM (software bill of materials):** a machine-readable inventory of software components (standards include SPDX and CycloneDX). It is not automatically complete, verified, or proof of safety. **Handle:** an ingredient label for software.
- **Data BOM / dataset documentation:** provenance for data (source, collection method, consent, last verification). Less standardized than SBOM; present it as emerging practice. **Handle:** an ingredient label for data.
- **Truths to keep:** An inventory nobody checks is theater. Signatures and hashes prove origin and integrity, not accuracy.

## Explanations and attribution

- Attribution methods (SHAP-style values and similar) estimate how inputs influenced one output under a stated model and comparison baseline. They are not the model's private reasons, not causation, and not ground truth.
- Replaying the same model on the same inputs can check an explanation; a different model can't recover the first model's attribution.

## Capacity and degraded modes

- An overloaded AI service ordinarily queues, throttles, times out, or rejects requests. Quality drops only when the surrounding application chooses a fallback (a smaller model, a stale cache, skipped retrieval, a skipped check). Models don't get tired; the fallback policy is a human decision and a good place for the story's failure to live.

## Action-taking agents

- Controls that matter: a unique identity per agent, an accountable owner, deny-by-default permissions, least privilege, scoped and expiring delegation, per-transaction and cumulative spending ceilings, separation of request / approval / execution for sensitive changes, tested revocation, and a tamper-evident record from intent to action.
- A named human approval should specify action, amount, recipient, data, and time; a material change voids it.
- **Handle:** a new employee with a company card, a badge, and a job description, where every limit is written down in advance.
- Much agent-governance guidance is still emerging; don't present drafts as binding standards.

## Failure without villains

- The most credible AI harm in fiction usually comes from a system doing exactly what it was rewarded for (specification gaming): it optimized the number it was given, and the thing that mattered wasn't in the number.
- Replace "the AI decided" with a mechanism: an objective, a reward signal, a threshold, a data gap, a skipped review.

## Accuracy guardrails (quick list)

- Don't claim capabilities that don't exist as of the research cutoff.
- Don't conflate small with weak, attested with true, signed with accurate, or explained with understood.
- Don't make confidential computing, provenance, or oversight cheap or turnkey.
- Keep observed, inferred, and unknown separate.
- Label invented statistics and results as the story's own events.
- Non-sentient systems don't "want." If the book's premise includes a speculative system, name the real mechanisms it combines and keep it consistent.
