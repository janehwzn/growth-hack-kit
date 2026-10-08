# Product Profile: Astraea

## Positioning

An AI fortune-telling PWA for women curious about love and relationships — bazi, MBTI, tarot, palmistry, and western astrology in one dreamy, beautiful experience.

- **Name:** Astraea （星缘）
- **Slogan:** "The star-maiden reads your fate."
- **Category:** Lifestyle / Entertainment — AI astrology & fortune-telling
- **Stage:** v0 (play-test build live; App Store launch pending)
- **Links:**
  - Web app / PWA: (placeholder — private repo `janehwzn/astraea`)
  - iOS / Android: (placeholder — pending App Store + APK builds)
  - Instagram / TikTok / 小红书： (placeholder — accounts to be created at launch)

## Audience personas

### Persona 1 — "The astrology girlie" (US/EU, 18–34)

- **Demographics:** Women 18–34, US/Europe, iPhone users, into wellness/spirituality content
- **Hangs out on:** TikTok, Instagram Reels, Pinterest
- **Already follows / uses:** Co–Star, The Pattern, astrology meme pages, tarot readers on TikTok
- **Trigger:** A friend shares a gorgeous compatibility card ("we're 94%?!"); curiosity + aesthetic FOMO

### Persona 2 — 小红书玄学/情感女生 (18–30)

- **Demographics:** 年轻女性，对情感、玄学、MBTI、塔罗感兴趣
- **Hangs out on:** 小红书， 抖音， 微博超话
- **Already follows / uses:** 塔罗占卜博主、情感树洞号、MBTI 话题
- **Trigger:** 一张"星缘"合盘卡片的截图+准到离谱的评论区；闺蜜@她来测

### Persona 3 — Product Hunt / indie audience

- **Demographics:** Indie hackers, designers, AI-curious early adopters (mixed gender, 25–40)
- **Hangs out on:** Product Hunt, Hacker News, X/Twitter
- **Already follows / uses:** AI product launches, "build in public" threads
- **Trigger:** A beautiful launch page + the technical hook (deterministic calendar engine, zero-token interpretations)

## Brand voice

Tone: `dreamy`, `playful`, `mystical` — the pipeline accepts these via `--tone`.

- **Do (EN):** "The stars have been keeping secrets about your love life. Tonight, they talk." / "Your moon sign called — it wants better boundaries."
- **Do （中文）:** "星星今晚有话想对你说，关于他。" / "你的月亮星座，藏着你所有的心软。"
- **Don't:** clinical horoscope jargon with no warmth; bro-y hustle tone; fear-mongering ("WARNING: Mercury retrograde will RUIN you")
- **Don't （中文）:** 生硬的命理术语堆砌；恐吓式营销（"不转不是中国人"式）
- **Languages:** EN primary (US/EU), ZH for 小红书/中文社区
- **Aesthetic anchors:** midnight blue + gold + dusty pink, serif headlines, dreamy feminine — captions should *feel* like the UI looks

## Key messages

1. **All systems, one reading** — bazi （真太阳时 corrected) + sun/moon/rising + MBTI + tarot + palmistry, not just "what's your sign"
2. **Deterministic, not hallucinating** — the calendar/compatibility engine is pure rules, zero tokens; the LLM only writes interpretations
3. **Made to be shared** — every reading ends in a beautiful share card (couple compatibility, love tarot spread)
4. **For her** — designed for women who love romance content, not generic horoscope spam
5. **Private by design** — birth data stays on device (PWA, offline-capable)

## Built-in viral loops

- **Share cards** — every compatibility/tarot result generates a gorgeous card; shared to IG Stories / 小红书 / group chats → new users arrive curious — `live` (v0)
- **Couple compatibility** — requires *two* people's birth info; the second person is a new user by construction — `live` (v0)
- **Referral `?ref=` landing page** — waitlist with referral leaderboard (`landing/waitlist-referral/`) — `live` (this kit)
- **Daily draw / streak** (planned) — "your card of the day" habit loop — `planned`
- **In-app purchase: love crystals store** (planned) — monetization, not viral

## Channels (priority order)

| # | Channel | Why | Playbook |
|---|---------|-----|----------|
| 1 | 小红书 | Persona 2 lives here; 玄学/情感 content has proven virality; screenshots travel | `playbooks/xiaohongshu.md` |
| 2 | TikTok / IG Reels | Persona 1; tarot/astrology is a native format; share cards are Reels-ready | `playbooks/instagram-tiktok.md` |
| 3 | Product Hunt | Launch spike + indie credibility; pretty AI products overperform | `playbooks/product-hunt.md` |
| 4 | Reddit (r/astrology, r/tarot) | High-intent seekers; strict no-spam, value-first only | `playbooks/reddit.md` |
| 5 | X/Twitter | Build-in-public + astro Twitter community | `playbooks/x-twitter.md` |
| 6 | Programmatic SEO | "moon in X + love compatibility" long-tail pages | `playbooks/seo-programmatic.md` |

## Notes

- Competitors: Co–Star, The Pattern, Sanctuary, various 八字/塔罗 mini-programs. Differentiation: multi-system (East + West) in one reading, deterministic engine, share-card-first design, bilingual EN/中文 dual brand.
- Pricing: v0 free; v1 adds palmistry, payments, real AI interpretations; crystal store for monetization.
- Risks: app-store review for "fortune-telling" category (frame as entertainment); trademark check still needed before launch (USPTO/CNIPA).
