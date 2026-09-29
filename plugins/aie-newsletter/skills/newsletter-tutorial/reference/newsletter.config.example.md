# Newsletter config (example)

Every skill in the `aie-newsletter` plugin reads one config file for your house
rules. Copy this file to `newsletter.config.md` at the root of your project (or
to `~/.claude/newsletter.config.md` to use it everywhere) and edit the values.

**Lookup order:** a path the user names in the request, then
`./newsletter.config.md`, then `~/.claude/newsletter.config.md`. If none exists,
the skill uses the defaults below and asks only for `publication.name`.

Nothing here is required except the publication name. Leave a value empty (`""`
or `[]`) to turn that feature off. The same file serves all five skills; each
skill reads the shared blocks plus its own block under `editions`.

```yaml
# ── Publication ────────────────────────────────────────────────
publication:
  name: "Your Newsletter"            # required
  url: "https://example.com"         # used for "check recent editions" and slugs
  post_url_pattern: "https://example.com/p/{slug}"
  beat: "AI"                         # the subject you cover; research is scoped to it
  audience: >
    Business leaders and operators who use this subject at work and need
    practical, cited information they can repeat in a meeting.
  platform: "beehiiv"                # beehiiv | substack | ghost | kit | mailchimp | other
  timezone: "America/New_York"

# ── Voice & style ──────────────────────────────────────────────
voice:
  style_file: ""                     # path to your voice/style guide, e.g. ./style/voice.md
  voice_skill: ""                    # optional: a skill that writes in the author's voice
  author_persona: >
    A knowledgeable peer who follows the beat closely. Not a hype machine, not
    an academic. First person where the edition calls for it.
  kicker_prefix: "// "               # label style for section kickers; "" to disable
  prefer_em_dashes: true             # em dashes over semicolons for punch
  emoji_policy: "subject-and-preview-only"   # none | subject-and-preview-only | allowed
  no_tables_in_body: false           # true = convert any table to a bulleted list
  final_prose_pass_skill: "ai-slop-killer"   # run on every draft before review

banned_words:                        # auto-fail in review if any appear
  - delve
  - realm
  - unleash
  - tapestry
  - paradigm
  - landscape
  - cornerstone
  - game-changer
  - revolutionary
  - unlock
banned_phrases:
  - "In this edition"
  - "Let's dive in"
  - "In today's fast-moving world"
spelling_rules:
  - "\"open source\" is two words, never hyphenated"

# ── Citations ──────────────────────────────────────────────────
citations:
  style: "inline-link"               # inline-link | footnotes | endnotes
  require_primary_sources: true      # company blog, official filing, tier-1 outlet
  never_link_to:                     # research FROM these, but never cite them
    - other newsletters
    - aggregators and AI news roundups
  tier_one_outlets:
    - Bloomberg
    - The Wall Street Journal
    - Reuters
    - CNBC
    - TechCrunch
    - The Verge
  min_sources_deep_dive: 5

# ── Research sources (news digest, tactic) ─────────────────────
sources:
  scan_for_leads:                    # places to discover stories; not cited
    - "Newsletters and aggregators you already read"
    - "Product launch trackers and tool directories"
  canonical:                         # places to cite
    - "Company blogs and official announcements"
    - "Regulator and government releases"
    - "Tier-1 outlets listed under citations.tier_one_outlets"
  apps_readers_use:                  # big updates here beat obscure launches
    - Notion
    - Slack
    - Figma
    - Canva
    - VS Code
  freshness_days: 7

# ── Images & metadata ──────────────────────────────────────────
images:
  skill: ""                          # optional image-generation skill name
  aspect_ratio: "16:9"
  brand_notes: ""                    # palette, style, "no embedded text", etc.
metadata:
  fields: [title, subtitle, subject_a, subject_b, preview_text, seo_title,
           meta_description, slug]
  seo_title_max_chars: 200
  meta_description_max_chars: 500
  preview_text_prefix: ""            # e.g. four emojis for the community edition
  social_posts:                      # one draft per entry; [] to skip
    - { channel: "LinkedIn (publication page)" }
    - { channel: "LinkedIn (author)" }
    - { channel: "X" }
  linkedin_hashtags: false

# ── Review ─────────────────────────────────────────────────────
review:
  pass_score: 90                     # out of 100; below this, fix and re-score
  max_revision_rounds: 3             # then stop and show the user the open items

# ── Staging (the approval gate) ────────────────────────────────
staging:
  # Where a finished, reviewed edition lands for a human to approve.
  # A markdown file, or your CMS/Notion database if connected — set here.
  destination: "file"                # file | notion | cms
  file_dir: "./editions"             # destination: file → {file_dir}/{date}-{slug}.md
  notion_database: ""                # destination: notion → database name or URL you own
  cms_collection: ""                 # destination: cms → collection/section name
  match_on: [title, publish_date]    # update instead of duplicating
  status_field: "Status"
  status_value: "Ready for copyedit"
  edition_type_field: "Edition Type"
  review_score_field: "Review Score"
  publish_handoff: ""                # optional skill/tool that ships an approved edition
  # The skill always STOPS after staging. A human approves before anything is sent.

# ── Per-edition settings ───────────────────────────────────────
editions:
  news_digest:
    name: "The Weekly Digest"
    day: "Monday"
    send_time: "07:00"
    words: { min: 900, max: 1200 }
    tagline: ""                      # optional line after Key Takeaways
    counts: { takeaways: 5, quick_hits: 4, tools: 3, extra_reads: 1 }
    labels:
      big_story: "THE BIG STORY"
      quick_hits: "QUICK HITS"
      tools: "TOOLS"
      extra_read: "EXTRA READ"
    max_share_single_company: 0.40   # concentration rule

  tutorial:
    name: "The Lesson"
    day: "Tuesday"
    send_time: "07:00"
    words: { min: 1000, max: 1500 }

  tactic:
    name: "The Tactic"
    day: "Wednesday"
    send_time: "07:00"
    words: { min: 350, max: 750 }    # max is a hard cap
    act_within_minutes: 10
    expert_panel: []                 # [] = use the default role-based panel

  deep_dive:
    name: "The Deep Dive"
    day: "Thursday"
    send_time: "07:00"
    words: { min: 2500, max: 4000 }
    exec_summary_words: { min: 220, max: 320 }
    missteps: 4
    key_takeaways: 4
    title_options: 3
    signature_hook: ""               # e.g. "a parallel from the author's own career"

  community:
    name: "Community Newsletter"
    day: ""
    mission_tagline: ""              # italic line under the hero
    hero_image: ""                   # path or URL to your logo; "" to skip
    promo_block:                     # optional ticket/offer callout; enabled: false to skip
      enabled: false
      heading: "Get Your Tickets"
      cta_label: "Register now"
      cta_url: ""
      items: []                      # "**Name — $Price — Date.** Description."
    event_sources: []                # Meetup/Luma/Eventbrite group URLs to pull events from
    event_window_days: 45
    key_links: {}                    # schedule, speakers, register, archive, ...
    sign_off: >
      Thanks for being part of a community that learns together.
    reshare_ask: ""                  # optional closing line for LinkedIn posts
```

## Notes

- **Word counts are defaults.** Change them to fit your format; the review
  rubrics read the numbers from here.
- **Banned words are yours to own.** The defaults catch common AI-sounding
  filler. Add your own; remove any you actually like.
- **Citation rule is not optional.** Whatever `citations.style` you choose,
  every factual claim must carry a source. The skills auto-fail an uncited
  statistic.
- **Staging never sends email.** Each skill stops at `staging.status_value`.
  Sending is a separate, human-approved step.
