# Optional email operating preferences

Copy the decisions you actually need into an owner-controlled `email.config.md`. Keep credentials in the host's authorized connection mechanism, never in this file. Values below are illustrative preferences, not an activated workflow or permission grant.

| Decision | Example |
| --- | --- |
| Accounts and connector aliases | work = authorized-work-connection; personal = authorized-personal-connection |
| Owner identities and aliases | Explicit From identities and intentional Reply-To per account |
| Arrival | Account notifications start in Inbox; dedicated editorial sources may use News |
| Review signal | Opening or marking read counts as human review; agent inspection preserves unread |
| Reviewed open work | File with To Do retained, or keep in Inbox until complete |
| Protected states | Unread, starred, draft, pending approval, snooze, unresolved ownership/classification |
| Filing map | Existing account-specific label/folder IDs plus needed vendor/development leaves |
| Drafting owner | One named automatic writer; preserve manual drafts |
| Private-content handling | Approved local workflow or processing services and any excluded categories |
| Contacts | Main Contacts / Other Contacts / disabled; intended human reply recipients only |
| Cleanup executor | Existing documented entrypoint and tested policy version, or unavailable |
| Automation | Disabled unless requested; one scheduler owner, chosen time and IANA time zone |
| Batch limits | Executor's verified request/time/operation budget and retry policy |
| Reports and undo | Approved local journal location, result destination and retention |

Record actual capabilities separately from these preferences. Missing write access is an implementation gap; changing the configuration cannot grant it. If a prior executor supports only a subset of the chosen policy, preserve that distinction until its replacement is tested.
