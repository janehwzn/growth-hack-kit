# Referral landing page

A single-file waitlist + referral page (`index.html`). No build step — it works opened from `file://`, and deploys as-is to GitHub Pages.

## Features

- **Hero** in Astraea's brand (midnight blue + gold + dusty pink, serif headlines)
- **Email capture** → stored in `localStorage` (`ghk_waitlist`); a `mailto:` fallback line is included for real delivery
- **`?ref=` attribution** — visiting `?ref=luna88` increments `luna88`'s invite count
- **Referral link generator** — visitor picks a code, gets a copyable `?ref=<code>` link
- **Leaderboard** — rendered from `localStorage` (`ghk_board`), seeded with demo entries on first visit

## Deploy (GitHub Pages)

1. Push this repo, go to **Settings → Pages → Deploy from a branch**, pick `main` and `/landing/waitlist-referral`
2. Your page is live at `https://<user>.github.io/growth-hack-kit/`
3. Share per-channel links: `?ref=xiaohongshu`, `?ref=tiktok`, `?ref=producthunt` — attribution is automatic

## Tracking model

```
visitor clicks ?ref=CODE  →  localStorage ghk_board[CODE] += 1
visitor joins waitlist    →  localStorage ghk_waitlist += email
```

Every invite is attributed to exactly one code (last-click). For production, replace the `DB` object with `fetch()` calls to a tiny backend (Cloudflare Worker + KV, or Supabase) and point the email form at your provider (Resend, Loops, etc.). The `?ref=` contract stays the same, so playbooks and `analytics/tracker.csv` don't change.

## Theming for your product

Search `index.html` for the CSS variables (`--night`, `--gold`, `--pink`) and the brand strings (`Astraea`, `星缘`, `The star-maiden reads your fate.`) — swap them for your product's palette and copy. The referral mechanics are product-agnostic.
