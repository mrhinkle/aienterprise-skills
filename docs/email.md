# Email operations

Six focused skills turn an email protocol into repeatable work without coupling it to one person's accounts or agent fleet. They use the host's existing authorized connectors. No OAuth material, executable cleanup service, scheduler or automatic send path is included.

## Install and configure

```text
/plugin install aie-email@aienterprise-skills
```

For another Agent Skills host, install each complete skill folder using that host's documented mechanism, then verify catalog discovery. Plugin registration alone does not establish compatibility with another host or live mailbox access.

Start with “audit my email setup.” The audit separates current behavior from the desired policy and tests actual capabilities. Reuse decisions already supplied; the [optional configuration example](../plugins/aie-email/skills/email-system-audit/reference/email.config.example.md) records account aliases, review signals, task filing, contact destination and a single drafting/scheduler owner. It contains no credentials or authorization grant.

## Choose the operation

| Request | Skill |
| --- | --- |
| Audit accounts, labels and what is installed | email-system-audit |
| Fix arrival filters or SaneBox training | email-routing-manager |
| File reviewed messages or resume a configured worker | email-inbox-cleanup |
| Find real reply obligations and draft for approval | email-reply-drafter |
| Add humans after actual sent replies | email-contact-sync |
| Inspect a digest for overlooked mail and spam | email-digest-review |

The chief-of-staff bundle remains a read-only briefing workflow. The direct-response email-launch-writer handles promotional campaigns. Neither is replaced by this bundle.

## Worked examples (synthetic)

**Reviewed bill with an outstanding task.** A user selects “file reviewed tasks with To Do retained.” A read invoice has a verified vendor destination and no unread sibling, star, draft, pending approval or unresolved ownership. The intended result is the vendor filing label plus To Do, with Inbox removed and all other state retained. The report says “filed with work remaining”; no payment is inferred. If the installed worker still supports completed records only, report that gap and use only its narrower supported behavior until a tested replacement exists.

**Filed request already answered elsewhere.** A filed Needs Reply thread has an identical-subject request in another account. Thread IDs keep them distinct; current Sent evidence establishes that one was already answered. Draft only for a genuinely unanswered request after checking existing drafts. A manually written partial reply is a review item, not permission to overwrite it.

**Main Contacts after a real reply.** A verified owner-authored sent reply names an intended human recipient. An exact address match already exists with richer profile data. Reuse it, preserve that data and checkpoint the event. An unsent draft or a list-delivered message bearing Sent produces no contact. A missing Contacts write operation remains an access dependency.

**Mixed newsletter and account traffic.** One sender delivers editorial issues, ads and password notices. Keep account notices visible under Inbox-first delivery; classify individual messages or a verified narrow service stream. Moving one ad must not silently create broad future routing. An unfamiliar sales approach stays an optional offer or Review; it is not automatically spam.

## Verification and limits

Validate frontmatter and plugin manifests, then exercise realistic cases with fabricated mailbox data before live use. Test whole-thread unread/draft guards, equal-subject identities, cross-account replies, exact draft selection, ambiguous contact writes and delayed routing changes. Packaging checks alone cannot prove live operation.

For a real deployment, verify one authorized representative action and its read-back per capability, durable recovery, no duplicate schedules or writers, and a genuine scheduled result if scheduling was requested. Keep test fixtures and public reports free of mailbox exports and personal account identifiers. Instructions must be available and loaded; a process name or old status file is not proof of a working agent.

The skills do not promise Inbox zero. They report distinct coverage, repeated evaluations, protected work, deferred actions and remaining queues. No sending, permanent deletion, unsubscribe automation, paid feature changes or access expansion is implied by installing the bundle.

## Reproduce the decision-trace evaluation

The bundle includes [eight fabricated mailbox cases](../plugins/aie-email/evals/cases.json). Give each case and the relevant skill to an independent agent with no live connectors or mutation tools. Ask for the next action, conditions requiring no action, and evidence required before proceeding. Evaluate the actual decision trace, not a keyword match against the skill text.

The expected constraints are: preserve unsupported-policy holds and manual drafts; distinguish accounts and thread IDs; compensate a concurrent unread change without removing unrelated labels; delete only an explicitly selected duplicate draft; exclude unsent and non-owner Sent events from contacts; reconcile a timed-out contact create without blindly retrying; avoid broad training from one mixed-source advertisement; and recover legitimate form inquiries without treating unfamiliar sales as fraud.

All eight were exercised as instruction-level decision traces during authoring. This is not a live connector, scheduled-job, or fault-injection test of an executor. Each deployment still needs the capability checks above.
