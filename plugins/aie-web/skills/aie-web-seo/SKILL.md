---
name: aie-web-seo
description: Audits any website for search-engine optimization (SEO) and answer-engine optimization (AEO). Checks meta tags, heading hierarchy, structured data / JSON-LD schema, internal linking, sitemaps, Core Web Vitals signals, keyword-to-page mapping, content gaps, and how well pages surface in AI answer engines (ChatGPT, Perplexity, Google AI Overviews, Claude). Produces a scored findings report with severity levels and a prioritized fix list. Works on any stack — plain HTML, WordPress, React, Next.js, Vite, Astro, or a hosted builder. Trigger on "check SEO," "audit my site's SEO," "SEO audit," "improve search ranking," "get found on Google," "structured data check," "schema markup audit," "AEO," "answer engine optimization," "will AI cite my site," "featured snippet," "keyword research," or "content gap analysis."
---

# Web SEO & AEO Auditor

Audit a website for both classic search engines (Google, Bing) and modern answer engines (ChatGPT, Perplexity, Google AI Overviews, Claude, Copilot). Produce a scored, actionable report — not vague advice.

## When to use this skill

The user wants to know how findable their site is, why it isn't ranking, whether AI tools will cite it, or what to fix first. This skill is stack-agnostic: it works from a live URL or from source files (HTML templates, React/Next/Vite/Astro components, WordPress themes, etc.).

## Inputs to gather

- One or more **URLs** (or a path to source files).
- Optional: 2-3 **competitor URLs** for benchmarking.
- Optional: the site's **primary keywords / topics** and target audience.
- Optional: local business info if local SEO matters (name, address, phone, service area).

If the user gives only a URL, fetch it and analyze the rendered HTML. Note that fetching sees limited client-side JavaScript — flag that server-rendered or static output is more reliable for this audit.

## Audit procedure

Work through each area below. For the full checkable item lists, read `reference/audit-checklist.md`. For schema and AEO specifics, read `reference/schema-and-aeo.md`.

1. **On-page fundamentals** — title tags (50-60 chars), meta descriptions (150-160 chars), one unique H1, logical H2-H6 order, canonical tags, viewport, Open Graph and Twitter/X card tags, descriptive image alt text, clean URL slugs.
2. **Structured data** — find JSON-LD, validate it, confirm required properties, map each type to the rich result it earns. Details in `reference/schema-and-aeo.md`.
3. **Technical SEO** — robots.txt, XML sitemap, HTTPS, mobile-friendliness, and Core Web Vitals signals (LCP, INP, CLS). Note: INP replaced FID as a Core Web Vital in March 2024 (https://web.dev/blog/inp-cwv-launch).
4. **Crawlability & links** — internal link structure, broken links, orphaned pages, anchor-text quality, redirect chains.
5. **AEO / answer-engine readiness** — direct-answer lead paragraphs, Q&A blocks, comparison tables, step-by-step formats, cited sources, freshness dates, entity clarity, and extractable ~40-60 word definitions. Details in `reference/schema-and-aeo.md`.
6. **Keywords & content gaps** — map keywords to pages, flag cannibalization (one keyword targeted by multiple pages), and list high-value topics with no dedicated page.
7. **Competitor benchmark** (if URLs given) — compare meta quality, schema coverage, content depth, and heading structure; call out gaps.
8. **Local SEO** (if relevant) — LocalBusiness schema, NAP (name/address/phone) consistency on every page, "near me" and city+service phrasing.

## Scoring

Score each category 0-100, then compute a weighted overall score:

```
Overall = MetaTags*0.15 + Headings*0.10 + Schema*0.15 + Technical*0.15
        + AEO*0.15 + Keywords*0.15 + ContentGaps*0.10 + LocalSEO*0.05
```

If local SEO is not relevant, redistribute its weight to Keywords.

- **80-100** Excellent — competitive in the niche.
- **65-79** Good — some optimization needed.
- **50-64** Fair — significant gaps, clear action items.
- **Below 50** Poor — major work recommended.

## Output format

Return one report:

```
SEO & AEO AUDIT — {url}
Date: {date}

OVERALL: {n}/100

CATEGORY SCORES
  Meta tags        {n}/100
  Headings         {n}/100
  Structured data  {n}/100
  Technical SEO    {n}/100
  AEO readiness    {n}/100
  Keywords         {n}/100
  Content gaps     {n}/100
  Local SEO        {n}/100   (or N/A)

TOP QUICK WINS (highest impact, lowest effort)
  1. {fix} — {effort estimate}
  ...

FINDINGS BY SEVERITY
  [Critical] ...   (blocks indexing or rich results)
  [Major]    ...   (meaningful ranking / citation loss)
  [Minor]    ...   (good to fix)
  [Cosmetic] ...   (polish)

PRIORITIZED ACTION PLAN
  This week:  ...
  2-4 weeks:  ...
  Quarterly:  ...
```

Every finding names the exact element, page, or file and the concrete fix. Cite standards where a claim is factual (schema.org type pages, Google Search Central, web.dev). Keep the tone useful and direct — the goal is improvement, not a grade.

## Notes and limits

- A remote URL audit cannot see authenticated pages, server-side code, or a full sitemap crawl — it samples public pages. Say so.
- Do not fabricate search-volume numbers or domain-authority scores. If the user has no keyword-tool data, describe the method and mark estimates clearly as estimates.
- Re-running monthly and tracking category scores over time is the right cadence; offer to save prior scores for comparison.

**Sample run:** `examples/sample-run.md` — a condensed real run showing the exact output this skill produces.
