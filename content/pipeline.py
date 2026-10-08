#!/usr/bin/env python3
"""Growth Hack Kit — content pipeline.

Reads product updates from content/updates.yaml and renders one draft per
platform from content/templates/*.txt into content/drafts/YYYY-MM-DD/.

Usage:
    python3 content/pipeline.py --product astraea
    python3 content/pipeline.py --product astraea --platform x --tone dreamy
    python3 content/pipeline.py --list-platforms

Only stdlib + pyyaml. Templates use {placeholders}; lines starting with
"# " are comments and are stripped from output.
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT / "content" / "templates"
UPDATES_FILE = ROOT / "content" / "updates.yaml"
DRAFTS_DIR = ROOT / "content" / "drafts"

PLACEHOLDERS = ("product", "slogan", "title", "detail", "cta", "link")
TOKEN_RE = re.compile(r"\{([a-z_]+)\}")


def load_updates(product):
    with open(UPDATES_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    updates = [u for u in data if u.get("product") == product]
    if not updates:
        sys.exit(f"No updates found for product '{product}' in {UPDATES_FILE}")
    return updates


def load_profile(product):
    """Loosely parse products/<product>/PROFILE.md for slogan + tones."""
    path = ROOT / "products" / product / "PROFILE.md"
    slogan, tones = "", []
    if not path.exists():
        return slogan, tones
    text = path.read_text(encoding="utf-8")
    m = re.search(r'\*\*Slogan:\*\*\s*"?([^"\n]+)"?', text)
    if m:
        slogan = m.group(1).strip().rstrip('"')
    m = re.search(r'Tone:[^\n]*', text)
    if m:
        tones = [t for t in re.findall(r"`([^`]+)`", m.group(0))
                 if not t.startswith("-")]
    return slogan, tones


PLAYBOOKS = {
    "x": "x-twitter.md",
    "xiaohongshu": "xiaohongshu.md",
    "instagram": "instagram-tiktok.md",
    "producthunt": "product-hunt.md",
    "reddit": "reddit.md",
}


def load_template(platform):
    path = TEMPLATES_DIR / f"{platform}.txt"
    if not path.exists():
        sys.exit(f"Unknown platform '{platform}'. See --list-platforms.")
    lines = [
        ln for ln in path.read_text(encoding="utf-8").splitlines()
        if not (ln.startswith("# ") or ln == "#")
    ]
    return "\n".join(lines).strip()


def render(template, ctx):
    missing = sorted({m for m in TOKEN_RE.findall(template)
                      if m in PLACEHOLDERS and m not in ctx})
    if missing:
        sys.exit(f"Template needs missing placeholders: {missing}")
    out = template
    for _ in range(2):  # two passes so {cta} may itself contain {link}
        for key in PLACEHOLDERS:
            if key in ctx:
                out = out.replace("{" + key + "}", str(ctx[key]))
    return out


def slugify(title):
    slug = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", title.lower()).strip("-")
    return slug[:40] or "update"


def main():
    ap = argparse.ArgumentParser(description="Render per-platform content drafts.")
    ap.add_argument("--product", help="Product dir under products/")
    ap.add_argument("--platform", help="Single platform (default: all)")
    ap.add_argument("--tone", help="Brand voice tone (validated against PROFILE.md)")
    ap.add_argument("--link", default="", help="Override product link for {link}")
    ap.add_argument("--list-platforms", action="store_true")
    args = ap.parse_args()

    if args.list_platforms:
        print("\n".join(sorted(p.stem for p in TEMPLATES_DIR.glob("*.txt"))))
        return

    if not args.product:
        ap.error("--product is required (unless using --list-platforms)")

    platforms = [args.platform] if args.platform else sorted(
        p.stem for p in TEMPLATES_DIR.glob("*.txt"))
    slogan, tones = load_profile(args.product)
    if args.tone and tones and args.tone not in tones:
        print(f"Warning: tone '{args.tone}' not in profile tones {tones}",
              file=sys.stderr)
    tone = args.tone or (tones[0] if tones else "default")

    day = datetime.date.today().isoformat()
    outdir = DRAFTS_DIR / day
    outdir.mkdir(parents=True, exist_ok=True)

    count = 0
    for update in load_updates(args.product):
        link = args.link or update.get("link") or "https://example.com"
        ctx = {
            "product": update.get("product", args.product).title(),
            "slogan": slogan,
            "title": update.get("title", ""),
            "detail": update.get("detail", ""),
            "link": link,
            "cta": update.get("cta", f"Try it free: {link}"),
        }
        for platform in platforms:
            body = render(load_template(platform), ctx)
            header = (
                f"# DRAFT — {platform} — {ctx['product']} — {day}\n"
                f"# Update: {ctx['title']}\n"
                f"# Tone: {tone}\n"
                f"# Status: unreviewed — edit, then publish per "
                f"playbooks/{PLAYBOOKS.get(platform, platform + '.md')}\n"
                f"---\n"
            )
            path = outdir / f"{args.product}-{platform}-{slugify(ctx['title'])}.md"
            path.write_text(header + body + "\n", encoding="utf-8")
            count += 1
            print(f"wrote {path.relative_to(ROOT)}")
    print(f"\n{count} drafts in {outdir.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
