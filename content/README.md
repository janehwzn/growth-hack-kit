# Content pipeline

Turns `updates.yaml` into platform-ready drafts. The whole content operation is three steps:

## 1. Log updates

Add entries to `content/updates.yaml`:

```yaml
- product: astraea
  title: "Couple compatibility share cards launched"
  detail: "Enter two birth dates and get a gorgeous, shareable compatibility card."
  # optional overrides:
  # cta: "Get early access:"
  # link: https://astraea.example.com?ref=x
```

## 2. Generate drafts

```bash
python3 content/pipeline.py --product astraea            # all platforms
python3 content/pipeline.py --product astraea --platform x --tone dreamy
python3 content/pipeline.py --list-platforms
```

Drafts land in `content/drafts/YYYY-MM-DD/<product>-<platform>-<slug>.md`, each with a header (platform, tone, status) so you know what's unreviewed. Brand voice comes from `products/<product>/PROFILE.md` — the pipeline reads the slogan and validates `--tone` against the profile's tone list.

## 3. Review & publish

Edit the drafts (add screenshots, fix hooks), then publish following the matching `playbooks/<platform>.md`. Log results in `analytics/tracker.csv`.

## Placeholders

Templates in `content/templates/*.txt` use `{product} {slogan} {title} {detail} {cta} {link}`. Lines starting with `# ` are comments with platform constraints and are stripped from output. See CONTRIBUTING.md for how to add a template.

## Automation

`.github/workflows/content-scheduler.yml` runs this weekly and commits fresh drafts to the `drafts` branch — see the workflow file for details.
