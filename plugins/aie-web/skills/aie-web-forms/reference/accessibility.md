# Accessible Forms

Accessibility is not optional polish — a form that a keyboard or screen-reader user can't complete is a broken form.

## Labels

Every input needs a programmatic label. Use a real `<label>`, associated by wrapping or `for`/`id`.

```html
<label for="email">Email address</label>
<input id="email" name="email" type="email" required autocomplete="email">
```

- Placeholder text is NOT a label — it disappears on input and fails contrast.
- Group related inputs (e.g., radios) in a `<fieldset>` with a `<legend>`.

## Input types and autocomplete

Use the right `type` so mobile shows the correct keyboard and browsers can autofill:

- `type="email"`, `type="tel"`, `type="url"`, `type="number"`.
- Add `autocomplete` tokens (`name`, `email`, `tel`, `organization`) — WCAG 2.2 "Identify Input Purpose".

## Required and error states

- Mark required fields with the `required` attribute AND a visible indicator (not color alone).
- On error, set `aria-invalid="true"` and link the message with `aria-describedby`.
- Errors must say what's wrong and how to fix it: "Enter an email like name@example.com", not just "Invalid".

```html
<input id="email" name="email" type="email" required
       aria-invalid="true" aria-describedby="email-err">
<p id="email-err" class="error">Enter an email like name@example.com</p>
```

## Announcing status

Screen readers won't notice a visual-only success/error banner. Put status text in a live region:

- Success: container with `role="status"` (polite).
- Error summary: container with `role="alert"` (assertive), and move focus to it.

## Keyboard and focus

- Every control reachable and operable by keyboard, in a logical tab order.
- Visible focus indicator on all interactive elements.
- The honeypot field must be `tabindex="-1"` and `aria-hidden="true"` so it's skipped.

## Contrast and sizing

- Text and form borders meet WCAG AA contrast (4.5:1 for text, 3:1 for UI components).
- Touch targets at least 44×44 px.

## Reference

- WCAG 2.2 quick reference — https://www.w3.org/WAI/WCAG22/quickref/
- WAI forms tutorial — https://www.w3.org/WAI/tutorials/forms/
- MDN form validation — https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation
