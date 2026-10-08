# Programmatic SEO Playbook

> Best for: compounding long-tail traffic. Slow to start (3–6 months), then it runs while you sleep. Perfect for astrology: the query space is enormous and templatable.

## The insight

People search hyper-specific questions: "moon in Pisces love compatibility", "八字 日主 丙火 配偶", "what does Venus in Scorpio mean for relationships". Each query is low volume; together they're a river. One template × 1,000 combinations = 1,000 pages.

## Page templates (Astraea examples)

1. **Synastry pages:** `{planet} in {sign} love compatibility` — 12 planets × 12 signs = 144 pages
2. **Bazi pages:** `{日主} {十神} 婚姻` / `{日主} 另一半特征` — 10 day-masters × topics
3. **MBTI × astrology:** `{MBTI type} + {sun sign} love match` — 16 × 12 = 192 combos
4. **Tarot card meanings:** `{card} in love readings` — 78 cards

Each page: 300–600 words of *real* interpretation (your deterministic engine can generate the data; write the prose once per template with variable slots), one share-card image, internal links to 5+ sibling pages, FAQ schema.

## Build rules

- **Template + data, not spun garbage:** every page must answer its query genuinely. Thin pages get deindexed; useful pages rank
- **One template, many rows:** keep templates in version control; generate pages from structured data (sign meanings, element interactions)
- **Internal linking:** every page links to related combos — this is what makes programmatic SEO compound
- **Start with 20 pages,** measure for 60 days, then scale to 200+. Don't publish 1,000 untested pages day one
- **Bilingual:** EN pages for `astraea.app/synastry/...`, ZH pages for `.../bazi/...` — separate sitemaps

## Do / Don't

✅ Unique intro paragraph per page (even templated sites need this);
✅ Core Web Vitals green, mobile-first (your audience is on phones);
✅ submit sitemap to Search Console, watch indexation rate;
❌ auto-generated gibberish / keyword stuffing — Google's helpful-content system kills it;
❌ buying spammy backlinks — one good link (e.g. from your Show HN) beats 100 bad ones

## Metrics → `analytics/tracker.csv`

Pages indexed, avg position, organic clicks/week, signup conversion from organic. Target: 100 clicks/day by month 6, compounding.
