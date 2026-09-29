# Structured Data & Answer-Engine Optimization

## Structured data (JSON-LD)

Google recommends JSON-LD in a `<script type="application/ld+json">` block. Validate against:
- Schema.org type definitions — https://schema.org
- Google's structured-data documentation — https://developers.google.com/search/docs/appearance/structured-data
- Rich Results Test — https://search.google.com/test/rich-results
- Schema Markup Validator — https://validator.schema.org

### Common types and the rich result they can earn

| Schema type | Eligible result | Key required/recommended properties |
|---|---|---|
| `Organization` / `WebSite` | Knowledge panel and site name. Google removed the sitelinks search box on 2024-11-21; `WebSite` markup for the site name is still valid. | name, url, logo, sameAs |
| `Article` / `BlogPosting` | Article rich result | headline, image, datePublished, author |
| `FAQPage` | Not a Google rich result. Google removed the FAQ rich-result feature and its docs in May 2026. Visible Q&A on the page can still help readers and other answer engines. | mainEntity -> Question -> acceptedAnswer |
| `HowTo` | Not a Google rich result. Google removed HowTo rich results (desktop and mobile) and the docs in September 2023. Keep real numbered steps in the HTML anyway. | name, step |
| `Product` | Price, rating, availability | name, offers, aggregateRating, review |
| `LocalBusiness` | Local pack, map panel | name, address, telephone, geo, openingHours |
| `Event` | Event card | name, startDate, location |
| `Recipe` | Recipe card | name, image, recipeIngredient, recipeInstructions |
| `BreadcrumbList` | Breadcrumb trail in results | itemListElement |

Note: Google has fully dropped HowTo rich results (September 2023) and FAQ rich results (May 2026), and dropped the sitelinks search box (November 2024). Do not promise those treatments. Confirm any other type in current Search Central docs before you tell someone it will earn a rich result. Sources: [HowTo/FAQ changelog](https://developers.google.com/search/updates), [sitelinks search box retirement](https://developers.google.com/search/blog/2024/10/sitelinks-search-box).

### Validation checklist

- [ ] JSON-LD parses with no syntax errors.
- [ ] Required properties for the declared type are present.
- [ ] Recommended properties (image, author, datePublished) included where relevant.
- [ ] Types are nested correctly and use valid data types.
- [ ] Content in the markup matches visible on-page content (no markup-only claims).
- [ ] Passes the Rich Results Test.

## Answer-Engine Optimization (AEO)

Answer engines (ChatGPT, Perplexity, Google AI Overviews, Claude, Copilot) extract and cite passages. Optimize for clean extraction and trust.

### Content patterns that get cited

1. **Direct-answer lead** — the first paragraph answers the page's core question in 40-60 words, before any preamble.
2. **Q&A blocks** — real questions as headings with concise answers directly beneath.
3. **Comparison tables** — labeled columns and rows; models lift these cleanly.
4. **Step-by-step** — numbered `<ol>` steps, one action each, with any prerequisites and time stated.
5. **Definitions** — a crisp, standalone one-to-two sentence definition near the top.
6. **Cited sources** — link claims to primary sources; attribute statistics and quotes.
7. **Freshness signals** — a visible "last updated" date and current facts.

### Entity & authority signals

- [ ] The organization/author is identified consistently (Organization/Person schema, `sameAs` links to authoritative profiles).
- [ ] Author bylines and credentials are present on substantive content.
- [ ] Facts are accurate and internally consistent — answer engines penalize contradictions.
- [ ] Semantic HTML (`<ul>`, `<ol>`, `<table>`, `<dl>`, headings) makes structure machine-readable.

### How to test AEO

- Query the target questions in ChatGPT, Perplexity, Google AI Overviews, and Claude. Does the site appear as a citation? Is the cited passage accurate?
- Check whether the site's key facts are represented correctly when an assistant summarizes the topic.
- Track citation presence over time the way you would track rankings.

Emerging convention: some sites publish an `llms.txt` file at the domain root to guide LLM consumption (https://llmstxt.org). It is not an official standard and adoption varies — treat it as optional and note it, do not require it.
