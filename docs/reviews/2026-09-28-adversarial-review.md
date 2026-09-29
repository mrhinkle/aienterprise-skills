# Adversarial review — 2026-09-28

Hostile pass over every tracked file on `origin/main` at `f05c378` ("Add aie-direct-response skill bundle (#4)"). 101 tracked files, 7 plugin bundles, 18 skills. The question for each skill was: if an agent follows this literally, does it fail, mislead a stranger, or embarrass a public repo?

Line numbers in the table are the pre-fix locations on that commit. Status is against the companion branches listed at the bottom. Open pull requests #1, #2, #3, and #5 were not modified, rebased, or commented on. Files those PRs already change were left alone unless a fix could live in an unlocked reference or doc.

## What held up

- All 18 `SKILL.md` files have `name` and `description`. Each `name` matches its directory, matches `[a-z0-9-]{1,64}`, and the description is under 1024 characters.
- `.claude-plugin/marketplace.json` lists the same 7 plugins that exist on disk. Each `plugin.json` parses and its version matches the marketplace entry (all `1.0.0` except `aie-video` at `0.1.0-beta`). Skills are discovered from `skills/`; nothing on disk is an unlisted plugin, and nothing listed is missing.
- README skill and bundle counts match the tree (18 / 7). Those count lines live in files owned by open PRs, so they were not edited.
- No committed API keys, tokens, private phone numbers, client-confidential material, or private-repo URLs. The only home-directory-shaped string was a redacted example in the video publishing notes (F23). Email addresses in examples are placeholders.
- No `curl | bash`. No instruction to auto-approve destructive operations.
- Banned marketing words (delve, realm, unleash, tapestry, paradigm, landscape, cornerstone, game-changer, revolutionary, "unlock potential") appear only where a skill is listing words not to use. "Open source" is not hyphenated anywhere.
- `python3 -m py_compile` passes on the three video Python scripts. `swiftc -parse` passes on `ocr_slides.swift` and `liftsubject.swift` when each file is parsed alone (passing both in one invocation is a false failure: `swiftc` treats them as one module). All 8 JSON manifests parse.

## Severity counts

| Severity | Fixed | Deferred | Total |
|---|---:|---:|---:|
| P0 | 0 | 0 | 0 |
| P1 | 16 | 11 | 27 |
| P2 | 15 | 6 | 21 |
| P3 | 2 | 1 | 3 |
| **Total** | **33** | **18** | **51** |

P0 would have been a leak, a committed secret, or an install that cannot work. None of those showed up. The video failures are P1: an agent that follows the skill produces a wrong edit or a false verification failure, but the marketplace itself still installs.

## Findings

| ID | Sev | File:line | Problem | Fix | Status |
|---|---|---|---|---|---|
| F01 | P1 | `plugins/aie-video/skills/aie-video-webinar-publish/scripts/verify_edit.py:36` | Scribe helper told the operator the key "lives in ~/.zshrc" and passed `xi-api-key` on the curl argv, so the key shows up in the process list. | Read `ELEVENLABS_API_KEY` from the environment, send it via a mode-0600 curl config (`-K`) that is deleted afterwards, and redact the key from any error text. | fixed |
| F02 | P1 | `plugins/aie-video/skills/aie-video-webinar-publish/SKILL.md:80` | The transcribe step posted audio to Scribe with no mp3 conversion. Uploading the wav under an `.mp3` name, or uploading the wav itself, is not what the scripts' later mp3 path expects. | Add an explicit `ffmpeg` libmp3lame step (16 kHz mono, 64k) and say not to upload the wav as `.mp3`. | fixed |
| F03 | P1 | `plugins/aie-video/skills/aie-video-webinar-publish/SKILL.md:157` | Verify was documented without `--cuts`. A real cold-open removal of dialogue then fails the word-drift check. Same omission in `docs/video.md:57` and the render.py hint at `render.py:71`. | Pass `--cuts cuts.json` in the skill, the doc, and the script's hint. | fixed |
| F04 | P1 | `plugins/aie-video/skills/aie-video-webinar-publish/reference/webinar.config.example.md:40` | The example config presents filler lists and `max_word_loss_pct` as if the scripts read them. They do not. Editing the config does not change the edit. | Label those blocks as notes for the agent. State that the scripts hardcode the lists and the gate. | fixed |
| F05 | P1 | `plugins/aie-video/skills/aie-video-webinar-publish/SKILL.md:134` | Says the script prints the reconstructed opening. It prints a range count and seconds only. An agent will wait for text that never arrives. | Tell the agent to reconstruct the opening from the transcript minus those ranges. | fixed |
| F06 | P1 | `plugins/aie-video/skills/aie-video-webinar-publish/SKILL.md:96` | Commands are `python3 scripts/...` and `swift scripts/ocr_slides.swift`. The skill also says to work in a per-webinar folder, which does not contain `scripts/`. | Point at `/path/to/aie-video-webinar-publish/scripts/` and require absolute media paths. Same hint in `render.py`. | fixed |
| F07 | P1 | `plugins/aie-video/skills/aie-video-webinar-publish/SKILL.md:244` | Self-improvement told every run to edit the installed skill. A marketplace install would be rewritten in place. | Tell the user and offer a patch or an issue. Do not edit installed files unless asked. | fixed |
| F08 | P1 | `docs/faq.md:3` | FAQ says no skill needs an API key. The video scripts require `ELEVENLABS_API_KEY`, and publishing uses platform credentials. | Say most skills need none, name the video exception, and say never to commit a key. | fixed |
| F09 | P1 | `docs/web.md:10` | Describes `aie-web-audit` as on-page basics, performance signals, obvious SEO, and surface UX. The skill's four parts are SEO/AEO, copy, UX/mobile, and a public security-header scan. It does not measure Core Web Vitals from HTML. | Rewrite the doc sentence to match the skill and point speed at `aie-web-performance`. | fixed |
| F10 | P1 | `docs/chief-of-staff.md:38` | Tells the reader to pair the brief with a `schedule` skill. This marketplace does not ship one. Same claim in `plugins/aie-chief-of-staff/skills/aie-chief-of-staff/reference/connectors.md:31`. The skill file itself (`SKILL.md:46`) makes the same claim and is owned by PR #3. | Docs and connectors now say to use the host's scheduled tasks. The skill sentence stays deferred (D18's file). | fixed in the unlocked files |
| F11 | P1 | `plugins/aie-web/skills/aie-web-seo/reference/schema-and-aeo.md:15` | Table still promises a sitelinks search box (removed 2024-11-21), an FAQ rich result (removed May 2026), and a HowTo rich result (removed September 2023, desktop and mobile). An agent will add markup and promise a treatment Google no longer shows. | Say those three are not Google rich results, keep the markup advice that is still useful, and cite Search Central. | fixed |
| F12 | P1 | `plugins/aie-social/skills/aie-social-linkedin/reference/research-checklist.md:21` | Research says to fetch pages and has no rule that the page is untrusted data. The direct-response skills already have that rule. Same gap in the X checklist. The skill files that should say it are owned by PR #3. | Add the rule to both checklists, which the skills already tell the agent to read. | fixed |
| F13 | P1 | `plugins/aie-social/skills/aie-social-linkedin/reference/quality-rubric.md:37` | "Report the score" after ten pass/fail checks, with no mapping from checks to a number. Same line in the X rubric (`quality-rubric.md:38`). | Score is the count of passing checks, written `N/10`. | fixed |
| F14 | P1 | `plugins/aie-direct-response/skills/direct-response-campaign-writer/SKILL.md:3` | The description trigger "create a direct-response campaign" selects this skill for email launches. The body already routes email to `email-launch-writer`; the description, which is what triggers, did not. | Description now says not to use it for promotional email or launch sequences, and to use `copy-chief` when the request is critique. Length 482, still under 1024. | fixed |
| F15 | P1 | `plugins/aie-web/skills/aie-web-forms/reference/serverless-example.md:13` | Honeypot field is `company_website`, a real B2B form field. Legitimate submissions get rejected. The same name is in the skill snippet at `SKILL.md:32`, which PR #3 owns. | Example now uses `company_website_hp` and says the skill snippet is still wrong. | fixed in the example; skill line deferred (D20) |
| F16 | P1 | `plugins/aie-web/skills/aie-web-testing/reference/patterns.md:33` | The "catch silent failures" sample hangs errors on `(page as any)._errors`, listens to every console error and every `requestfailed` (ads and analytics), and the assertion is only a comment. | Fixture collects same-origin `pageerror`s and asserts inside the test. Console and third-party request failures are called out as noise, not a default failure. | fixed |
| F17 | P2 | `plugins/aie-video/skills/aie-video-webinar-publish/SKILL.md:114` | Docs say "you know" is counted and never cut. The script has no bigram matcher, so it neither cuts nor counts it. Config `never_cut` listed it too (`webinar.config.example.md:38`). | Discourse-marker list matches `MARKERS`. "you know" is described as undetected. | fixed |
| F18 | P2 | `plugins/aie-video/skills/aie-video-webinar-publish/reference/webinar.config.example.md:40` | Config and the written gate used ±1%. `verify_edit.py` passes at ±1.5% and at least 40% of fillers removed. | Skill table, doc table, and config notes match the script: ≥40% fillers, ±1.5% word drift. Healthy target stays 60–70%. | fixed |
| F19 | P2 | `plugins/aie-video/skills/aie-video-webinar-publish/SKILL.md:95` | Thumbnail step imports Pillow. `pip install` line omitted `pillow`. Same gap in `docs/video.md`. | Add `pillow` to both install lines. | fixed |
| F20 | P2 | `plugins/aie-social/skills/aie-social-linkedin/reference/formatting-guide.md:1` | Both formatting guides state 2026 algorithm numbers. `sources.md` exists and `docs/social.md` mentions it, but the guide the agent is told to follow never says to re-check those URLs. LinkedIn `SKILL.md:10` also says "three reference files" while listing four and omitting `sources.md` (that sentence is D11). | Top of both formatting guides: read `sources.md`, re-check the URLs, and trust the live page over the snapshot. | fixed |
| F21 | P2 | `plugins/aie-chief-of-staff/skills/aie-chief-of-staff/reference/cos.config.example.md:76` | Filled example used ShipLoop, FreightIQ-style competitors, and `ceo@shiploop.com`. `shiploop.io` is a real site. A public example should not look like a client. | Reserved `.example` names: Northwind Freight, Example Hauler, Sample Logistics. | fixed |
| F22 | P2 | `.gitignore:1` | Ignore list was `.DS_Store`, `node_modules/`, `slop.config.md`, `*.log`. A filled `cos.config.md`, `webinar.config.md`, `voice.config.md`, `.env`, or `__pycache__` could be committed. | Ignore those. `!.env.example` stays committable. Example files are named `*.example.md`, so they are not ignored. | fixed |
| F23 | P2 | `plugins/aie-video/skills/aie-video-webinar-publish/reference/publishing.md:21` | Error example used a `/Users/.../` path. | `/path/to/edited.mp4`. | fixed |
| F24 | P2 | `plugins/aie-video/skills/aie-video-webinar-publish/scripts/verify_edit.py:18` | Docstring named an internal recording ("Build Skills") as the evidence for the cold-open false failure. | Say "a real hour-long webinar" and keep the measured numbers (272 words, false −3.39%, true −0.7%). | fixed |
| F25 | P2 | `plugins/aie-video/skills/aie-video-webinar-publish/scripts/verify_edit.py:38` | `curl -s` with no status check. A 401 body could be parsed as a transcript. | `-sS`, append `%{http_code}`, fail unless curl exits 0 and the code starts with 2. | fixed |
| F26 | P2 | `plugins/aie-video/skills/aie-video-webinar-publish/scripts/build_edit.py:54` | `dur()` did `float(stdout.strip())`. Two audio streams print two durations and the check crashes, or a failed ffprobe yields an empty float. | Require return code 0, exactly one non-empty duration line, and say to extract a single stream. | fixed |
| F27 | P2 | `plugins/aie-video/skills/aie-video-webinar-publish/scripts/ocr_slides.swift:8` | Unreadable images and Vision failures `continue` with no stderr. Zero arguments and zero titles both exit 0. The skill then treats silence as "no chapters" and may invent titles. | Usage on stderr and exit 2 when there are no args. Stderr per failure. Exit 1 when nothing was recognized. | fixed |
| F28 | P2 | `plugins/aie-video/skills/aie-video-webinar-publish/SKILL.md:207` | Chapter step said the tool "reads slide titles off sampled frames" but never gave the sample or OCR commands, so the agent improvises. | `ffmpeg -vf fps=1/10` plus the swift invocation. Exit 1 means invent nothing. | fixed |
| F29 | P2 | `docs/social.md:5` | Both social skills honor a `voice.config.md` in the working directory. No example file existed, so the agent invents the schema. | `reference/voice.config.example.md` in each social skill. `docs/social.md` says to copy it and not commit the filled file. | fixed |
| F30 | P2 | `plugins/aie-web/skills/aie-web-links/reference/fixes.md:24` | Orphan section told the agent to fix pages a homepage crawl cannot see. Following it means inventing orphans. | Say a crawl cannot see unlinked pages. Need a sitemap, source tree, or host file list. URL-only means out of scope. | fixed |
| F31 | P3 | `plugins/aie-video/skills/aie-video-webinar-publish/scripts/build_edit.py:26` | `PAD = 0.06` was defined and never used. | Removed. | fixed |
| F32 | P3 | `plugins/aie-video/skills/aie-video-webinar-publish/scripts/render.py:67` | A successful concat left `{out}.parts/` behind. A blanket `rmtree` of that path would also delete unrelated files if the directory already existed. | After a successful concat, unlink only the part files and `concat.txt` this run created, then `rmdir`. If the directory is not empty, leave it and say so. | fixed |
| F33 | P2 | `plugins/aie-direct-response/skills/copy-chief/reference/audit-rubric.md:26` | Bands put 80–89 in B, and a Major issue caps the score at 89 labeled `NOT PERFORMANCE-READY`. Read quickly, band B and "not performance-ready" look like a contradiction. The cap is intentional. | One sentence: the letter is not a release decision, and a capped 89 can sit in band B and is still not performance-ready. | fixed |
| D01 | P1 | `plugins/ai-slop-killer/skills/ai-slop-killer/reference/scoring.md:37` | Score is `total_points / word_count * 1000`, so a short piece saturates at 100. | PR #3 already changes the multiplier to 500 ("per 500 words"). Not touched here. | deferred — PR #3 owns `scoring.md` and already edits this line |
| D02 | P1 | `plugins/ai-slop-killer/skills/ai-slop-killer/reference/scoring.md:13` | Severe is 5 points for any hard-banlist word, and Moderate is 2 points for "corporate-AI vocabulary" that includes words also on that banlist (the catalog lists elevate, foster, streamline, myriad, pivotal as both). One word can be booked twice. | Do not retune the rubric inside a file PR #3 is rewriting. PR #3's diff does not touch this double count. | deferred — file owned by PR #3; the overlap is still there after that PR |
| D03 | P1 | `plugins/ai-slop-killer/skills/ai-slop-killer/SKILL.md:48` | Fiction mode says "section-7 checks". Section 7 of `slop-catalog.md` is substance/factual (line 134). Fiction checks are section 8 (line 146). | Do not renumber the catalog. The skill sentence is the bug, and PR #3 owns the skill. | deferred — PR #3 owns the file |
| D04 | P1 | `plugins/aie-web/skills/aie-web-qa/SKILL.md` (description) | QA, links, and testing descriptions overlap ("test my site", broken links, forms). The wrong specialist triggers. | PR #3 narrows the QA description and drops those phrases. | deferred — PR #3 already edits the descriptions |
| D05 | P1 | `plugins/aie-web/skills/aie-web-audit/SKILL.md` (handoff) | The broad audit finds header and mixed-content issues and does not hand them to `aie-web-security`. | PR #3 adds that handoff. | deferred — PR #3 |
| D06 | P1 | `plugins/aie-web/skills/aie-web-audit/SKILL.md:25` | SEO part still tells the agent to score Core Web Vitals indicators from a URL fetch. Field data is not in the HTML. `docs/web.md` no longer repeats the claim (F09). | Leave the skill. Changing it conflicts with PR #3. | deferred — PR #3 owns the skill |
| D07 | P1 | `plugins/aie-web/skills/aie-web-qa/SKILL.md` | QA checklist requires four browsers for a pass that most agents cannot actually run. | Subjective how far to narrow it, and the skill is in PR #3. | deferred — PR #3 owns the skill |
| D08 | P1 | `plugins/ai-slop-killer/skills/ai-slop-killer/SKILL.md` (description) | Bare "copyedit" triggers the slop killer for ordinary edits. | PR #3 narrows the phrase to "copyedit this for AI tells". | deferred — PR #3 |
| D09 | P1 | `plugins/ai-slop-killer/skills/ai-slop-killer/SKILL.md` (description) | Description also auto-triggers after other prose skills. That is a product choice, not a typo. Narrowing it would change who the skill is for. | Leave it. | deferred — product scope, and the file is in PR #3 |
| D11 | P2 | `plugins/aie-social/skills/aie-social-linkedin/SKILL.md:10` | "Read the three reference files" then lists four, and never names `sources.md`. | F20 points at `sources.md` from the formatting guide, which this skill does tell the agent to read. The count sentence stays. | deferred — PR #3 owns the skill |
| D12 | P2 | several `SKILL.md` files | Many skills have no `examples/sample-run.md`. PR #3 adds 14 of them. Direct response and video still have none. | Do not invent sample runs. A fake transcript would be worse than a missing example. | deferred — inventing examples is not a confident fix |
| D13 | P2 | web UX vs QA checklists | One skill says tap targets about 48px, another cites the WCAG 44px minimum. The 48px line is a house rule, not a claim that 44 fails WCAG. Aligning them means editing skills PR #3 owns. | Leave both. | deferred — not a false statement, and the skills are in PR #3 |
| D14 | P2 | `plugins/ai-slop-killer` vs writing skills | Em-dash limits disagree across skills (a hard cap in one, a lighter rule in another). | Unifying them rewrites voice rules that are intentionally different per skill. | deferred — subjective |
| D16 | P1 | `docs/getting-started.md:7` | Says no API keys are required, and the install story omits bundles that later PRs add. Same file is in PR #1 and PR #2. | FAQ is corrected (F08). This file is not. | deferred — PR #1 and PR #2 both edit it |
| D17 | P2 | `plugins/aie-social/skills/aie-social-x/SKILL.md:3` | "make a thread" is broad enough to steal non-X work. Tightening the description is a product call. | Leave the trigger. PR #3 already touches this file for other reasons. | deferred — subjective, file owned by PR #3 |
| D18 | P2 | `plugins/aie-chief-of-staff/skills/aie-chief-of-staff/SKILL.md:3` | "brief me" and "catch me up" are broad. The skill also still names a `schedule` skill at line 46 (see F10). | Docs and connectors are fixed. The skill file is in PR #3. | deferred — PR #3 owns the skill |
| D20 | P1 | `plugins/aie-web/skills/aie-web-forms/SKILL.md:32` | Honeypot snippet still uses `company_website`. The worked example no longer matches it, on purpose, and the example says so. | Change the skill when PR #3 is not sitting on it. | deferred — PR #3 owns the skill |
| D21 | P3 | `plugins/aie-video/skills/aie-video-webinar-publish/scripts/render.py:45` | Snyk Code reports low path-traversal on CLI paths (`--cuts`, `--out`, and the same pattern in `build_edit.py` and `verify_edit.py`). These are local operator tools. The path is the file the user named. Refusing absolute paths would break the skill, which requires them. | The new `rmtree` sink was removed (F32). Remaining findings are the CLI itself. | deferred — not a service-side traversal; sanitizing it breaks the tool |

D10 from the working notes (social skill files lack the untrusted-page rule) is not a separate item. F12 puts the rule in the checklists those skills already require.

## Not findings

- `ffprobe` with more than one `-show_entries` still prints duration on a generated mp4. That was tested and is not the multi-stream bug. F26 is the multi-line stdout case.
- Copy-chief's cap at 89 is not a math error. F33 only explains it.
- Banlist mentions of banned words are the list doing its job.
- `plugins/aie-writing-room` and the other bundles in PRs #1, #2, and #5 are not on `main`. They were not reviewed as part of this tree.

## How the fixes were checked

- `python3 -m py_compile` on `build_edit.py`, `render.py`, and `verify_edit.py` after the last edit.
- `swiftc -parse` on `ocr_slides.swift` alone, and on `liftsubject.swift` alone.
- `json` parse of every `*.json` in the tree (8 files).
- `git diff` scanned for the banned words and for `open-source`. No hits.
- Campaign-writer description length measured at 482 characters.
- Snyk Code on the video `scripts/` directory. The `shutil.rmtree` finding closed when cleanup became unlink plus `rmdir`. Remaining lows are D21.
- No ffmpeg render was run. There is no fixture webinar in the repo, and synthesizing one would not exercise Scribe.

## Files left untouched on purpose

PR #1 (`agent/baad-ai-work-setup`) and PR #2 (`agent/add-hermes-ha-skill`) both change `.claude-plugin/marketplace.json`, `README.md`, `docs/README.md`, and `docs/getting-started.md`. PR #5 (`add-writing-bundles`) changes the marketplace and the two READMEs as well. PR #3 (`audit-fixes`) changes the `SKILL.md` (and adds `examples/sample-run.md`) for ai-slop-killer, chief of staff, skill creator, both social skills, and all nine web skills, plus `plugins/ai-slop-killer/skills/ai-slop-killer/reference/scoring.md`.

## Companion pull requests

Opened 2026-09-28 against `main`. Not merged.

| Branch | Findings | URL |
|---|---|---|
| `grok/review-report` | this report, F22 | https://github.com/mrhinkle/aienterprise-skills/pull/7 |
| `grok/review-video` | F01 F02 F03 F04 F05 F06 F07 F17 F18 F19 F23 F24 F25 F26 F27 F28 F31 F32 | https://github.com/mrhinkle/aienterprise-skills/pull/8 |
| `grok/review-docs` | F08 F09 | https://github.com/mrhinkle/aienterprise-skills/pull/9 |
| `grok/review-web-refs` | F11 F15 F16 F30 | https://github.com/mrhinkle/aienterprise-skills/pull/10 |
| `grok/review-social` | F12 F13 F20 F29 | https://github.com/mrhinkle/aienterprise-skills/pull/11 |
| `grok/review-copy-cos` | F10 F14 F21 F33 | https://github.com/mrhinkle/aienterprise-skills/pull/12 |
