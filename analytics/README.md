# Analytics

Measure what matters, with zero budget. Two files:

- **[metrics.md](metrics.md)** — definitions that actually get used here: K-factor, AARRR, CAC, plus how to track each without paid tools
- **[tracker.csv](tracker.csv)** — the weekly log. One row per week per product. Fill it every Monday; the formulas in metrics.md read off it

## The weekly ritual (15 min)

1. Pull numbers: landing page `?ref=` splits (from your backend or the localStorage demo), social analytics, waitlist count
2. Append one row to `tracker.csv`
3. Compute K-factor for the week (formula in metrics.md)
4. One-line retro in the `notes` column: what worked, what to kill, what to 2x

No dashboard needed until the CSV has 8+ weeks of rows. The CSV *is* the dashboard.
