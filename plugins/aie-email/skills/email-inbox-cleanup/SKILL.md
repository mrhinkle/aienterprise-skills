---
name: email-inbox-cleanup
description: "File reviewed email under an agreed protocol while preserving unread mail, drafts and outstanding work labels; run or resume an existing cleanup executor. Trigger on \"clean up my inbox\", \"file email I have read\", \"sort what is left\", or \"resume inbox cleanup\". Does not send mail or change arrival filters."
---

# Email inbox cleanup

Reduce Inbox clutter according to the owner's established review and task policy. Use already-granted scope; do not require the owner to approve the same routine filing again.

## Establish what can run

Verify the account mapping, approved review signal, destination labels, open-task policy and actual tool/executor capabilities. Use owner-provided `email.config.md` or the current conversation. Without a review signal or mutation authority, prepare a preview and ask only for the missing decision. An agent reading mail must not mark it read or count its own access as human review.

If a maintained deterministic executor exists, invoke its documented manual entrypoint with its lock, limits, checkpoints and recovery behavior. Compare its active policy with the requested one before running. When an older executor supports only a narrower subset of the authorized request, state that limitation and proceed with that safe subset; hold unsupported items and report them separately. For example, a completed-record worker leaves an unpaid To Do invoice in Inbox even when the desired future policy would file it. Do not rewrite its rules, bypass limits, reset cursors or improvise a competing worker during a run. Installation alone does not prove execution.

Without an executor, use available provider tools only for a bounded authorized batch with recoverable before-state. Do not claim that this creates a reliable recurring service. If the necessary per-message operations or verification are unavailable, produce the concrete plan and capability gap.

## Filing decisions

Read complete current conversation state before filing. Protect any unread sibling, star, draft, pending reply approval, snooze or unresolved legitimacy, classification, destination or next-step ownership. These are the bundle's conservative defaults; a deliberate owner exception must be explicit and supported by the executor. Preserve state on every message, including unrelated labels.

For confidently classified reviewed mail, follow the selected open-task policy:

- **File with task labels:** file an identified unpaid bill, known action request or failed build with To Do and applicable Needs Reply/Waiting labels retained. Add To Do only when an action remains. Ensure the agent that follows up scans filed work queues as well as Inbox.
- **Keep open work in Inbox:** file only records established as complete or informational with no outstanding action.

Neither policy treats reading, age, an automated receipt or a new label as evidence that a human task is complete. Unknown mail stays visible with Review; routine informational mail does not acquire a fabricated task.

## Execute and verify

Use stable account + conversation + message IDs. Capture before-state and required additions/removals, re-read immediately before mutation, and act only on eligible captured messages. For Gmail, archive by removing INBOX only from those messages; do not mark read, remove work labels or apply a thread-wide archive to unseen siblings. Other providers need verified equivalent semantics. [Gmail label semantics](https://developers.google.com/workspace/gmail/api/guides/labels).

Record each intended mutation before execution. Verify the full expected label/read state afterward, recheck conversation changes, and restore Inbox to exact affected IDs if a concurrent unread/draft/approval change invalidates filing. A new UNREAD state explicitly invalidates review: restore only the captured Inbox removal, retain the new UNREAD state and unrelated concurrent edits, and defer that conversation until a later human review. Do not retry filing that conversation in the same invocation. Do not blindly retry an ambiguous write: read its result, reconcile the journal, and leave unresolved recovery visible.

Use configured bounded passes, backoff and a single writer lock. Stop on quota deferral, required recovery, account failure, overlap or lack of progress. Keep durable cursors and revisit older held mail when its review state changes. If scheduling is requested, use one explicit owner and an IANA time zone, reuse an existing matching job, and verify a real scheduled result separately from manual success.

Report completed-record filing separately from filing with work remaining, plus labels added, protected/uncertain work, errors and the remaining queue. Repeated evaluations are not distinct-thread counts. Sending, deletion, unsubscribe, filter changes and credential expansion are outside cleanup.
