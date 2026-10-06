---
name: aie-web-links
description: Crawl a website and validate every internal link, external link, image, and asset reference — flagging broken links (404/410/5xx), mixed content (HTTP assets on HTTPS pages), redirect chains, orphaned pages, broken in-page anchor links, and malformed mailto:/tel: links. Produces a fix-it report grouped by severity with the exact page, URL, status code, and recommended fix. Works from a source folder or a live/staging URL, on any stack. Trigger on "check my links," "broken links," "link checker," "find dead links," "audit my links," "check for mixed content," "find redirect chains," "orphaned pages," "are my links working," or "validate links before launch."
---

# Website Link Checker

Crawls a site and validates links, images, and assets, then reports what's broken and how to fix it. Broken links hurt user trust and SEO; this catches them before visitors do.

## Workflow

1. **Confirm the source** — a local build/source folder OR a publicly reachable URL (production or staging). Note any auth or robots.txt restrictions; report links that can't be reached rather than guessing.
2. **Build the link inventory** — parse pages for `<a href>`, `<img src>`, `<link href>`, `<script src>`, media/`srcset`, `mailto:`, `tel:`, and in-page `#anchor` targets. Note where each link lives (source page + line).
3. **Validate each link** (see `reference/status-codes.md` for how to interpret responses):
   - Internal links resolve to a real page/asset.
   - External links return a healthy status; distinguish broken (404/410/5xx) from merely slow.
   - Images/assets load.
   - No HTTP asset is referenced on an HTTPS page (mixed content).
   - Redirects are single hops, not chains.
   - `#anchor` links point to an element with a matching `id`/`name` on the target page.
   - `mailto:`/`tel:` are well-formed.
4. **Find orphans** — pages that exist but nothing links to them (unreachable by crawl from the homepage).
5. **Report** using the format below. See `reference/fixes.md` for the standard fix for each issue type.

## Practical notes

- Some external sites block automated requests (403) or rate-limit. Report these as "could not verify," not confirmed-broken.
- A 200 with a slow response is a warning, not a break.
- Prefer `HEAD` requests where supported, falling back to `GET`, to reduce load.
- For large sites, cap external-link concurrency and de-duplicate URLs before requesting.

## Output Format

Lead with a summary, then findings grouped by severity.

**Summary**
- Links checked: N (internal / external / assets)
- Broken: N • Redirect chains: N • Mixed content: N • Orphans: N
- Quick wins (fix in under 5 min): N

**Findings** — for each issue:
| Severity | Source page | Link / target | Status | Fix |
|----------|-------------|---------------|--------|-----|

Severity levels:
- **Critical** — broken internal links, mixed content on HTTPS, links to pages returning 5xx, missing images on key pages (home/pricing/CTA).
- **High** — broken external links on high-traffic pages, invalid email links, redirect chains, non-working social links.
- **Medium** — missing images on secondary pages, orphaned pages, broken anchor links, slow-but-working links.
- **Low** — outbound links to deprecated-but-working pages, slow external assets.

If URLs changed, also output a **redirect map** (old URL → new URL → 301/302).

## Reference

- Read `reference/status-codes.md` for the status-code table and what each means.
- Read `reference/fixes.md` for the standard remediation and time estimate per issue type.

## Standards

- Google Search Central on crawling and links — https://developers.google.com/search/docs/crawling-indexing
- MDN Mixed content — https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content
- MDN HTTP redirects — https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections

**Sample run:** `examples/sample-run.md` — a condensed real run showing the exact output this skill produces.
