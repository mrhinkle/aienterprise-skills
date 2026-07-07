# SEO & AEO Audit Checklist

Check each item. Mark Pass / Fail / N-A and note the specific element or page.

## On-page fundamentals

- [ ] `<title>` present, unique per page, 50-60 characters, front-loads the primary term.
- [ ] Meta description present, unique, 150-160 characters, reads as a compelling snippet.
- [ ] Exactly one `<h1>` per page, describing the page.
- [ ] H2-H6 follow a logical order — no skipped levels (H2 then H4), no headings used purely for styling.
- [ ] `<meta charset>` and `<meta name="viewport" content="width=device-width, initial-scale=1">` present.
- [ ] Canonical tag present, self-referential on originals, absolute URL, no canonical chains.
- [ ] Open Graph tags: `og:title`, `og:description`, `og:image`, `og:type`, `og:url`.
- [ ] Twitter/X card tags: `twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`.
- [ ] Every meaningful image has descriptive `alt` text; decorative images use empty `alt=""`.
- [ ] URLs are lowercase, hyphen-separated, descriptive, free of tracking parameters where possible.

## Technical SEO

- [ ] `robots.txt` present and does not accidentally block important paths.
- [ ] XML sitemap present, valid, referenced in robots.txt, lists canonical URLs only.
- [ ] All pages served over HTTPS with a valid certificate; no mixed content.
- [ ] Mobile-friendly: readable without zoom, tap targets spaced (min ~48x48px), responsive images (`srcset`/`<picture>`).
- [ ] Core Web Vitals signals — LCP < 2.5s, INP < 200ms, CLS < 0.1.
  (INP replaced FID as a Core Web Vital in March 2024 — https://web.dev/blog/inp-cwv-launch)
- [ ] `hreflang` present and reciprocal if the site has language/region variants; `x-default` set.

## Crawlability & links

- [ ] Important pages are reachable within ~3 clicks from the homepage.
- [ ] No broken internal or outbound links (404/410).
- [ ] No orphaned pages (pages with zero internal links pointing to them).
- [ ] Anchor text is descriptive, not "click here."
- [ ] Redirects are single-hop (no A -> B -> C chains) and use 301 for permanent moves.

## Keywords & content

- [ ] Each page has a clear primary keyword/topic and 1-2 secondary terms.
- [ ] No cannibalization — the same primary keyword is not targeted by multiple pages.
- [ ] Keyword-to-page map exists (which page owns which query).
- [ ] Content gaps identified: high-value topics/questions with no dedicated page.
- [ ] Prioritize gaps by (relevance x demand x achievability). Do not invent exact volumes without a data source.

## Local SEO (if applicable)

- [ ] `LocalBusiness` (or a subtype) JSON-LD with address, phone, geo, hours.
- [ ] NAP (name, address, phone) identical on every page and matching external listings.
- [ ] City + service and "near me" phrasing used naturally in copy and headings.
- [ ] Service-area or location pages exist where the business serves multiple areas.

## Competitor benchmark (if URLs provided)

For each competitor, compare against the audited site and note the gap:

| Metric | Your site | Competitor | Gap |
|---|---|---|---|
| Meta tag quality | | | |
| Heading structure | | | |
| Schema coverage | | | |
| Content depth | | | |
| Answer-ready formatting | | | |

Ask: which queries do they clearly target that this site does not? Which schema types do they implement? How current is their content?
