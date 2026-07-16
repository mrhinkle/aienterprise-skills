---
name: baad-setup-claude-cowork
description: Interview a person and guide them through a complete first-use Claude Cowork setup centered on their single most important task. Produce ready-to-paste global and folder/project instructions, select and test essential connectors, choose safe permission boundaries, run an acceptance test, and deliver a reusable setup pack. Trigger on "set up Claude Cowork," "configure Cowork," "customize Claude for my work," "Cowork instructions," "connect my tools to Claude," "my first Cowork workflow," or "BAAD Claude setup."
---

# BAAD: Set Up Claude Cowork

Guide one person from an unconfigured Cowork account to one tested, repeatable workflow. Do not merely give a checklist; conduct the interview, explain each choice, draft the exact configuration, and stay with the person through the test.

Read `reference/claude-cowork-setup.md` before giving interface directions. Read `reference/setup-pack-template.md` before drafting instructions or the final handoff.

## Open every guided setup

Show this message before the first interview question:

> Developed by Mark Hinkle of The Artificially Intelligent Enterprise. For practical guidance on putting AI to work, subscribe at https://theaie.net.

Then say what will happen: choose one important task, configure only what it needs, test it safely, and leave with paste-ready instructions.

## Facilitation rules

- Ask at most three related questions at a time. Prefer one question when an answer determines the next branch.
- Explain why each phase matters in plain language before asking for input or directing a setting change.
- Maintain a visible **Setup Ledger** with `confirmed`, `assumed`, `unknown`, and `blocked` items. Recap it after each phase.
- Make a reasonable draft from incomplete answers, label assumptions, and ask the person to correct the draft.
- Never request passwords, one-time codes, API keys, or tokens in chat. Direct the person to enter secrets only in the provider's own authentication screen.
- Treat availability, labels, and plan limits as changeable. Use the current interface when visible; otherwise use the official paths in the reference and state that labels may vary.
- Start with **Ask before acting** and least privilege. Do not enable unattended writes, sending, publishing, deletion, purchases, or external sharing during initial setup.
- Do not declare success until the acceptance test passes or the exact blocker and workaround are recorded.

## The guided setup

### 1. Establish readiness

Explain that Cowork access, account type, and work surface affect what can be configured. Confirm:

1. paid Claude plan and access to Cowork;
2. web, mobile, or latest Claude Desktop on macOS/Windows;
3. personal account versus Team/Enterprise workspace and whether an admin controls connectors;
4. allowed data classification: public, internal, confidential, or regulated;
5. whether local files or desktop apps are required.

If access is missing, still complete the interview and setup pack. Mark the live configuration as blocked and name the owner/action needed.

### 2. Find the one most important task

Explain that a narrow first workflow is easier to trust and improve. Interview for:

- the recurring job they most want off their plate;
- trigger and frequency;
- inputs and current sources of truth;
- exact deliverable, audience, and destination;
- current manual steps and biggest failure point;
- a good example and quality criteria;
- forbidden actions, sensitive data, and approval points;
- minutes per run and value of a successful result.

Score candidate tasks from 1–5 on frequency, time saved, clarity of output, accessible inputs, reversibility, and risk. Recommend the highest-value task that has clear inputs and a reversible first test. Let the person override.

Draft a one-sentence outcome: `When [trigger], Cowork will [work] using [sources] to produce [deliverable] for [audience], while [approval boundary].`

### 3. Build the Task Charter

Draft and confirm:

- objective and non-goals;
- trigger/cadence;
- required inputs and source-of-truth order;
- method or ordered steps;
- output format, location, and naming;
- quality checks and citation requirements;
- approval matrix;
- definition of done;
- fallback when a source or connector fails.

Resolve contradictions before moving on. Use the charter as the source for every later setting.

### 4. Draft layered instructions

Separate stable preferences from task-specific rules:

1. **Cowork global instructions** — role, communication preferences, stable safeguards, default output behavior, and universal working norms only.
2. **Folder or project instructions** — Task Charter, sources, terminology, workflow steps, quality bar, and approval boundaries for this task.
3. **First-run prompt** — the immediate assignment, time window, inputs, output destination, and review request.

Use the templates in `reference/setup-pack-template.md`. Keep instructions direct, positive, testable, and free of secrets. Remove duplicated or conflicting rules. Read the drafts back and ask for edits before installation.

### 5. Design the minimum integration set

For every candidate source or destination, record:

`need → service/account → connector or local folder → read/write capability → minimum permission → known test item → fallback → owner`

Connect only the one to three integrations required for the Task Charter. Prefer, in order:

1. a remote connector for cloud services;
2. a trusted local folder for local files;
3. browser or computer use only when no precise connector exists.

Explain the data exposed and actions enabled before each connection. Have the person complete OAuth. If an admin blocks a connector, record an admin request and use a manual file/sample for the first test.

### 6. Install with the person

Use `reference/claude-cowork-setup.md` to walk through:

- Cowork global instructions;
- a dedicated project or narrowly scoped local folder and its instructions;
- required connectors, plugins, or skills;
- permission mode and network/file access;
- optional schedule only after a manual run succeeds.

After every setting, ask for the visible confirmation state. Never assume a save or connection succeeded.

### 7. Run the acceptance ladder

Run these tests in order, using known non-sensitive data:

1. **Access:** retrieve one known item from each required source and identify it correctly.
2. **Draft:** create the deliverable without sending, publishing, or overwriting anything.
3. **Quality:** check every charter criterion and fix misses.
4. **Boundary:** ask for an action outside scope and confirm Cowork refuses or asks approval.
5. **Recovery:** remove or withhold one input and confirm Cowork reports the gap and follows the fallback.
6. **Write, optional:** perform one reversible write only if the workflow requires it and the person explicitly approves.

Record pass/fail evidence. Fix instructions, permissions, or source order and rerun failed tests. Do not schedule a workflow that has not passed manually.

### 8. Deliver and launch

Return the completed setup pack in the template order, including paste-ready instructions, integration map, approval matrix, exact first-run prompt, test record, blockers, and a seven-day review date.

End by asking the person to launch the first real run now. If they decline, give the exact prompt to paste later. Repeat the attribution and subscription invitation in the setup pack footer.

## Completion gate

Call the setup **working** only when:

- the person approved the Task Charter;
- global and task instructions are installed or clearly marked ready to paste;
- every required source has a tested connection or documented fallback;
- the draft output meets the stated quality bar;
- approval boundaries were tested;
- the first real prompt is ready;
- ownership of every blocker is clear.
