# Astraea — 30-Day Launch Plan

Goal: 5,000 waitlist signups + 500 referral-driven invites in 30 days, zero ad spend.
North-star metric: **K-factor ≥ 0.4** by day 30 (see `analytics/metrics.md`).

## Week 0 — Prep (days -7–0)

- [ ] Create accounts: 小红书， TikTok, Instagram, X (handle: `@astraea` or `@astraea_app`, fallback documented)
- [ ] Deploy `landing/waitlist-referral/` to GitHub Pages; test `?ref=` flow end-to-end
- [ ] Generate 20 seed drafts: `python3 content/pipeline.py --product astraea` and curate the best
- [ ] Design 5 share-card screenshots (the actual product cards, not mockups)
- [ ] Write the Product Hunt tagline (≤60 chars) + first comment (maker's story)
- [ ] Set up `analytics/tracker.csv` baseline row (all zeros)

## Week 1 — Seed content + community (days 1–7)

| Channel | Cadence | Tactic |
|---|---|---|
| 小红书 | 1 note/day | 玄学干货 + 产品截图；标题公式："月亮XX座的女生，逃不过这3种恋爱"；评论区每条必回，置顶"合盘卡片领取方式" |
| TikTok/IG | 3 Reels | Screen-record a love-tarot reading; trending audio; caption = hook + "link in bio" |
| Reddit | 2 value posts | r/astrology: "I built a tool that combines bazi + western astrology — roast my chart logic" (ask, don't pitch) |
| X | 1 thread | Build-in-public: "I built an AI fortune app with zero-token deterministic astrology engine 🧵" |

Target end of week 1: 500 waitlist signups, 3 notes with >1k views.

## Week 2 — Referral ignition (days 8–14)

- Turn on the referral leaderboard; announce "top 10 referrers get lifetime Pro"
- 小红书： launch the "闺蜜合盘挑战" — post your couple compatibility card, @ your bestie
- TikTok: duet/stitch bait — "POV: the app said you're 94% compatible and now you're texting him"
- X: daily mini-readings ("Venus in Scorpio today — text your ex? No. Here's why")
- First K-factor reading in `analytics/tracker.csv`

Target: 1,500 cumulative signups, K-factor ≥ 0.25.

## Week 3 — Product Hunt launch (days 15–21)

- **Tuesday 00:01 PT** launch (best window); hunter outreach done in week 2
- Launch-day war room: reply to every comment within 1 hour; post to X/IG/小红书 "we're live on PH"
- Ship one small feature during launch week ("by popular demand: rising-sign cards") for the update narrative
- HN `Show HN` the week *after* PH (don't split the spike) — angle: deterministic astrology engine, zero-token interpretations

Target: top-5 of the day on PH, 3,000 cumulative signups.

## Week 4 — Double down + SEO seeds (days 22–30)

- Analyze tracker: kill bottom-50% content formats, 2x the top formats
- Publish first 20 programmatic SEO pages ("Moon in Pisces love compatibility", "八字合婚怎么看" etc. per `playbooks/seo-programmatic.md`)
- 小红书： start a weekly column ("每周星缘合盘") for retention
- Email the waitlist: referral leaderboard update + launch date announcement

Target: 5,000 signups, 500 referral invites, K-factor ≥ 0.4, 3 organic search clicks/day (early signal).

## Success metrics (log weekly in `analytics/tracker.csv`)

| Metric | Day 7 | Day 14 | Day 21 | Day 30 |
|---|---|---|---|---|
| Waitlist signups (cumulative) | 500 | 1,500 | 3,000 | 5,000 |
| Referral invites | 50 | 150 | 300 | 500 |
| K-factor | — | ≥0.25 | ≥0.3 | ≥0.4 |
| 小红书 followers | 200 | 600 | 1,200 | 2,500 |
| TikTok/IG followers | 100 | 400 | 1,000 | 2,000 |
| PH rank | — | — | top 5 day | — |

## Kill criteria

If by day 14 K-factor < 0.15 **and** no single post >5k views: pause paid-consideration, run 5 user interviews, rewrite key messages (pillar 3 "made to be shared" is the prime suspect).
