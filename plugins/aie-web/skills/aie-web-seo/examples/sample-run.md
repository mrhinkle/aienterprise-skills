# Sample run — aie-web-seo

Condensed report from a run against the same demo site as the aie-web-audit sample (`brightpath.example`, fictionalized). Output shape is exactly what a live run produces.

```
SEO & AEO AUDIT — brightpath.example
Date: 2026-07-14

OVERALL: 58/100

CATEGORY SCORES
  Meta tags        52/100
  Headings         70/100
  Structured data  20/100
  Technical SEO    75/100
  AEO readiness    45/100
  Keywords         60/100
  Content gaps     55/100
  Local SEO        N/A (weight redistributed to Keywords)

TOP QUICK WINS (highest impact, lowest effort)
  1. Add Organization JSON-LD sitewide (name, url, logo, sameAs) — ~30 min
  2. Write meta descriptions for /services, /about + 4 more pages — ~45 min
  3. Add a direct-answer lead paragraph (40-60 words) to the top 3 service pages — ~1 hr
  4. Add visible "last updated" dates to the 8 blog posts — ~20 min

FINDINGS BY SEVERITY
  [Critical] robots.txt blocks /assets/, which contains the CSS — pages render
             unstyled for crawlers (blocks rich-result eligibility)
  [Major]    Zero structured data on any page; competitors both ship Organization
             + Service + FAQPage
  [Major]    /services and /services/consulting both target "operations consulting"
             — cannibalization; consolidate or differentiate
  [Major]    No page answers "what does an operations consultant cost" — highest-
             value gap found in the content map
  [Minor]    Title tags run 70-85 chars on 4 pages — trim to 50-60
  [Minor]    Anchor text "click here" on 9 internal links

PRIORITIZED ACTION PLAN
  This week:  fix robots.txt, add Organization schema, meta descriptions
  2-4 weeks:  merge the cannibalizing pages, add cost/pricing page, AEO leads
  Quarterly:  re-run this audit; track category scores over time
```

Standards cited during the run: schema.org type definitions, Google Search Central structured-data docs, web.dev Core Web Vitals. Estimates were labeled as estimates — no invented search volumes.
