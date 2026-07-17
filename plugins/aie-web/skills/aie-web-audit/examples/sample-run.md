# Sample run — aie-web-audit

Condensed report from a run against a demo site (a small consulting firm; domain fictionalized to `brightpath.example`). The scores, findings, and handoffs show the exact output shape of a live run.

```
WEBSITE HEALTH AUDIT — brightpath.example
Date: 2026-07-14

OVERALL HEALTH: 64/100

CATEGORY SCORES
  SEO & AEO   58/100
  Copy        71/100
  UX          68/100
  Security    60/100

TOP QUICK WINS (high impact, low effort)
  1. Add meta descriptions to the 6 pages missing them — ~30 min
  2. Compress the 2.8 MB homepage hero image and set width/height — ~15 min
  3. Add HSTS and X-Content-Type-Options headers at the host config — ~15 min
  4. Rewrite the homepage H1 from "Welcome" to the actual value proposition — ~20 min
  5. Fix the footer's http:// logo reference (mixed content) — ~5 min

FINDINGS BY SEVERITY
  [Critical] Mixed content: /about loads an http:// tracking script on an https page
  [Major]    No JSON-LD anywhere — Organization + Service schema missing sitewide
  [Major]    Homepage H1 is "Welcome to BrightPath" — says nothing a stranger can use
  [Major]    Mobile nav overlaps the CTA button at 375px
  [Minor]    5 images missing alt text (team page)
  [Cosmetic] Inconsistent button styles between /services and /contact

WHAT'S NEXT
  Schema + meta depth        → run aie-web-seo
  Hero image + LCP (3.9s)    → run aie-web-performance
  Headers + mixed content    → run aie-web-security
  Pre-relaunch check         → run aie-web-qa
```

62–64/100 is a solid base — the five quick wins above are an afternoon of work and would likely push the site past 75.
