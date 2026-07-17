# Sample run — aie-web-links

Condensed link-check report for the demo site (`brightpath.example`, fictionalized). Output shape matches a live run.

**Summary**
- Links checked: 412 (208 internal / 121 external / 83 assets)
- Broken: 7 • Redirect chains: 2 • Mixed content: 1 • Orphans: 3
- Quick wins (fix in under 5 min): 5

**Findings**

| Severity | Source page | Link / target | Status | Fix |
|----------|-------------|---------------|--------|-----|
| Critical | /about | http://cdn.brightpath.example/logo.png | mixed | change to https:// |
| Critical | /services | /services/strategy-consulting | 404 | page renamed → update link to /services/strategy or 301 |
| High | /blog/ops-metrics | https://partner-site.example/report | 404 | destination gone — replace or remove |
| High | footer (all pages) | mailto:hello@brightpath,example | malformed | fix comma → hello@brightpath.example |
| High | / | /resources → /library → /resources-hub | chain | point link straight at /resources-hub |
| Medium | /team | #advisors (no matching id) | anchor | add id="advisors" to the section |
| Medium | — | /case-studies/nw-2023 (0 inbound links) | orphan | link from /case-studies index or redirect |
| Low | /blog/tools-we-use | https://vendor.example/old-docs | 301 | works; update to final URL when convenient |

**Could not verify (not counted as broken):** 4 external links returned 403 — the destinations block automated checks (linkedin.com profile links among them). Check manually.

**Redirect map (for the renamed service pages):**

```
/services/strategy-consulting  →  /services/strategy   301
/library                       →  /resources-hub       301
```

Re-run scheduled monthly; the two criticals were fixed and re-verified in the same session.
