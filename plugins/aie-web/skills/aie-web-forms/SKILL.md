---
name: aie-web-forms
description: Wire up HTML/JSX web forms so they actually work — connect a contact, inquiry, or newsletter form to a delivery provider, add client- and server-side validation, spam protection (honeypot and rate limiting), accessible labels and error messages, loading states, and clear success/error feedback. Provider-agnostic: shows email-delivery, form-backend, and newsletter providers as swappable examples. Also audits existing forms for broken submission, missing validation, or accessibility gaps. Trigger on "wire up my form," "connect my contact form," "my form doesn't submit," "audit my forms," "add form validation," "add spam protection to my form," "hook up newsletter signup," "make my form accessible," or "add a honeypot."
---

# Web Form Wiring

Turns a static form into a working one: submission goes somewhere, input is validated, spam is filtered, the form is accessible, and the user sees success or error feedback. Provider-agnostic — swap in whatever email/form/newsletter service the user already uses.

## Workflow

1. **Inventory the forms** — scan the HTML/JSX for `<form>` elements and fields. Identify each form's job (contact, inquiry/partnership, newsletter signup) and note missing `name`, `label`, or `required` attributes.
2. **Pick the delivery path** — confirm which provider the user wants. See `reference/providers.md` for common options and how each is wired. Three patterns cover almost everything:
   - **Server function + email API** (e.g., an email-sending API) — full control over validation and templates.
   - **Hosted form backend** (e.g., a form-to-email/webhook service) — set the form `action` to the provider endpoint; no server code.
   - **Embedded newsletter widget** (e.g., an email marketing platform) — drop in the provider's embed/iframe; the platform handles capture and consent.
3. **Wire the submission** — build the endpoint or point the form at the provider. See `reference/serverless-example.md` for a provider-agnostic server handler with validation, honeypot, and templated notifications.
4. **Add validation** — required-field and email/phone format checks on the client for fast feedback, re-validated on the server (client checks are a UX nicety, not security).
5. **Add spam protection** — a honeypot field (see below) at minimum; rate limiting on the endpoint for anything public.
6. **Make it accessible** — see `reference/accessibility.md`. Every input needs a real `<label>`; errors must be announced, not just colored.
7. **Add feedback states** — a loading state on the submit button, a success message, and an error message that tells the user what to do next.
8. **Document config** — list required environment variables in a `.env.example` and give host setup steps. Never commit real secrets.
9. **Test** — validation fires, honeypot rejects filled submissions, success and error paths both render, and a real submission is received end to end.

## Honeypot (minimum spam protection)

A hidden field bots fill and humans never see. Reject any submission where it's non-empty. Hide with CSS, not just `type="hidden"` (some bots skip hidden inputs), and mark it `aria-hidden` + `tabindex="-1"` so assistive tech and keyboard users skip it.

```html
<div style="position:absolute;left:-9999px" aria-hidden="true">
  <label>Leave this field empty
    <input type="text" name="company_website" tabindex="-1" autocomplete="off">
  </label>
</div>
```

```js
// server side
if (body.company_website) return respond(400, "Rejected");
```

## Validation essentials

- **Required**: reject empty required fields.
- **Email**: match a reasonable pattern (don't over-engineer the regex) and rely on the provider's bounce handling.
- **Phone**: optional, loose format check.
- Always re-check on the server — never trust the client.

## Output Format

When wiring: list the files created/changed, the env vars needed, the provider setup steps, and a test checklist.

When auditing existing forms, report findings by severity:
- **Critical** — form doesn't submit, submits nowhere, or ships a secret to the browser.
- **High** — no server-side validation, no spam protection, no error state shown to users.
- **Medium** — missing labels/accessible errors, no loading state, weak client validation.
- **Low** — copy/UX polish (button label, success wording).

## Reference

- `reference/providers.md` — common email, form-backend, and newsletter providers and how to wire each.
- `reference/serverless-example.md` — provider-agnostic server handler (validation + honeypot + templates + env vars).
- `reference/accessibility.md` — labels, error announcement, focus, and WCAG pointers.

## Standards

- MDN client-side form validation — https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation
- WCAG 2.2 (labels, errors, input purpose) — https://www.w3.org/WAI/WCAG22/quickref/
- OWASP input validation cheat sheet — https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
