# Poco Loco Ranch — UV DTF Gang Sheet (size test)

A print-ready **22″ × 24″ (2 ft)** gang sheet built to **Ninja Transfers' UV DTF
PermaSticker™** spec, laying out every brand asset at a range of sizes so the
best physical size for each can be chosen before a production run.

**Deliverables:**
- [`poco-loco-gangsheet-22x24.png`](poco-loco-gangsheet-22x24.png) — labeled size-test proof
- [`poco-loco-gangsheet-22x24-PRODUCTION.png`](poco-loco-gangsheet-22x24-PRODUCTION.png) — **label-free, print-ready** (no title, headings, or size labels; art only). The leftover space is filled with **5× Hard Law (3.5″, stacked)** + **5× CELLARS (3.5″)** usable transfers.

## Built to spec

| Requirement (Ninja Transfers UV DTF) | This file |
|---|---|
| Width fixed at **22″**, length one of their sizes (here **2 ft**) | 22″ × 24″ |
| **300 DPI** raster | 6600 × 7200 px @ 300 DPI |
| **Transparent background** PNG | RGBA, transparent |
| Color: Adobe RGB (1998) recommended | art is pure black / white (profile-independent) |
| Min feature ≥ 0.02″ (0.5 mm) | see note on the 1″ seal below |
| Max file size 50 MB | ~8.1 MB |

## What's on the sheet

- **Circular seal** — 3.5″ → 1.25″, each size shown **two ways: transparent and
  white-backed** (an opaque white disc behind the ring) for comparison
- **Ranch script logo** — 4″ → 1″ (transparent)
- **Entrance gate** — 7″ → 2″ (transparent)
- **Windmill** — 4″ → 1.5″ tall (transparent)
- **Historic-site plaque** — 3.5″ → 2″ tall
- **Ranch house line art** — 6″ → 2.5″ (transparent)
- **Seller logo — CELLARS pomegranate** (full color) — **3.5″ ×2 sized for a
  soda-can glass** + a 2.25″ reference; the "CELLARS" wordmark is white ink
- **Hard Law logos** — horizontal lockup 4.5″ and stacked mark 2.5″

The two added brands (seller + Hard Law) sit in the open space beside the
plaque and house rows.

Small gray labels/headings are **guides for the size test** — strip them for a
production sheet (or ask for a label-free version).

## Transparent vs white backing

A **transparent** transfer prints only the inked art — the surface shows through
the gaps, which looks best on light goods. A **white-backed** version adds an
opaque white layer behind the art so it stays crisp on dark or colored goods.
Per request, only the **seal** is shown both ways (white disc); everything else
is transparent.

## Notes / production caveats

- **Plaque:** clean source art (solid black body, **opaque white** lettering)
  placed with its transparent background preserved — prints as a black plaque
  with white text, die-cut to the plaque outline.
- **House:** fine navy line art — delicate at the smaller sizes; the size test
  shows where the thin lines start to drop out.
- **Smallest marks** (1.25″ seal, 1″ script): thin rings/strokes approach the
  0.02″ minimum feature size — exactly the legibility limit this test reveals.

## Regenerate

```bash
pip install Pillow
python3 gangsheet/build_gangsheet.py             # labeled size-test proof
python3 gangsheet/build_gangsheet.py production   # label-free, print-ready file
```

Edit the size tuples near the bottom of `build_gangsheet.py` to change which
sizes appear. Source art lives in [`source/`](source/).
