# Poco Loco Ranch — OS&E Sourcing Dashboard

Low-volume, brandable, luxury-feel guest supplies for the **Poco Loco Ranch** (Boerne, TX),
inspired by the OS&E at **Badrutt's Palace**. Branding is done **in-house** (laser engraving,
embroidery, and UVDTF) — or via supplier customization where noted.

**15 items · 45 vetted options · per-unit range $0.46–$440 · lowest minimum order: 1**

## How to view

- Open **`index.html`** in any browser (uses the photos in `assets/img/`).
- Or open **`dashboard-standalone.html`** — a single self-contained file (images embedded) you
  can email or open offline.

## What's in here

| File | Purpose |
|------|---------|
| `build.py` | Generator — single source of truth (the `DATA` list). Run `python3 build.py`. |
| `data/items.json` | Structured data emitted by the build. |
| `index.html` | The dashboard (open this). |
| `dashboard-standalone.html` | Self-contained single-file version (images inlined). |
| `assets/img/` | Real product photos + your logo + a rendered preview. |

### To add or edit an item
Edit the `DATA` list in `build.py`, drop the product photo(s) in `assets/img/`, then run
`python3 build.py`. It rebuilds `index.html`, `dashboard-standalone.html`, and `data/items.json`.

## Items by room

- **Closet & Dressing** — Engraveable wood hanger · Long-handled shoehorn · Standing shoehorn / valet block
- **Bath** — Shower-mounted refillable bottles
- **Bar & Table** — Bottle opener · Linen cocktail napkins
- **Bedroom & Comfort** — Small individual blankets · Sewing kit
- **Welcome & Desk** — Nice thick pens · Canvas tote bags · Bandana
- **Entry & Outdoor** — Thick branded outdoor rubber mat · Umbrella holder/stand · Long umbrellas · Poco Loco cornhole

Each item lists a **Recommended** pick plus two alternatives, with real photos, per-unit price,
supplier, minimum-order terms, specs, and the branding method.

## Methodology

- Prices, minimums, specs and the product photos were taken **directly from each supplier's live
  product page on 2026-06-21**. Retail pricing changes — confirm at checkout.
- Featured suppliers ship from **US stock** with low/no minimums so you can buy in genuinely low
  volume. A few items carry an honest caveat where a category is genuinely scarce at low volume
  (e.g., a standing shoehorn in a wooden base block).
- Photos are each supplier's own product image, downloaded so the dashboard never shows a broken link.
