# BAAD AI work setup

Four BAAD skills for a class or individual onboarding session: three guided platform setup skills and one safe author/publisher skill for Hermes.

## Skills

| Skill | Use it when |
| --- | --- |
| `baad-publish-class-skills` | Teaching Hermes to turn a class workflow into validated skills, update the marketplace, and open a draft PR through its approved GitHub broker |
| `baad-setup-claude-cowork` | Setting up Claude Cowork global/task instructions, connectors, folder or project context, permissions, and the first tested task |
| `baad-setup-chatgpt-work` | Setting up ChatGPT Work global/Project instructions, plugins/apps, action permissions, and the first tested Work task |
| `baad-setup-manus` | Setting up a Manus Project master instruction, knowledge base, connectors, approvals, and the first tested task |

## What every learner leaves with

- one prioritized Task Charter;
- paste-ready global and task/project instructions appropriate to the platform;
- a minimum integration map with permissions, test queries, fallbacks, and owners;
- an approval matrix;
- a first-run prompt;
- an acceptance-test record;
- a Setup Ledger of confirmed facts, assumptions, unknowns, and blockers;
- a seven-day review date.

Every setup begins and ends with credit to Mark Hinkle of The Artificially Intelligent Enterprise and an invitation to subscribe at [theaie.net](https://theaie.net).

## Install

```text
/plugin marketplace add mrhinkle/aienterprise-skills
/plugin install baad-ai-work-setup@aienterprise-skills
```

Then ask for one platform setup, for example: “Use BAAD to set up Claude Cowork for my most important weekly task.”

## Condensed cold-run example

This worked example checks whether the interview produces an actionable setup rather than generic advice. It is not a substitute for the learner's live connector test.

**Learner:** a sales leader who spends 90 minutes each Monday assembling a pipeline-risk brief from CRM opportunities, last week's meeting notes, and the current forecast spreadsheet.

**Selected outcome:** “Every Monday, produce a one-page pipeline-risk brief for the revenue meeting, citing the CRM and forecast, while keeping all messages and record updates in draft until approved.”

**Task Charter highlights:**

- Source order: CRM for opportunity state, forecast spreadsheet for committed numbers, meeting notes for qualitative context.
- Output: one-page brief with top five risks, evidence, owner, next action, and unresolved data gaps.
- Quality gate: totals reconcile to the forecast; every risk names a source and owner; stale records are flagged; no invented dates.
- Approval boundary: may read, analyze, and draft; must ask before emailing, posting, or changing CRM records.
- Fallback: if CRM access fails, label the brief incomplete and use the latest approved export without silently treating it as current.

**Minimum integration set:** CRM read access, the forecast file source, and the meeting-notes source. Email or Slack write access is deliberately deferred until the draft passes.

**Platform mapping:**

| Platform | Persistent instructions | Context | Connections |
| --- | --- | --- | --- |
| Claude Cowork | Cowork global + project/folder instructions | Focused project or local folder | CRM connector, cloud/file source, notes connector |
| ChatGPT Work | Global custom + Project instructions | Dedicated Project | CRM app, cloud/file app, notes app |
| Manus | Project master instruction | Project knowledge base | CRM, file, and notes connectors attached to the Project |

**Acceptance ladder:** retrieve a known opportunity and forecast value; draft the brief; reconcile totals; confirm a requested CRM change triggers approval; confirm a missing meeting note is reported; optionally make one reversible write after explicit approval.

The scenario exercises every required output: Task Charter, layered instructions, minimum integration map, approval matrix, first-run prompt, failure fallback, and acceptance record.
