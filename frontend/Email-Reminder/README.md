# Email Reminder

Plain HTML, CSS and JavaScript. No libraries or build step.

## Files

- index.html: email registration, verification check and Send to Josh.
- welcome.js: logic for index.html.
- reminder.html: instant/later delivery, date/time, message and optional subject.
- reminder.js: logic for reminder.html.
- styles.css: basic black-and-white layout.

## Open

Open index.html in your browser. If your browser blocks session storage for local files, serve this folder with `python -m http.server 8000` and visit http://localhost:8000.

## Add your API calls

Search for TODO in the JavaScript files:

1. welcome.js / requestEmailVerification(email): request an SES verification email through your backend.
2. welcome.js / checkEmailVerification(email): return true only when your backend confirms verification.
3. reminder.js / submitReminder(reminder): send the form values to your backend.

These functions deliberately report "not connected yet" until implemented. They do not simulate successful verification or sending. You can use Send to Josh to view the reminder form before connecting the APIs.

The suggested payload is documented inside submitReminder. Adapt it to your existing API. The author address and default subject belong in backend configuration. Never put AWS credentials in these frontend files. Session storage is only a way to pass the selected recipient between pages; the backend must enforce verification and validate incoming requests independently.
