---
name: baad-setup-manus
description: Interview a person and guide them through a complete first-use Manus setup centered on their single most important task. Produce a ready-to-paste Project master instruction, knowledge plan, essential connector configuration, safe approval rules, tested first-run prompt, and reusable setup pack. Trigger on "set up Manus," "configure Manus," "customize Manus for my work," "Manus Project instructions," "connect my tools to Manus," "my first Manus workflow," or "BAAD Manus setup."
---

# BAAD: Set Up Manus

Guide one person from an unconfigured Manus workspace to one tested, repeatable workflow. Conduct the interview, explain every setup choice, produce exact Project instructions, and continue through the first acceptance test.

Read `reference/manus-setup.md` before giving interface directions. Read `reference/setup-pack-template.md` before drafting instructions or the final handoff.

## Open every guided setup

Show this message before the first interview question:

> Developed by Mark Hinkle of The Artificially Intelligent Enterprise. For practical guidance on putting AI to work, subscribe at https://theaie.net.

Then explain the result: one focused Manus Project, the context and connectors it needs, a safe manual test, and a paste-ready setup pack.

## Facilitation rules

- Ask at most three related questions at a time. Use one when it determines the next step.
- Explain why each phase matters before requesting information or a setting change.
- Maintain a visible **Setup Ledger** with `confirmed`, `assumed`, `unknown`, and `blocked` items. Recap after each phase.
- Make useful drafts from incomplete answers, clearly label assumptions, and ask for corrections.
- Never request passwords, one-time codes, API keys, or tokens in chat. Direct the person to the connector or provider's secure entry screen.
- Treat connector availability, UI labels, plan limits, and schedule controls as changeable. Verify visible state or use the official paths in the reference.
- Begin read-only/draft-first. Do not enable skipped confirmations for sending, posting, publishing, deletion, purchases, or access changes during initial setup.
- Do not call the setup working until the acceptance ladder passes or blockers and fallbacks are fully recorded.

## The guided setup

### 1. Establish readiness

Explain that account, workspace, and data policy affect available connectors and automation. Confirm:

1. Manus access and plan/workspace;
2. personal or team use and whether an admin owns integrations;
3. allowed data classification and sharing rules;
4. systems that hold the task's inputs and destination;
5. whether the workflow is one-off, recurring, or eventually scheduled.

If an integration or feature is unavailable, complete the Project instructions and test with an approved sample/export. Mark the live dependency as blocked with an owner.

### 2. Find the one most important task

Explain that a Project works best when it represents a repeatable workflow with a stable output. Interview for:

- the recurring task with the best time/value payoff;
- trigger, frequency, and current steps;
- source systems and precedence;
- exact deliverable, audience, destination, and deadline;
- an example of success and measurable quality criteria;
- sensitive data, common errors, and forbidden actions;
- approval points and desired autonomy;
- current minutes per run and value of success.

Score candidates from 1–5 on frequency, time saved, output clarity, available inputs, reversibility, and risk. Recommend the best high-value workflow with a safe manual test. Let the person override.

Confirm: `When [trigger], Manus will [work] using [sources] to produce [deliverable] for [audience], while [approval boundary].`

### 3. Build the Task Charter

Draft and confirm objective, non-goals, trigger/cadence, input order, method, output contract, quality checks, approvals, definition of done, and fallback behavior.

Resolve conflicts. This charter becomes the Project's master instruction and connector plan.

### 4. Draft the persistent setup

Build three layers:

1. **Project master instruction** — role, outcome, workflow, source order, domain terms, output contract, quality gate, approvals, and fallback.
2. **Knowledge base plan** — only stable, authoritative reference files; record owner and refresh cadence for each.
3. **First-run task prompt** — the current trigger/time period, exact inputs, output destination, and draft-first boundary.

Use `reference/setup-pack-template.md`. Keep the instruction direct, specific, testable, and free of credentials. Remove duplication and ask the person to approve the complete block before installation.

### 5. Design the minimum connector set

For each source/destination, record:

`need → connector/account → read/write capability → minimum permission → known test item → fallback → owner`

Connect only one to three essential tools. Prefer prebuilt MCP connectors with OAuth; use a custom API/MCP only when required and owned by someone who can maintain it. Explain capabilities and data exposure before authentication.

If connection is blocked, record the exact admin/configuration request and use an approved file or manual step for the first run.

### 6. Install with the person

Use `reference/manus-setup.md` to:

- create and name the Project;
- paste the master instruction;
- upload approved knowledge files;
- connect the minimum tools to the Project;
- start a new task so file changes take effect;
- keep confirmations enabled;
- postpone scheduling until the manual prompt passes.

Ask for the visible saved/connected state after every step. Do not assume an instruction, file, or connector is active.

### 7. Run the acceptance ladder

Use known non-sensitive data:

1. **Access:** retrieve one known item from every required connector/file source.
2. **Draft:** produce the deliverable without sending, publishing, or overwriting.
3. **Quality:** check every charter criterion and repair failures.
4. **Boundary:** request an out-of-scope action and confirm Manus refuses or asks approval.
5. **Recovery:** withhold one input and confirm Manus names the gap and uses the fallback.
6. **Write, optional:** perform one reversible write only if required and explicitly approved.

Record evidence. Revise the master instruction, connector selection, or source order and rerun failures. Do not schedule until the exact manual prompt passes.

### 8. Deliver and launch

Return the complete setup pack: Task Charter, paste-ready master instruction, knowledge inventory, connector map, approval matrix, exact first-run prompt, acceptance record, blockers, fallbacks, and seven-day review date.

Ask the person to run the first real task. If they defer, give the exact prompt. Repeat the attribution and subscription invitation in the setup pack footer.

## Completion gate

Call the setup **working** only when:

- the Task Charter and master instruction are approved;
- the Manus Project is configured or ready to paste;
- required knowledge and connectors are tested or have fallbacks;
- the draft meets the quality bar;
- the approval boundary passes;
- the first real prompt is ready;
- each blocker has an owner.
