# Deliverability and compliance handoff

This checklist spots issues; it does not certify legal compliance or configure the sender.

## Permission and message classification

- Identify whether the message is commercial/promotional or truly transactional; mixed content may still be commercial.
- Record consent or other applicable basis by segment and jurisdiction. U.S. CAN-SPAM, Canada's CASL, UK PECR/UK GDPR, EU rules, and local laws differ.
- Never acquire, scrape, or infer a sendable list because addresses are publicly visible.
- Suppress opt-outs, prior complaints, invalid addresses, disallowed geographies, buyers when appropriate, and anyone outside the offer's eligibility.
- Define an evidence-based engagement window using reliable clicks, purchases, replies, and other trustworthy activity; opens may be distorted. Sequence the most-engaged eligible cohort first. Exclude or separately reconfirm longer-dormant recipients where lawful; otherwise throttle and hold dormant tranches until delivery, complaint, bounce, and inbox-placement signals from the engaged cohort are acceptable. Run a documented seed/inbox-placement check before the first dormant tranche. Record the chosen window, evidence, order, thresholds, and owner.

Create a segment-level consent evidence matrix with: jurisdiction and subscriber type; message classification; address source; collection date, method, and form/version; sender/legal entity; approved channels, purposes, products, and affiliates/transfers; express, implied, or soft-opt-in conditions and expiry; withdrawal/suppression timestamp; proof artifact; and evidence owner. Unknown, conflicting, expired, or out-of-scope rows default to suppression and specialist review.

## Message requirements

- Accurate From, Reply-To, routing information, and subject.
- Clear sender identity and valid postal address where required.
- Clear, functioning unsubscribe in the message; one-click unsubscribe headers for traffic that platform rules require.
- Material affiliate, sponsor, endorsement, testimonial, price, renewal, trial, guarantee, and deadline disclosures near the associated claim.
- For any AI-generated or AI-modified face, voice, avatar, demonstration, proof image, or testimonial depiction, record provenance, permission from any implicated real person for the intended synthetic commercial use, and approved disclosure. Do not represent an invented person as a customer or a simulation as real proof. Unknown or unapproved provenance, subject permission, or disclosure forces `COPY-BLOCKED` and `DRAFT — DO NOT SEND`.
- An opt-out must not require payment, login, or unnecessary personal information.

## Sender readiness

Have the operator verify current requirements for the actual mailbox providers and volume at release time. Gmail's sender classes, thresholds, enforcement, and required controls are version-sensitive; do not rely on a number stored in this skill. Current guidance distinguishes baseline requirements from additional bulk-sender authentication, alignment, complaint, formatting, and one-click-unsubscribe requirements. Yahoo publishes similar authentication, complaint, and unsubscribe expectations.

Do not ask a copywriter to guess DNS state. Flag SPF, DKIM, DMARC, reverse DNS, TLS, aligned From domain, RFC 8058 headers, Postmaster monitoring, domain/IP reputation, list-unsubscribe behavior, gradual volume changes, and separation of promotional and transactional streams for technical verification.

Before `SEND-READY`, require a dated preflight receipt naming the actual domain, mailbox providers, expected daily volume band, promotional/transactional stream, current official requirement source, each check and result, evidence link or output, owner, and unresolved status. A receipt no older than 90 days may be reused only for the same domain, stream, provider mix, and volume band when no material configuration, reputation incident, or applicable provider-rule change has occurred. Require a fresh receipt for a new domain or stream, material volume increase, configuration change, reputation incident, applicable provider-requirement change, or dormant-segment reactivation. Unknown or failing authentication, alignment, unsubscribe, complaint/reputation, suppression, or volume-readiness status means `DRAFT — DO NOT SEND`; distinguish that operational send gate from the separate copy-status verdict.

## Regulated-category release gate

Detect health, supplement, safety, financial, investment, earnings, legal, employment, housing, credit, children, environmental, and other regulated or consequential categories. Require current category and jurisdiction review before clean copy.

- **Health/supplement:** classify disease, health, structure/function, performance, and safety implications; identify product category/regulator; verify claim substantiation ceiling, labeling consistency, contraindications/material safety, testimonial treatment, and required notification/disclaimer.
- **Financial/investment:** identify sender and speaker status, product/instrument, audience, jurisdiction, recommendation/suitability implications, performance methodology and fair balance, hypothetical/backtested status, testimonial/promoter conditions, disclosures, records, and approval.
- **Earnings/income/business opportunity:** identify the offer type and whether business-opportunity, franchise, investment, employment, gig-work, or other rules may apply. Require written substantiation, measured period, denominator across the relevant purchaser population, number and percentage achieving at least the stated result, material participant differences, costs/effort, typicality support, and treatment of atypical testimonials. A generic “results not typical” disclosure does not cure a misleading net impression. Require qualified review of disclosure-document, earnings-statement, recordkeeping, timing, and language triggers where applicable.
- **Environmental:** identify each express and implied general-benefit, carbon/emissions, offset, renewable-energy/material, recyclable, recycled-content, compostable, degradable, free-of, non-toxic, certification, or seal claim; define product/package and lifecycle scope, geography, accounting method, baseline, boundary, time period, and material limitations. Require competent support and clear qualifications; never inflate one narrow attribute into an unqualified overall environmental benefit. Require current jurisdiction review before clean copy.

Unresolved category review forces `DRAFT — DO NOT SEND` and must name the owner, claim/questions, jurisdiction, and evidence needed.

## Tracking and privacy gate

Map pixels, link rewriting, device/cohort identifiers, conversion tags, cross-site attribution, vendors, data fields, purpose, legal/consent basis, notice, retention, access, transfers, and deletion. Require current privacy-owner review for the target jurisdictions. Disable nonessential tracking when consent or another required basis is unknown; do not condition delivery or core access on unnecessary tracking.

## Deadline integrity

Verify that email, landing page, checkout, countdown, automation, and support team use the same deadline and timezone. Decide in advance how in-flight checkouts, payment failures, replies, accessibility needs, and genuine exceptions are handled. Do not quietly keep a supposedly closed offer available to exploit urgency.

## Accessibility and rendering

Before `SEND-READY`, record `pass`, `fail`, or `unverified` for semantic headings, meaningful link text, logical reading order, keyboard-operable email and destination actions, informative alt text, reflow at 320 CSS pixels, and contrast of at least 4.5:1 for normal text and 3:1 for large text. Do not place essential offer terms or the CTA only in an image. Provide a useful plain-text version and test major mobile and dark-mode renderings. A failed or unverified path to any essential claim, term, qualification, or action forces `DRAFT — DO NOT SEND`; name the owner and remediation.
