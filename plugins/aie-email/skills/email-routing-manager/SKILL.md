---
name: email-routing-manager
description: "Organize email labels and arrival rules, including optional SaneBox training, while preserving account notifications for review. Trigger on \"fix my email routing\", \"organize email folders\", \"train SaneBox\", or \"separate newsletters from account notices\". Not a bulk cleanup or reply-writing skill."
---

# Email routing manager

Repair arrival rules and design a filing map around the owner's actual mail. Reuse existing authorization; a request to propose a label map alone is not permission to activate rules.

## Plan from live state

Verify the mailbox identity, current labels, provider filters and any third-party sorting rules. Read the owner's supplied preferences or `email.config.md` if present. Capture the exact rules and affected message IDs before changing them; separate a rule's effect on future delivery from moving historical messages.

Prefer a small structure that separates action from storage. Example filing branches are Personal/Accounts/Home, Personal/Accounts/Vehicles, Accounts/Vendors/<service>/{Billing,Updates,Support}, and Development/{GitHub,CodeRabbit,CI,Security}. Add project or vendor leaves only when actual volume makes them useful. Preserve useful existing labels and avoid renaming or deleting folders without checking their contents and dependent rules.

Under an Inbox-first policy, bills, receipts, renewals, account updates, support and development notifications arrive in Inbox even if a filing label is added. Dedicated editorial publications may use News and dedicated commercial streams Promotions when approved. Classify mixed-purpose sources by message purpose; do not use a broad domain rule that diverts account notices or catches unrelated newsletter subdomains.

## Apply within the approved scope

Inspect actual conversation context for forms, list traffic and bots. A sender's display name, List-ID or no-reply address cannot by itself distinguish a human request from automated information. Code review bot messages may arrive through a hosting service's notification address; use the underlying author and context.

Change only the conflicting rule or precise source/category. Preserve unrelated predicates and actions. When authorization covers one misfiled message from a mixed-purpose sender, correct that message with an ordinary label and leave the source rule unchanged. If a reliable narrower service/category rule cannot be verified, keep Inbox arrival and classify per message; do not substitute no-reply or List-ID heuristics. Read the rule back, check representative affected mail and verify provider reprocessing has settled before further moves. Restore wrongly diverted unseen mail without marking it read. Retain an undo record of the original rule and exact message changes.

If SaneBox is involved, read [SaneBox training and folder changes](reference/sanebox.md) first. Ordinary filing and training folders have different consequences. Do not purchase features or infer subscription entitlement from a trial banner.

For Gmail message changes, use actual account label IDs. Labels on a conversation can come from different messages; thread-wide changes affect all current messages. Prefer exact message IDs for a bounded correction and verify their full expected label sets. [Gmail label semantics](https://developers.google.com/workspace/gmail/api/guides/labels).

## Report

State rules added/changed/removed, historical messages corrected, unread state preserved, pending provider work and unresolved exceptions. A saved rule is not proof of future delivery; say whether a representative delivery has actually been observed. Leave daily cleanup to its configured executor rather than repeatedly retraining arrival rules.
