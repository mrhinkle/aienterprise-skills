# Server Handler Example (provider-agnostic)

A POST-only endpoint that validates input, rejects honeypot hits, and sends a notification via an email API. Replace `sendEmail` with your provider's SDK call — the structure is the same for Resend, Postmark, SendGrid, Mailgun, SES, etc.

```js
// api/contact.js  (adapt to your runtime's handler signature)

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const { name = "", email = "", subject = "", message = "", company_website = "" } = req.body || {};

  // 1. Honeypot: real users never fill this
  if (company_website) return res.status(400).json({ error: "Rejected" });

  // 2. Server-side validation (never trust the client)
  if (!name.trim() || !message.trim()) {
    return res.status(422).json({ error: "Name and message are required." });
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return res.status(422).json({ error: "Please enter a valid email." });
  }

  try {
    // 3. Send notification — swap this call for your provider's SDK
    await sendEmail({
      from: process.env.FROM_EMAIL,          // verified sender
      to: process.env.TO_EMAIL,              // where submissions go
      replyTo: email,
      subject: `New message: ${subject || "Contact form"}`,
      text: `From: ${name} <${email}>\n\n${message}`,
    });

    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error("Send failed:", err);
    return res.status(500).json({ error: "Could not send. Please try again." });
  }
}
```

## Client submit handler

```js
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const btn = form.querySelector("[type=submit]");
  btn.disabled = true; btn.textContent = "Sending…";

  const res = await fetch("/api/contact", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(Object.fromEntries(new FormData(form))),
  });

  btn.disabled = false; btn.textContent = "Send";
  const data = await res.json().catch(() => ({}));

  if (res.ok) {
    showStatus("success", "Message sent — we'll get back to you soon.");
    form.reset();
  } else {
    showStatus("error", data.error || "Something went wrong. Please try again.");
  }
});
```

`showStatus` should write to a container with `role="status"` (success) or `role="alert"` (error) so screen readers announce it — see `accessibility.md`.

## .env.example

```
FROM_EMAIL=noreply@yourdomain.com
TO_EMAIL=hello@yourdomain.com
EMAIL_API_KEY=replace-me           # set in your host's env vars, never commit
```

## Optional: rate limiting

For public endpoints, cap submissions per IP (e.g., 5 per hour) using a KV store, the provider's limits, or edge middleware. Reject with 429 when exceeded.
