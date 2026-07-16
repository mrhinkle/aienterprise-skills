# ChatGPT Work setup reference

Use this for platform directions and constraints. Verify the visible interface because Work and the plugin/app directory are rolling out.

## Recommended setup path

1. Confirm that **Work** appears in the mode switcher. Work is intended for longer research and finished documents, spreadsheets, presentations, reports, and Sites; use Codex for software development.
2. Open **Settings → Personalization → Custom Instructions**, enable customization, paste the approved global block, and save. Longer custom-instruction fields currently have a 1,500-character limit.
3. Create a dedicated **Project**. Open its menu → **Project settings**, paste the task-specific instructions, and add only approved reference files. Project instructions apply only there and override global custom instructions.
4. Select **Work** inside that Project and start the manual test.
5. Discover workflow packages from **Plugins**. Manage each underlying connection and permission from the plugin configuration or **Settings → Apps**. Interface labels may still say apps/connectors during migration.
6. For each app, review search, sync, and write capabilities separately. On managed workspaces, confirm role access, action controls, and app permissions with an admin.
7. Connect the specific account through OAuth. Use `@app` or the `+` tool menu when an explicit source test is helpful.
8. Keep consequential actions approval-gated during the initial workflow. Add a schedule/trigger only after a manual acceptance pass.

## Surface and data cautions

- Work on web/mobile runs in the cloud. Work in the desktop app can use local files and desktop apps with permission.
- At launch, cloud Work conversations and desktop Work threads may not appear on the other surface. Choose the surface where the source data and ongoing history need to live.
- Consumer-plan app data and conversation content can have different model-improvement rules from Business/Enterprise/Edu workspaces. Review **Settings → Data Controls** and workspace policy before using confidential data.
- Synced apps may index connected content. Disconnecting stops future access but existing conversations and saved memories may need separate deletion.
- Apps respect the permissions of the connected account; they do not grant access the person does not already have.

## Troubleshooting branches

| Symptom | Likely cause | Next action |
| --- | --- | --- |
| Work is missing | Gradual rollout, plan/workspace eligibility, or outdated app | Update, try an eligible surface, confirm workspace policy; prepare in a Project meanwhile |
| Plugin/app cannot connect | Region, plan, admin disablement, or provider OAuth scope | Read the app detail, ask the admin for enablement/scopes, or use an approved export |
| Source item is missing | Wrong account, sync delay, permission, or query | Confirm account and direct access; use an exact title/date/owner; test explicit `@app` selection |
| Action unavailable | Admin action control or app lacks write capability | Keep draft-only, request the exact action from the admin, or perform manually |
| Desktop file absent on web | Local/cloud surface mismatch | Run in desktop Work or upload an approved copy to the Project |
| Responses ignore global preferences | Project instructions override global or conflict | Remove duplication, put task rules in the Project, and start a fresh Work task if needed |

## Official sources

Checked July 16, 2026:

- [ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275/)
- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-using-projects-inchatgpt)
- [ChatGPT Custom Instructions](https://help.openai.com/en/articles/8096356-chat-preferences-for-chatgpt)
- [Plugins in ChatGPT and Codex](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex)
- [Apps in ChatGPT](https://help.openai.com/en/articles/11487775-apps-in-chatgpt)
- [ChatGPT apps with sync](https://help.openai.com/en/articles/10847137)
- [Data Controls FAQ](https://help.openai.com/en/articles/7730893-how-chatgpt-uses-browsing-and-memory)
- [Admin controls, security, and compliance in apps](https://help.openai.com/en/articles/11509118)
