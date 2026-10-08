# Metrics that matter (zero-budget edition)

## K-factor (viral coefficient)

The single number this kit optimizes. **K = i × c** where:

- **i** = average invites sent per user (share cards posted, referral links clicked)
- **c** = conversion rate of invites → new users

| K | Meaning |
|---|---|
| < 0.2 | No viral loop — you're doing content marketing, that's fine, name it |
| 0.2–0.5 | Loop exists, optimize the share moment (better cards, better timing) |
| 0.5–1.0 | Strong — every 2 users bring ~1 more; paid acquisition now has leverage |
| > 1.0 | True virality — rare, usually launch-week only; enjoy and capture emails |

**How to measure with zero budget:** your landing page's `?ref=` attribution. `i` ≈ referral-link clicks ÷ waitlist signups; `c` ≈ signups from `?ref=` ÷ referral-link clicks. Log both in `tracker.csv` weekly.

## AARRR (pirate metrics)

| Stage | What it means here | Zero-budget tracking |
|---|---|---|
| **Acquisition** | Someone arrives | `?ref=` channel splits on the landing page |
| **Activation** | They join the waitlist / try the demo | Waitlist count, demo sessions |
| **Retention** | They come back | Weekly returning visitors (Plausible/Umami free tier) |
| **Revenue** | They pay | Stripe dashboard (later) |
| **Referral** | They invite others | `?ref=` invites per user → feeds K-factor |

For a pre-launch product, only **Acquisition → Activation → Referral** matter. Don't instrument the rest early.

## CAC (customer acquisition cost)

**CAC = total spend ÷ new users.** With zero ad spend, your spend is *time*: `hours × your hourly value ÷ new users`. If a 小红书 note takes 1 hour and brings 50 signups, that's your baseline. Any paid test must beat it.

## Rules

1. One north-star metric per product (Astraea: K-factor). Everything else is diagnostic
2. Weekly cadence — daily numbers are noise
3. Kill criteria beat hope: define them in your launch plan (see `products/astraea/launch-plan.md`), then honor them
