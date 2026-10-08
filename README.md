# 🚀 Growth Hack Kit

An open-source, **runnable** growth-hack OS for indie makers — not another link list.

Most "growth hacking" repos on GitHub are one of three things: planning-only AI agents, single-purpose infra (a scheduler *or* a referral tool), or curated lists of links. Growth Hack Kit is the missing fourth thing: a complete, hands-free pipeline that turns **product updates → platform-ready drafts → published posts → referral traffic → measured results**, pre-wired for your product and runnable from a fresh clone.

## What's inside

```
growth-hack-kit/
├── products/            # Product profiles: positioning, personas, brand voice
│   ├── _template/       # Copy this to add your product
│   └── astraea/         # Example: Astraea (AI fortune-telling PWA)
├── playbooks/           # Per-platform growth SOPs (Xiaohongshu, X, IG/TikTok,
│                        # Product Hunt, Reddit, HN, programmatic SEO)
├── content/             # updates.yaml + pipeline.py + templates → timestamped drafts
├── landing/             # Self-hosted waitlist + ?ref= referral landing page
├── analytics/           # K-factor / AARRR definitions + zero-budget weekly tracker
└── .github/workflows/   # Weekly scheduler: runs the pipeline, commits drafts
```

## Quickstart

**1. Add your product** — copy the template and fill it in:

```bash
cp -r products/_template products/myproduct
# edit products/myproduct/PROFILE.md
```

**2. Log product updates** — add entries to `content/updates.yaml`:

```yaml
- product: myproduct
  title: "Couple compatibility share cards launched"
  detail: "Users can now generate a shareable compatibility card for any pair."
```

**3. Generate drafts** — the pipeline renders one draft per platform from templates:

```bash
python3 content/pipeline.py --product myproduct
# drafts land in content/drafts/2026-10-08/
```

**4. Publish** — review the drafts, post per the relevant `playbooks/*.md`, and point traffic at your `landing/` page with `?ref=` links.

**5. Measure** — log weekly numbers in `analytics/tracker.csv` and compute your K-factor with the formulas in `analytics/metrics.md`.

```bash
python3 content/pipeline.py --list-platforms   # see supported platforms
python3 content/pipeline.py --product astraea --platform xiaohongshu --tone playful
```

## How it differs from awesome-lists

| awesome-lists / planning agents | Growth Hack Kit |
|---|---|
| Link collections, read-only | Runnable scripts + templates, write-first |
| Generic advice | Product profiles with brand voice baked into generated drafts |
| One channel at a time | One `updates.yaml` entry → drafts for 5 platforms at once |
| No measurement | Weekly tracker + K-factor/AARRR formulas included |
| "Good luck" | Playbooks with do/don't, cadence, and example hooks per platform |

We deliberately **don't** rebuild what exists: for heavy-duty multi-platform scheduling, self-host [Postiz](https://github.com/gitroomhq/postiz); for full affiliate programs, use [RefearnApp](https://github.com/zak123dsfdf/refearnapp) or [RefKit](https://github.com/refkitnet/refkit). This kit is the lightweight layer that sits on top: strategy → content → referral capture → measurement.

## The first product: Astraea

Astraea ("The star-maiden reads your fate." / 星缘) is an AI fortune-telling PWA — bazi, MBTI, tarot, palmistry, western astrology — for women interested in romance and relationships. Its built-in share cards make it a natural viral-loop demo for this kit. See `products/astraea/PROFILE.md` and the 30-day `launch-plan.md`.

## Contributing

Growth hackers welcome — this gets better the more playbooks, templates, and product profiles it collects. See [CONTRIBUTING.md](CONTRIBUTING.md). Good first contributions:

- A new platform playbook (`playbooks/`)
- A new content template (`content/templates/`)
- Your product profile (`products/`) with real numbers in `analytics/tracker.csv`

## License

MIT © 2026 Jane Hu ([janehwzn](https://github.com/janehwzn)). See [LICENSE](LICENSE).

---

## 中文简介

**Growth Hack Kit** 是一个开源、可直接运行的独立开发者增长工具包——不是链接收藏夹。

- `products/`：产品档案（定位、人群、品牌语气），自带示例 Astraea（AI 算命 PWA，星缘）
- `playbooks/`：分平台增长 SOP（含小红书中文版：封面标题公式、发布时间、评论区运营、合规引流边界）
- `content/`：把产品更新写进 `updates.yaml`，`pipeline.py` 一键生成 X / 小红书 / IG / Product Hunt / Reddit 五个平台的草稿
- `landing/`：单文件 waitlist + `?ref=` 裂变落地页，GitHub Pages 直接部署
- `analytics/`：K-factor / AARRR 定义 + 零预算周追踪表

快速上手：复制 `products/_template` → 填产品档案 → 在 `content/updates.yaml` 写更新 → `python3 content/pipeline.py --product <你的产品>` → 按 playbook 发布 → 用 tracker.csv 记录数据。欢迎提 PR 贡献新的 playbook、模板和产品档案（见 CONTRIBUTING.md）。
