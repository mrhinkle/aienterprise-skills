# Form Delivery Providers

Pick the pattern that matches the user's stack. These are examples — the wiring generalizes to any comparable service.

## Pattern A — Server function + email API

Use when you want control over validation, spam checks, and email templates, and you have somewhere to run a server function (serverless function, edge function, Node/Python/PHP backend).

**How it wires:**
1. The form POSTs to your own endpoint (e.g., `/api/contact`).
2. The endpoint validates input, checks the honeypot, then calls the email API to send a notification (and optionally an auto-reply).
3. The API key lives in a server environment variable, never in the browser.

**Examples of email-sending APIs:** transactional email services such as Resend, Postmark, SendGrid, Mailgun, or Amazon SES. All expose a "send email" call with `from`, `to`, `subject`, and `html`/`text`. Swap the SDK import and the send call; the surrounding handler stays the same. See `serverless-example.md`.

**Domain setup:** most require verifying your sending domain (SPF/DKIM/DMARC records) before mail lands reliably. Do this before going live.

## Pattern B — Hosted form backend (no server code)

Use when you don't want to run any backend. The provider gives you an endpoint URL.

**How it wires:**
1. Set the form `action` to the provider endpoint and `method="post"`.
2. Give each field a `name`.
3. The provider emails you the submission and/or fires a webhook. Configure a redirect or use their AJAX mode for a custom success message.

**Examples:** form-to-email/webhook services such as Formspree, Basin, Formcarry, or Web3Forms. Some support a honeypot and spam filtering as built-in options — enable them.

```html
<form action="https://provider.example/f/your-id" method="post">
  <label>Email <input type="email" name="email" required></label>
  <label>Message <textarea name="message" required></textarea></label>
  <input type="text" name="_honey" style="display:none" tabindex="-1" aria-hidden="true">
  <button type="submit">Send</button>
</form>
```

## Pattern C — Embedded newsletter signup

Use for email-list growth. The email marketing platform handles capture, double opt-in, and consent — no wiring needed beyond the embed.

**How it wires:**
1. Create the list/audience in the platform.
2. Copy its embed snippet (inline form or iframe) into your page.
3. The platform owns validation, storage, and compliance.

**Examples:** email marketing platforms such as Mailchimp, ConvertKit/Kit, Buttondown, Beehiiv, or Substack. Prefer the platform's native embed over rebuilding the signup yourself so you inherit their consent and deliverability handling.

```html
<!-- Newsletter embed placeholder — replace with your platform's snippet -->
<iframe src="https://platform.example/embed?list=YOUR_LIST_ID"
        style="border:0;width:100%;height:220px" title="Newsletter signup"></iframe>
```

## Choosing

- No backend and simplest path → Pattern B.
- Full control over templates/validation → Pattern A.
- Growing an email list → Pattern C (can coexist with A or B for the contact form).
