---
name: email-contact-sync
description: "Add intended human recipients to the sending account's chosen contacts after verified sent replies, with deduplication and preserved contact data. Trigger on \"add people I reply to to contacts\", \"sync contacts after sent replies\", or \"promote replied-to people to main Contacts\". Excludes drafts and bulk recipient harvesting."
---

# Email contact sync

Maintain useful contacts after actual human correspondence. The owner selects main Contacts, autocomplete/Other Contacts, or no automatic saving; these are not interchangeable outcomes.

## Verify the event and capability

Use the current request and owner-provided account preferences or `email.config.md`. Confirm the sending account and the requested contact destination, plus an existing authorized read/write route. Gmail access or a contacts-list tool does not prove contact creation is available. If access is missing, identify the exact unsupported action and prepare an owner-controlled authorization step; do not inspect, copy or broaden credentials as a workaround.

Process only a verified sent reply authored by the account owner to an intended human recipient. Inspect actual authorship and reply context, not a Sent label alone. An unsent draft, forward, calendar artifact, bot/list address, tracking address or incidental CC is not an eligible event. A Reply-To alias or a cross-account copy does not move contact ownership to another account. Include additional intentional human recipients only when the selected policy explicitly covers them.

## Deduplicate before writing

Use a durable key containing sending account, sent-message ID and recipient address. Parse addresses exactly; do not strip plus tags, collapse aliases or merge people by display name. Apply only normalization the provider's documented identity rules support. Search/list the chosen account's contacts with complete coverage sufficient to establish whether that exact address exists. Do not treat a prefix search or stale cache miss as proof of absence.

Reuse a matching main contact and retain richer names, phone numbers, notes and provenance. If an appropriate Other Contacts entry exists, promote it through a supported provider operation when main Contacts was selected; verify the result in the actual main collection. Do not guess a person's name or overwrite fields from an email signature without authority.

Serialize writes per account. Record intent before creation/promotion, capture the returned resource identity, and verify it directly afterward. On timeout or ambiguous success, reconcile the exact address/resource before retrying; never create again merely because a search index is delayed. Use one bounded reconciliation pass per ambiguous event in an invocation, honoring provider backoff. If a returned resource or complete fresh account evidence cannot establish the result, leave the intent pending and report it; do not issue another create in that invocation. A later run rechecks the durable intent before proceeding. Advance the sent-event checkpoint only after a verified result or a durable explicit skip. Preserve a retry record for unresolved events.

For Google-specific implementation constraints, read [People API notes](reference/google-contacts.md). Other providers need their own verified main/autocomplete distinction and read-back behavior.

## Report

Report per account: added, reused, promoted, excluded, pending access, failed and remaining events. A successful API call is not proof the contact is in the chosen collection. Keep addresses and private profile data out of public logs; retain only the local evidence needed for reconciliation. No reply is sent by this skill, and no contact is created solely because a draft was approved.
