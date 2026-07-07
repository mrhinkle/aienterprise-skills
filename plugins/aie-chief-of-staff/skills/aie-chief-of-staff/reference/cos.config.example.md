# cos.config.md — annotated example

Copy this to `cos.config.md` in your working directory and edit. Delete any field to fall back to defaults. This is what makes the brief *yours* — the more you fill in, especially `industry`, `competitors`, and `vips`, the sharper it gets.

```yaml
# --- WHO ---
name: "Your Name"
role: "Your title / what you own"
timezone: "America/New_York"
working_hours: "8:00-18:00"          # used to find focus blocks and flag over-full days

# --- INDUSTRY SCAN ---
industry: "the space you operate in"  # e.g. "enterprise AI / B2B media"
keywords:                             # topics to watch in the news scan
  - "AI agents"
  - "enterprise adoption"
  - "AI governance"
competitors:                          # tracked by name + optional domain/handle
  - name: "Competitor A"
    domain: "competitora.com"
    handle: "@competitora"
  - name: "Competitor B"
    domain: "competitorb.com"
company: "Your company / brand"       # also scanned for mentions & reputation
news_sources:                         # preferred outlets to weight first (optional)
  - "techcrunch.com"
  - "theinformation.com"
news:
  lookback: "48h"                     # how far back the news scan reaches
  max_items: 8

# --- INBOX ---
vips:                                 # senders whose mail jumps the queue
  - "boss@company.com"
  - "biggestclient@client.com"
  - "cofounder@company.com"
email_scope:
  folders: ["inbox"]                  # labels/folders to scan
  lookback: "72h"
ignore:                               # skip these unless clearly material
  - "no-reply@"
  - "notifications@"
  - "newsletter senders you already read"

# --- CALENDAR ---
calendars: ["primary"]               # which calendars to include
output:
  lookahead: 1                        # days beyond today to preview (0 = today only)
  length: "standard"                  # brief | standard | detailed
  save_to: ""                         # optional file path to also write the brief
  email_to_self: false                # if true, DRAFT (never send) a self-email

# --- PRIORITIES (weights everything) ---
priorities:                           # current goals/projects; brief leans toward these
  - "Ship Q3 launch"
  - "Close the Acme deal"

# --- TOOLS ---
connectors:                           # let the skill know what to use; auto-detects if omitted
  email: "auto"                       # gmail | outlook | ms365 | auto
  calendar: "auto"                    # google | outlook | auto
```

## Filled example (for reference)

```yaml
name: "Jordan Lee"
role: "VP Product, mid-market SaaS"
timezone: "America/Chicago"
working_hours: "8:30-17:30"
industry: "vertical SaaS for logistics"
keywords: ["freight tech", "supply chain AI", "TMS platforms"]
competitors:
  - { name: "FreightIQ", domain: "freightiq.com" }
  - { name: "HaulPilot", domain: "haulpilot.io" }
company: "ShipLoop"
vips: ["ceo@shiploop.com", "head-of-sales@shiploop.com"]
priorities: ["Launch carrier-scorecard v2", "Renew Northwind account"]
```

## Notes
- With **no config**, defaults apply: today's calendar, primary inbox over the last 72h, a generic industry scan (weaker — set `industry` and `competitors`), and a standard-length brief.
- Keep `vips` current — it's the single highest-leverage field for inbox triage.
- `competitors` drives the most useful part of the news scan. Add domains/handles so the search can target them precisely.
- Nothing here authorizes sending or deleting. `email_to_self` and drafted replies are always drafts you approve.
