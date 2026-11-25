# Sample run — aie-web-forms

Condensed wiring run: the demo site's static contact form (`brightpath.example`, fictionalized) connected to a serverless handler + email API (Pattern A from `reference/providers.md`).

## What was found (inventory)

One `<form>` on /contact: no `action`, no labels on 2 of 4 fields, no validation, no spam protection, no feedback states. Classic static-template form — looks fine, submits nowhere.

## What was delivered

```
FILES CREATED / CHANGED
  api/contact.js        — POST handler: validation + honeypot + provider send
                          (adapted from reference/serverless-example.md)
  contact.html          — labels wired (for/id), honeypot field added, novalidate
                          removed, status region added (role="status"/"alert")
  js/contact-form.js    — submit handler: loading state, success/error rendering
  .env.example          — FROM_EMAIL, TO_EMAIL, EMAIL_API_KEY (no real values)

ENV VARS NEEDED (set in host dashboard, never committed)
  FROM_EMAIL   verified sender on your domain
  TO_EMAIL     where submissions land
  EMAIL_API_KEY

PROVIDER SETUP
  1. Verify the sending domain (SPF/DKIM records) at the email provider
  2. Create an API key scoped to sending only
  3. Add the three env vars to the production environment

TEST CHECKLIST (all passed)
  ✓ Empty required fields rejected client-side AND server-side (422)
  ✓ Bad email format rejected server-side
  ✓ Honeypot filled → 400, no email sent
  ✓ Submit button disables + shows "Sending…" during the request
  ✓ Success and error states both render and are announced (role=status/alert)
  ✓ End-to-end: real submission delivered to the test inbox
```

## Audit-mode note

Run in audit mode instead, the pre-fix form would have reported: **Critical** (submits nowhere), **High** (no server validation, no spam protection, no error state), **Medium** (2 unlabeled fields, no loading state).
