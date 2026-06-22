# Poco Loco Ranch — UV DTF Gang Sheet (size test)

A print-ready **22″ × 24″ (2 ft)** gang sheet built to **Ninja Transfers' UV DTF
PermaSticker™** spec, laying out every brand asset at a range of sizes so the
best physical size for each can be chosen before a production run.

**Deliverable:** [`poco-loco-gangsheet-22x24.png`](poco-loco-gangsheet-22x24.png)

## Built to spec

| Requirement (Ninja Transfers UV DTF) | This file |
|---|---|
| Width fixed at **22″**, length one of their sizes (here **2 ft**) | 22″ × 24″ |
| **300 DPI** raster | 6600 × 7200 px @ 300 DPI |
| **Transparent background** PNG | RGBA, transparent |
| Color: Adobe RGB (1998) recommended | art is pure black / white (profile-independent) |
| Min feature ≥ 0.02″ (0.5 mm) | see note on the 1″ seal below |
| Max file size 50 MB | ~6.7 MB |

## What's on the sheet

- **Circular seal** — 4.5″ → 1″ (by width)
- **Ranch script logo** — 4.5″ → 1″ (by width)
- **Entrance gate** — 9″ → 3″ (by width)
- **Windmill** — 4.5″ → 1.5″ (by height)
- **Historic-site plaque** — 3.5″ → 2″ (by height)

Small gray labels/headings are **guides for the size test** — strip them for a
production sheet (or ask for a label-free version).

## Notes / production caveats

- **Plaque:** its lettering is *knocked out to transparent* in the source art,
  so it's flattened onto **white** here — it prints as a black plaque with white
  text (a rectangular sticker), instead of see-through letters on clear film.
- **1″ seal:** the "BOERNE, TEXAS" ring and outline approach the 0.02″ minimum
  feature size — that's exactly the legibility limit this test is meant to show.
- The other four marks are black line art on a fully transparent background.

## Regenerate

```bash
pip install Pillow
python3 gangsheet/build_gangsheet.py      # run from the repo root
```

Edit the size tuples near the bottom of `build_gangsheet.py` to change which
sizes appear. Source art lives in [`source/`](source/).
