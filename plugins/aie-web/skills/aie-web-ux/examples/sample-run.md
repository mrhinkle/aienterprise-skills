# Sample run — aie-web-ux

Condensed UX review of the demo site (`brightpath.example`, fictionalized). Audience given: operations leads at mid-size firms evaluating a consulting engagement.

## 1. Overall

**66/100 — usable but leaky: visitors can find the services, but the path from "interested" to "contacted" has real friction, especially on mobile.**

## 2. Top 3 friction points

1. **The primary CTA disappears on mobile.** "Book a consultation" is a header button on desktop; at phone widths it's inside the hamburger menu. The one action the site exists for requires two taps to even see.
2. **The services pages don't answer "why you."** Each lists what BrightPath does, but no proof — no client names, results, or credentials until the buried /case-studies page. A skeptical visitor has no reason to pick them over the next tab.
3. **The contact form asks for too much, too soon.** Nine fields including budget and start date. For a first inquiry, every extra field costs conversions.

## 3. Scorecard

| Category | Score | Notes |
|----------|-------|-------|
| Navigation & structure | 74 | Clear top nav; breadcrumbs missing on case studies |
| Visual hierarchy | 70 | Good desktop; hero text overlaps image at 375px |
| Mobile experience | 52 | CTA hidden; tap targets in footer ~30px |
| Readability | 78 | Good line length; two pages of 14px body text |
| Forms & interaction | 55 | 9-field form; no inline validation feedback |
| Perceived performance | 68 | Hero loads late, pushes content down |
| Error handling | 60 | Generic 404; form errors clear only on resubmit |
| Content quality | 72 | Strong services copy; proof elements buried |
| Design consistency | 75 | Two button styles competing |
| Accessibility & inclusivity | 58 | Focus states missing on nav; contrast fails on footer links |
| **Overall** | **66** | |

## 4. Prioritized fixes

Navigation and mobile first: surface the CTA outside the mobile menu (High); cut the contact form to name/email/message + one optional field (High); add one proof element to each service page (High); fix footer tap targets and contrast (Medium); add focus states (Medium); custom 404 with a path back to services (Low).
