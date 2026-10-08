---
name: New product profile
about: Add a product to products/ for the pipeline and playbooks to target
title: "[product] <product-name>"
labels: product
---

## Product

- **Name:**
- **One-line positioning:**
- **Stage:** idea / v0 / beta / launched
- **Links:** (mark placeholders)

## Audience (2–3 personas)

1.
2.

## Brand voice

- **Tones for `--tone`:**
- **Do (example lines):**
- **Don't:**

## Viral loops (mark live vs planned)

-

## Checklist

- [ ] Copied `products/_template/` to `products/<name>/`
- [ ] Filled every PROFILE.md section (no TODOs)
- [ ] Added 3+ entries to `content/updates.yaml`
- [ ] Ran `python3 content/pipeline.py --product <name>` — drafts look right
- [ ] (optional) Added `launch-plan.md` with 30-day targets
