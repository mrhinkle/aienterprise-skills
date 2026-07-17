# Sample run — aie-web-qa

Condensed post-update QA report against the demo site's staging environment (`staging.brightpath.example`, fictionalized). Output shape matches a live run.

```
QA TEST REPORT
Site: staging.brightpath.example    Date: 2026-07-14    Environment: staging

OVERALL: PASS WITH KNOWN ISSUES

ISSUES FOUND
  1. Contact form accepts submission but no email arrives
     Severity: Critical
     Location: /contact
     Steps to reproduce: fill all fields with valid data → Submit → success
       message shows → inbox (test address) empty after 15 min
     Expected: notification email delivered
     Actual: silent delivery failure; network tab shows the POST returning 200
       but the provider dashboard logs a domain-verification error
     Fix: verify the sending domain (SPF/DKIM) at the email provider; re-test
       end to end with a real inbox

  2. Mobile menu doesn't close after navigation
     Severity: Major
     Location: all pages at ≤768px
     Steps to reproduce: open menu → tap "Services" → new page loads with the
       menu still covering content
     Expected: menu closes on navigation
     Actual: overlay persists until manually closed
     Fix: close the menu on route change / link click

  3. Console 404 for /js/legacy-carousel.js on the homepage
     Severity: Minor
     Location: /
     Fix: remove the stale script tag (carousel was deleted in the redesign)

TESTS PASSED
  ✓ 11/11 pages render clean at 320/768/1024/1440px
  ✓ Navigation: all 34 internal links resolve; back button and 404 page OK
  ✓ Cross-browser: Chrome, Firefox, Safari (WebKit) — no layout breaks
  ✓ HTTPS everywhere; certificate valid; no mixed content
  ✓ Performance smoke: LCP 2.3s on emulated 4G

REGRESSION (post-update)
  Previously failed: newsletter signup double-submit → Result: FIXED

RECOMMENDATION
  Hold until issue 1 is fixed and re-tested (the contact form is the site's
  only lead channel). Blockers remaining: 0; criticals: 1; est. fix time: ~1 hr.
```
