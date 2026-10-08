# Contributing to Growth Hack Kit

Thanks for making this more robust. This repo grows through real playbooks, templates, and product profiles from people actually shipping. Here's how to add yours.

## What to contribute

1. **A product profile** — `products/<your-product>/PROFILE.md` (+ optional `launch-plan.md`)
2. **A platform playbook** — `playbooks/<platform>.md`
3. **A content template** — `content/templates/<platform>.txt`
4. **Pipeline improvements** — `content/pipeline.py` (keep stdlib + pyyaml only)
5. **Real data** — anonymized rows in `analytics/tracker.csv` showing what actually worked

## How to add a product profile

```bash
cp -r products/_template products/myproduct
```

Then fill in every section of `products/myproduct/PROFILE.md`. A good profile has:

- Positioning in **one sentence** (who it's for + what it does + why now)
- 2–3 concrete audience personas (age, platform, what they already follow)
- Brand voice with **do/don't examples** — this is what the pipeline's `--tone` flag reads
- Built-in viral loops (share cards, referral, UGC mechanics — be honest about what exists vs. planned)
- Links section; mark anything not-yet-live as `(placeholder)`

Optionally add `products/myproduct/launch-plan.md`: a 30-day, week-by-week plan with channels, cadence, and numeric targets (see `products/astraea/launch-plan.md` for the format).

## How to add a playbook

One markdown file per platform: `playbooks/<platform>.md`. Every playbook must include:

- **Who it's for** (which products/audiences this channel fits)
- **Setup** (account, bio link, any tooling)
- **Tactics** — concrete, ordered, with example hooks (not "post good content")
- **Do / Don't** — especially spam and compliance boundaries
- **Cadence** — posts per day/week, best times with timezone
- **Metrics** — what to track in `analytics/tracker.csv`

Write in the language of the platform's audience (e.g. 小红书 playbook in Chinese). Then add a row to the `playbooks/README.md` index.

## How to add a content template

Templates live in `content/templates/<platform>.txt` and use `{placeholders}`:

| Placeholder | Meaning |
|---|---|
| `{product}` | Product name |
| `{slogan}` | Product slogan |
| `{title}` | Update title from `updates.yaml` |
| `{detail}` | Update detail from `updates.yaml` |
| `{cta}` | Call to action line |
| `{link}` | Product link (from profile or `--link`) |

Put platform constraints in `#` comments at the top of the template (character limits, hashtag rules, etc.). Test with:

```bash
python3 content/pipeline.py --product astraea --platform <your-platform>
```

If any placeholder is missing from an update entry, the pipeline will error — keep placeholders to the table above unless you also update `pipeline.py`.

## PR conventions

- One PR per playbook / template / product — small PRs merge faster
- Title format: `[playbook] xiaohongshu v2` / `[template] threads` / `[product] myproduct` / `[pipeline] ...`
- Describe **what you tested**: which command you ran, what drafts it produced
- No affiliate links, no undisclosed self-promotion. Playbooks must disclose when a tactic is paid
- Keep docs in EN for public OSS surfaces; ZH is welcome where the audience is Chinese (same rule as the existing 小红书 playbook)

## Code style

- `pipeline.py`: Python 3, stdlib + pyyaml only, ~150 lines. No new dependencies without discussion
- Landing page: single HTML file, no build step, must work from `file://`
- Workflows: valid YAML, pin action versions by SHA or semver tag

## Code of Conduct

Be kind, be specific, no spam. Playbooks that teach spam get removed — growth hacking is about leverage, not abuse.
