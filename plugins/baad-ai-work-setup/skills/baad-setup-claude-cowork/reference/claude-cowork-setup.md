# Claude Cowork setup reference

Use this file for current interface guidance and platform-specific constraints. Verify visible labels when possible because Cowork is evolving.

## Recommended setup path

1. Confirm a paid Claude plan and select **Cowork** from the message composer.
2. For account-wide Cowork preferences, open **Settings → Cowork → Global instructions → Edit**, paste the approved global block, and save.
3. For cloud work, create a focused project and add its task instructions and approved reference files.
4. For desktop work with local files, select the narrowest useful folder and add folder instructions. Avoid granting a home folder, broad shared drive, or secrets directory.
5. Add remote services through **Customize → Connectors** or **Settings → Connectors**. Use the directory's capability description to distinguish read from write actions. Team/Enterprise users may need an owner to enable a connector first.
6. Prefer remote connectors for cloud/SaaS tools. Use desktop extensions for local services or local folders. Use browser/computer interaction only when a connector is unavailable.
7. Set **Ask before acting** for the initial workflow. Consider lower-friction approval modes only after successful boundary testing and only for reversible actions.
8. Run the workflow manually before scheduling it.

## Local, cloud, and scheduled-task cautions

- Cowork can run remotely, but tasks that need local files, browser state, or desktop apps require Claude Desktop to be open and connected.
- Remote scheduled tasks can use connected tools and files saved to the Claude account. They cannot depend on an arbitrary local computer folder while the computer is unavailable.
- Scheduled tasks run as separate Cowork sessions. Put all required context in the saved prompt, project, account-hosted files, connectors, plugins, or skills.
- Permanent file deletion always requires explicit permission. Keep deletion outside the first workflow.
- Connector access follows the person's permissions in the source service. A connector does not grant access the person lacks.

## Troubleshooting branches

| Symptom | Likely cause | Next action |
| --- | --- | --- |
| Cowork is absent | Plan, rollout, app version, or admin toggle | Confirm plan, update the app, try web, or ask the workspace owner |
| Connector unavailable | Plan/region/admin restriction | Record an admin request; use an approved export or sample file |
| Known item not found | Wrong account, insufficient source permission, or vague query | Confirm account/workspace, open the item directly, and retry with an exact identifier |
| Local file unavailable | Folder not granted or Desktop disconnected | Attach only the needed folder/file and keep Desktop open |
| Too many approval prompts | Workflow uses browser/computer interaction or broad writes | Prefer a precise connector; narrow the workflow before changing approval mode |
| Schedule fails | Local dependency, missing connector, or incomplete saved prompt | Run manually, move context to the project/account, and test the saved prompt again |

## Official sources

Checked July 16, 2026:

- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- [When to use desktop and web connectors](https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors)
- [Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
- [Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)
- [Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)
