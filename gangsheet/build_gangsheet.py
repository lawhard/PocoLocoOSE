#!/usr/bin/env python3
"""
Poco Loco Ranch — UV DTF gang sheet builder.

Builds a print-ready 22" x 24" (2 ft) gang sheet to Ninja Transfers' UV DTF
spec: 22" fixed width, 300 DPI, PNG with transparent background, Adobe RGB.
  -> 6600 x 7200 px canvas.

Lays out each brand asset at a range of test sizes (with small size labels)
so the physical print size of each can be evaluated. Source art is decoded
from the originals the client supplied (brand-assets/raw_*.*).

Run:  python3 gangsheet/build_gangsheet.py
"""
from PIL import Image, ImageDraw, ImageFont
import sys

# Label-free PRODUCTION mode:  python3 gangsheet/build_gangsheet.py production
LABELS = not any(a in ("production", "--production", "--no-labels") for a in sys.argv[1:])

DPI       = 300
W_IN, H_IN = 22, 24
W, H      = W_IN * DPI, H_IN * DPI            # 6600 x 7200
MARGIN    = int(0.30 * DPI)                   # keep art >=0.3" from edges
GAP_X     = int(0.22 * DPI)                   # gap between items on a shelf
GAP_Y     = int(0.28 * DPI)                   # gap between shelves in a band
BAND_GAP  = int(0.45 * DPI)                   # gap between asset bands
USABLE_W  = W - 2 * MARGIN
BLACK     = (17, 17, 17, 255)                 # near-black ink
GRAY      = (120, 120, 120, 255)             # annotation gray
ASSET_DIR = "gangsheet/source"
OUT       = ("gangsheet/poco-loco-gangsheet-22x24.png" if LABELS
             else "gangsheet/poco-loco-gangsheet-22x24-PRODUCTION.png")
FONT      = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(px):
    return ImageFont.truetype(FONT, px)

F_TITLE = font(46)
F_HEAD  = font(54)
F_LABEL = font(40)

# ---- load + prep source art -------------------------------------------------
def trimmed(name, athresh=12):
    im = Image.open(f"{ASSET_DIR}/{name}").convert("RGBA")
    r, g, b, a = im.split()
    a = a.point(lambda v: 0 if v < athresh else v)   # drop near-invisible halo px
    im.putalpha(a)
    return im.crop(a.getbbox())

GATE     = trimmed("gate.webp")            # entrance gate (wide)
SCRIPT   = trimmed("script-logo.webp")     # Poco Loco Ranch script + cactus
WINDMILL = trimmed("windmill.webp")        # windmill (tall)
SEAL     = trimmed("seal.webp")            # circular seal
HOUSE    = trimmed("house.webp")           # ranch-house line drawing (wide)
PLAQUE   = trimmed("historic-plaque.png")  # black plaque, white text, transparent bg
HARDLAW_H = trimmed("hardlaw-horizontal.webp")  # Hard Law lockup (wide)
HARDLAW_S = trimmed("hardlaw-stacked.png")      # Hard Law emblem + wordmark (stacked)
SELLER    = trimmed("seller-pomegranate.webp")  # seller's pomegranate + CELLARS mark (color; white wordmark)

def scaled_w(img, inches):
    w = int(round(inches * DPI)); h = int(round(w * img.height / img.width))
    return img.resize((w, h), Image.LANCZOS)

def scaled_h(img, inches):
    h = int(round(inches * DPI)); w = int(round(h * img.width / img.height))
    return img.resize((w, h), Image.LANCZOS)

def white_disc(art, inset=0.02):
    """white circular backing under a round mark (the seal)."""
    w, h = art.size
    base = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ix, iy = int(w*inset), int(h*inset)
    ImageDraw.Draw(base).ellipse([ix, iy, w-1-ix, h-1-iy], fill=(255, 255, 255, 255))
    base.alpha_composite(art)
    return base

def white_plaque(art, pad_in=0.08, radius_in=0.10):
    """white rounded-rectangle backing behind an irregular mark."""
    pad = int(pad_in*DPI); rad = int(radius_in*DPI)
    base = Image.new("RGBA", (art.width+2*pad, art.height+2*pad), (0, 0, 0, 0))
    ImageDraw.Draw(base).rounded_rectangle([0, 0, base.width-1, base.height-1],
                                           radius=rad, fill=(255, 255, 255, 255))
    base.alpha_composite(art, (pad, pad))
    return base

def label(text):
    bb = F_LABEL.getbbox(text)
    im = Image.new("RGBA", (bb[2]-bb[0]+4, bb[3]-bb[1]+4), (0,0,0,0))
    ImageDraw.Draw(im).text((2-bb[0], 2-bb[1]), text, font=F_LABEL, fill=GRAY)
    return im

def item(img, text):
    """art with a centered size label beneath it (no label in production mode)."""
    if not LABELS:
        return img
    lab = label(text)
    gap = int(0.07 * DPI)
    w = max(img.width, lab.width); h = img.height + gap + lab.height
    cell = Image.new("RGBA", (w, h), (0,0,0,0))
    cell.alpha_composite(img, ((w-img.width)//2, 0))
    cell.alpha_composite(lab, ((w-lab.width)//2, img.height + gap))
    return cell

# ---- layout -----------------------------------------------------------------
canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(canvas)

def shelves(items):
    out, cur, cw = [], [], 0
    for it in items:
        add = it.width + (GAP_X if cur else 0)
        if cw + add > USABLE_W and cur:
            out.append(cur); cur, cw = [], 0; add = it.width
        cur.append(it); cw += add
    if cur: out.append(cur)
    return out

def band(title, items, y):
    if LABELS:
        draw.text((MARGIN, y), title, font=F_HEAD, fill=GRAY)
        y += F_HEAD.getbbox(title)[3] + int(0.10 * DPI)
    for shelf in shelves(items):
        sh = max(it.height for it in shelf)
        x = MARGIN
        for it in shelf:
            canvas.alpha_composite(it, (x, y + sh - it.height))  # bottom-align
            x += it.width + GAP_X
        y += sh + GAP_Y
    return y + BAND_GAP - GAP_Y

# title (omitted in production mode)
if LABELS:
    draw.text((MARGIN, MARGIN - int(0.04*DPI)),
              'POCO LOCO RANCH  —  BRAND ASSET SIZE TEST  (+ SEAL WHITE-BACKING)  —  22" x 24" UV DTF GANG SHEET  —  300 DPI',
              font=F_TITLE, fill=GRAY)
y = MARGIN + (int(0.45 * DPI) if LABELS else 0)

def paired(art, sizes, backing):
    """alternate a transparent + a white-backed copy of one mark at each size."""
    out = []
    for s in sizes:
        a = scaled_w(art, s)
        out.append(item(a, f'{s}"'))
        out.append(item(backing(a), f'{s}"  white'))
    return out

# white backing requested on the SEAL only
y = band("CIRCULAR SEAL  —  transparent + white backing at each size",
         paired(SEAL, (3.5,2.5,1.75,1.25), white_disc), y)
y = band("RANCH SCRIPT LOGO  (width)",
         [item(scaled_w(SCRIPT, s), f'{s}"') for s in (4,3.5,3,2.5,2,1.5,1.25,1)], y)
y = band("ENTRANCE GATE  (width)",
         [item(scaled_w(GATE, s), f'{s}"') for s in (7,4.5,3,2)], y)

# windmill (by height) + plaque (by height) share a band to save space
wm = [item(scaled_h(WINDMILL, s), f'{s}" tall') for s in (4,3,2.25,1.5)]
pl = [item(scaled_h(PLAQUE, s),   f'{s}" tall') for s in (3.5,2.75,2)]
seller = [item(scaled_w(SELLER, 3.5),  'SELLER 3.5" (glass)'),
          item(scaled_w(SELLER, 3.5),  'SELLER 3.5" (glass)'),
          item(scaled_w(SELLER, 2.25), 'SELLER 2.25"')]
y = band("WINDMILL  ·  PLAQUE  ·  SELLER LOGO  (sized 3.5\" for a soda-can glass, x2)", wm + pl + seller, y)

hardlaw = [item(scaled_w(HARDLAW_H, 4.5), 'HARD LAW 4.5"'),
           item(scaled_w(HARDLAW_S, 2.5), 'HARD LAW 2.5"')]
y = band("RANCH HOUSE LINE ART  ·  HARD LAW LOGOS (added)",
         [item(scaled_w(HOUSE, s), f'{s}"') for s in (6,4,2.5)] + hardlaw, y)

print(f"content bottom y = {y}px ({y/DPI:.2f}in) of {H}px ({H_IN}in)")
assert y <= H - MARGIN, "OVERFLOW: content exceeds canvas height"

canvas.save(OUT, dpi=(DPI, DPI))
# downscaled preview for quick visual check
prev = canvas.copy()
bg = Image.new("RGBA", prev.size, (199,199,199,255))   # mid gray so white backing is visible
_pv = "/tmp/gangsheet_preview.jpg" if LABELS else "/tmp/gangsheet_preview_production.jpg"
Image.alpha_composite(bg, prev).convert("RGB").resize((W//6, H//6), Image.LANCZOS).save(_pv, quality=88)
import os
print("saved", OUT, f"{os.path.getsize(OUT)/1e6:.2f} MB", canvas.size)
