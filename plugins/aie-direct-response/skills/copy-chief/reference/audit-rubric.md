# Copy-chief audit rubric

## Severity

- **Blocking:** The copy is materially deceptive, unsupported, internally contradictory, aimed at the wrong reader, or missing an intelligible offer or action. It is not publish-ready.
- **Major:** A reachable reader is likely to lose interest, misunderstand the offer, reject a central claim, or encounter material friction.
- **Moderate:** The weakness reduces force or clarity but does not break the argument.
- **Polish:** A defensible optional improvement. Never present taste as a defect.

## Scoring

Score each category from 0 to 5 and show one sentence of evidence. Calculate each contribution as `(category score / 5) × weight` and sum the contributions to 100. Mark a category `N/A` only when its required input is genuinely absent, name the missing input, and redistribute that category's weight proportionally across the scored categories. Never use `N/A` to conceal a defect, unresolved release gate, or relevant unknown that should be scored or classified by severity.

| Category | Weight | A-level evidence |
| --- | ---: | --- |
| Audience and awareness fit | 10 | The message meets a specific reader where they are and does not explain what they already know. |
| Big Idea and Rule of One | 15 | One useful, interesting, credible idea organizes the whole piece; one clear action wins. |
| Promise and offer | 15 | The desired outcome, deliverables, terms, price, risk, and next step are easy to understand. |
| Proof and credibility | 15 | Every material claim has proportionate, attributable support; sources and limitations are visible. |
| Lead and argument | 10 | The opening earns attention and the argument advances without logical gaps or premature pitching. |
| CUB and specificity | 10 | No material passage is confusing, unbelievable, or boring; concrete detail earns its space. |
| Objections and risk | 10 | The copy addresses the real reasons not to act without caricaturing or pressuring the reader. |
| Voice and reader respect | 5 | It sounds recognizably like the supplied voice and treats the reader as an autonomous adult. |
| Compliance, accessibility, and net impression | 10 | Claims, endorsements, scarcity, pricing, guarantees, disclosures, essential information, and actions survive the relevant legal and access checks. |

Bands: 90–100 A; 80–89 B; 70–79 C; below 70 not ready. While any Blocking issue is open, report `min(uncapped score, 69)` and label the asset `NOT PUBLISHABLE`. While no Blocking issue remains but any Major issue remains, report `min(uncapped score, 89)` and label it `NOT PERFORMANCE-READY`. Missing specialist review for a regulated claim is Blocking regardless of the numerical total. Show both the uncapped arithmetic and reported capped score when a cap applies. Do not inflate the score to be encouraging.

## Big Idea test

Write the idea as one plain sentence, then test:

1. Is it important to the specific reader now?
2. Is it a single belief or discovery rather than a bundle of benefits?
3. Is the angle fresh relative to what this audience has already heard?
4. Does the product have a credible role in resolving it?
5. Can the claim be supported at the strength implied?
6. Does the rest of the piece express and advance the same idea?

Label the result `strong`, `promising but under-supported`, `familiar`, `fragmented`, or `misaligned`. Explain why.

## Four-Legged Stool

Assess each leg independently:

1. **Big or unifying idea** — the organizing concept.
2. **Promise of benefit** — the meaningful change offered to the reader.
3. **Proof** — support for every express and reasonably implied material claim.
4. **Credibility** — reasons to trust the product, spokesperson, and company.

Do not count repeated assertions as proof. Do not count fame, production value, or confidence as credibility by themselves.

## CUB annotations

Use compact tags tied to exact copy:

- `[C]` What could a reasonable reader interpret in more than one way? Name the ambiguity.
- `[U]` What claim outruns the available proof, prior belief, or internal logic? Name the proof gap.
- `[B]` What repeats known material, delays payoff, or lacks consequence? State whether to cut, compress, or replace.

A sentence may receive more than one tag. Avoid line-editing the entire draft before resolving structural failures.

Example: `[U] “Guaranteed to double revenue in 30 days.” Reader consequence: the absolute result outruns the supplied two-customer anecdote. Repair: provide representative controlled evidence, narrow the claim to what the data supports, or remove it.`

Example ledger row:

| Claim | Type | Source / evidence owner | Status | Support ceiling | Safe wording | Date / population / denominator | Typicality | Testimonial-use fields | Synthetic-media status / subject permission / disclosure | Disclosure | Approval owner | Release blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| “Teams cut weekly reporting time by 31%” | performance | 2026 customer study / analytics lead | qualified | association in 42 active teams over 8 weeks | “In a study of 42 active teams, median weekly reporting time was 31% lower after eight weeks” | 2026 / active teams / n=42 | cohort only | n/a | not used | study scope beside claim | analytics + legal | verify selection method |

## Output shapes

For a quick or vague critique, return only: reviewed asset ID and exact version; writer-supplied status or statuses—including separate copy and send status when supplied—owner, open blockers, and any attached sender-preflight receipt identity; verdict/readiness and version coverage; likely reader takeaway; material assumptions; up to five issues ordered by likely response impact; and the single next revision. Do not imply numerical precision. Apply `NOT PUBLISHABLE`, `NOT PERFORMANCE-READY`, and specialist-review labels whenever their conditions exist even without a numerical score.

For a requested formal audit, return:

1. **Verdict:** asset ID, exact version, writer-supplied status or statuses, owner, blockers, and attached preflight-receipt identity; intended message versus likely reader takeaway; review readiness, score, and exact-version coverage.
2. **Top priorities:** no more than five, ordered by likely response impact.
3. **Structural audit:** Rule of One, Big Idea, Four-Legged Stool, offer, objections, CTA.
4. **CUB markup:** exact excerpts, tags, reader consequence, repair.
5. **Claim and compliance ledger:** claim, evidence status, testimonial-use status, synthetic-media provenance/subject permission/disclosure where relevant, other disclosure or verification need, approval owner, and release blocker.
6. **Voice notes:** what to preserve, what drifts, and one calibration example.
7. **Revision plan:** sequential edits with acceptance criteria.
8. **Test plan:** primary metric, guardrails, and one or two hypotheses tied to the top priorities; include the full experiment validity fields when judging a winner.
9. **Optional rewrite:** only if requested, or a short sample when needed to make the coaching concrete.

End with the single next revision the writer should make first. Every verdict applies only to the exact reviewed version and expires after any material copy, offer, evidence, disclosure, format, or production change; state that re-review requirement in quick and formal outputs.

## Connected-suite output

For a connected campaign, do not blend the review into one generic verdict. In addition to the applicable quick or formal shape:

1. list every asset ID, medium, exact version, writer-supplied status or statuses—including separate copy and send status when supplied—owner, open blocker, and attached preflight-receipt identity;
2. apply every relevant format gate and give a separate readiness verdict, severity list, and review status for each asset/version;
3. give a cross-asset consistency verdict for claim wording and support ceiling, proof and disclosure placement, synthetic-media status, voice, offer terms, CTA, deadline/timezone, eligibility, and destination behavior; any unresolved material mismatch makes every affected version `NOT PUBLISHABLE` until corrected and re-reviewed;
4. state which exact versions the verdict covers and require re-review after any material copy, offer, evidence, disclosure, or production change.

Writer tokens map as follows: `DRAFT — NOT FOR RELEASE` and `DRAFT — DO NOT SEND` remain `NOT PUBLISHABLE` until their blockers close. `COPY-READY` together with `DRAFT — DO NOT SEND` becomes `NOT PUBLISHABLE — OPERATIONAL SEND GATE OPEN`; this preserves the copy verdict and asserts no copy defect. `NOT PERFORMANCE-READY` means no Blocking defect was found but at least one Major response defect remains; it never means send-ready or production-ready. Preserve the preflight receipt identity in the audit trail. A copy-chief verdict does not authorize release.
