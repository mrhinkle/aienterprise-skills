# Google Contacts adapter notes

Gmail and People API access are separate capabilities. Verify the chosen account's authorized contact-create/update operation rather than inferring it from Gmail or contacts-list access.

The People API supports contact creation and updates. Its contact search is prefix-based and cached; refresh and examine exact returned email addresses, or use a complete relevant contacts listing before concluding no match exists. Incremental sync can lag writes and is not a read-after-write check. Verify the returned contact resource directly and confirm the intended collection. [Read and manage contacts](https://developers.google.com/people/v1/contacts).

Send same-account contact mutations sequentially. Updates require current source metadata/etag and an intentional field mask; re-read on conflict and preserve fields outside the authorized change. A timeout may mean a write succeeded: reconcile before another create. [People API mutation guidance](https://developers.google.com/people/v1/contacts).

Google provides `otherContacts.copyOtherContactToMyContactsGroup` for copying one Other Contact into the user’s contacts with selected fields. Use that documented operation only if the current connector and grants support it; record the returned person and verify the destination. Do not invent a sourceType mutation or delete the source Other Contact. [Official copy operation](https://developers.google.com/people/api/rest/v1/otherContacts/copyOtherContactToMyContactsGroup). If it is unavailable, report the exact missing capability rather than silently substituting a multi-step create/delete workflow. No contact changes belong to a draft-only workflow.

Source review: October 5, 2026. These notes describe constraints, not an included connector or OAuth grant.
