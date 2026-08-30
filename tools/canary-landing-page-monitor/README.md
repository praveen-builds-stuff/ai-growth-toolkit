# Canary — Landing Page Monitor

Synthetic monitoring for paid landing pages: checks links, CTAs, and embedded forms daily,
emails a report. Built with Playwright, GitHub Actions, and Resend.

No company-specific data in this repo — replace the placeholder URLs in `config.js` and the
environment variables in `.env.example` before use.

## Architecture

- `config.js` — list of page URLs to monitor
- `adMonitor.js` — lightweight check: hits every URL in parallel, flags non-200/timeout (runs in seconds)
- `monitor.js` — deep check: links, CTA buttons, embedded form iframes, modal forms, CTA destination pages
- `emailReport.js` — builds and sends the HTML report
- `.github/workflows/daily-monitor.yml` — runs both checks on a daily schedule

## Design notes worth keeping if you rebuild this

- **Stealth mode is necessary** for any page using HubSpot (or similar) embedded forms —
  headless Chromium gets detected and blocked, so the browser context needs a real
  user-agent and automation-detection flags disabled.
- **Script-present ≠ form-visible.** Checking for the embed script/container tells you the form
  is *configured*, not that it *renders*. Wait for actual field elements to appear before marking
  a form healthy — this is the difference between a real check and a false sense of security.

## Setup

1. `npm install playwright resend dotenv`
2. Fill in `config.js` with your actual landing page URLs
3. Get a Resend API key (resend.com), add it plus `FROM_EMAIL`/`TO_EMAIL` to `.env` locally and as GitHub Secrets
4. Test locally: `node monitor.js`
5. Push to GitHub — the workflow runs automatically on schedule, or trigger manually from the Actions tab
