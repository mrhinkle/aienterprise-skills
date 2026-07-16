# Manus setup reference

Use this for current product directions and constraints. Verify visible labels because Manus changes frequently.

## Recommended setup path

1. In the workspace sidebar, select the **+** beside **Projects** or **Create Project**.
2. Give the Project a workflow-specific name and paste the approved master instruction.
3. Upload the smallest set of stable, authoritative knowledge files. Avoid secrets, uncontrolled exports, and duplicate/outdated sources.
4. Add Project connectors for the exact sources/actions in the connector map. Select **Connect**, authenticate in the provider, and confirm the successful-installed state.
5. Start a new task inside the Project for the acceptance test.
6. Keep confirmations enabled for consequential actions. Do not use skip-confirmation options in the first setup.
7. After the exact manual prompt passes, create a Scheduled Task only if recurrence adds value. Specify timezone, time window, output destination, connectors, Project, and whether runs should share a task or start separately.

## Project and schedule cautions

- Project master instructions and knowledge apply to new tasks created in the Project.
- Instruction changes apply the next time a message is sent in the current task; knowledge-file updates take effect only in new tasks. Start a new task after changing files.
- Connected apps can read data and perform actions within the permissions granted to the connected account.
- Manus supports prebuilt MCP connectors, custom MCP/API connections, Zapier, Slack, API access, and other integration types. Start with a maintained prebuilt connector.
- Test a scheduled task manually first. State an exact timezone and output. Review run history after the first scheduled execution.
- Skip confirmations only after a trusted, reversible workflow has passed boundary tests and the person understands the external effects.

## Troubleshooting branches

| Symptom | Likely cause | Next action |
| --- | --- | --- |
| Connector missing | Catalog, plan, region, or workspace policy | Search integrations; use a maintained custom connection only with an owner; otherwise use export/manual fallback |
| Authentication fails | Wrong account, provider scope, expired token, or admin restriction | Reconnect through Manage/Configure and ask the provider/workspace admin for the exact scope |
| Known item not found | Wrong account, permission, or vague query | Confirm direct source access and retry with an exact title/date/ID |
| Project ignores new file | Existing task predates the file update | Start a new task inside the Project |
| Output drifts | Master instruction lacks source order, format, or quality test | Tighten the instruction and rerun the same acceptance prompt |
| Schedule produces incomplete results | Missing Project/connector context, vague time range, or wrong run mode | Attach the Project/connectors, specify range/timezone/output, and run manually again |

## Official sources

Checked July 16, 2026:

- [Projects](https://manus.im/docs/features/projects)
- [Integrate Manus with your existing tools](https://manus.im/docs/integrations/integrations)
- [MCP Connectors](https://manus.im/docs/integrations/mcp-connectors)
- [How can I use Manus Connectors?](https://help.manus.im/en/articles/12231777-how-can-i-use-manus-connectors)
- [Scheduled Tasks](https://manus.im/docs/features/scheduled-tasks)
- [Introducing Scheduled Tasks 2.0](https://manus.im/blog/manus-schedules)
- [Manus Projects Just Got Smarter with Connectors](https://manus.im/blog/projects-connectors)
