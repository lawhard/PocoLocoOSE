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
OUT       = "gangsheet/poco-loco-gangsheet-22x24.png"
FONT      = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(px):
    return ImageFont.truetype(FONT, px)

F_TITLE = font(46)
F_HEAD  = font(54)
F_LABEL = font(40)

# ---- load + prep source art -------------------------------------------------
def trimmed(name):
    im = Image.open(f"{ASSET_DIR}/{name}").convert("RGBA")
    return im.crop(im.split()[3].getbbox())

def plaque_solid():
    """Plaque text is knocked out to transparent; flatten on white so it
    reproduces as a black plaque w/ white text, then crop to the art."""
    im = Image.open(f"{ASSET_DIR}/historic-plaque.png").convert("RGBA")
    bb = im.split()[3].getbbox()
    bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
    return Image.alpha_composite(bg, im).crop(bb)   # opaque rectangle

GATE     = trimmed("gate.webp")        # entrance gate (wide)
SCRIPT   = trimmed("script-logo.webp") # Poco Loco Ranch script + cactus
WINDMILL = trimmed("windmill.webp")    # windmill (tall)
SEAL     = trimmed("seal.webp")        # circular seal
PLAQUE   = plaque_solid()          # Texas historic-site plaque (rectangular)

def scaled_w(img, inches):
    w = int(round(inches * DPI)); h = int(round(w * img.height / img.width))
    return img.resize((w, h), Image.LANCZOS)

def scaled_h(img, inches):
    h = int(round(inches * DPI)); w = int(round(h * img.width / img.height))
    return img.resize((w, h), Image.LANCZOS)

def label(text):
    bb = F_LABEL.getbbox(text)
    im = Image.new("RGBA", (bb[2]-bb[0]+4, bb[3]-bb[1]+4), (0,0,0,0))
    ImageDraw.Draw(im).text((2-bb[0], 2-bb[1]), text, font=F_LABEL, fill=GRAY)
    return im

def item(img, text):
    """art with a centered size label beneath it."""
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

# title
draw.text((MARGIN, MARGIN - int(0.04*DPI)),
          'POCO LOCO RANCH  —  BRAND ASSET SIZE TEST  —  22" x 24" UV DTF GANG SHEET  —  300 DPI',
          font=F_TITLE, fill=GRAY)
y = MARGIN + int(0.45 * DPI)

y = band("CIRCULAR SEAL  (width)",
         [item(scaled_w(SEAL, s), f'{s}"') for s in (4.5,3.5,3,2.5,2,1.5,1.25,1)], y)
y = band("RANCH SCRIPT LOGO  (width)",
         [item(scaled_w(SCRIPT, s), f'{s}"') for s in (4.5,3.5,3,2.5,2,1.5,1.25,1)], y)
y = band("ENTRANCE GATE  (width)",
         [item(scaled_w(GATE, s), f'{s}"') for s in (9,6,4.5,3)], y)
# windmill (by height) + plaque (by height) share a band to save space
wm = [item(scaled_h(WINDMILL, s), f'{s}" tall') for s in (4.5,3.5,2.75,2,1.5)]
pl = [item(scaled_h(PLAQUE, s),   f'{s}" tall') for s in (3.5,2.75,2)]
y = band("WINDMILL  &  HISTORIC-SITE PLAQUE  (height)", wm + pl, y)

print(f"content bottom y = {y}px ({y/DPI:.2f}in) of {H}px ({H_IN}in)")
assert y <= H - MARGIN, "OVERFLOW: content exceeds canvas height"

canvas.save(OUT, dpi=(DPI, DPI))
# downscaled preview for quick visual check
prev = canvas.copy()
bg = Image.new("RGBA", prev.size, (245,245,245,255))   # light gray to see white art edges
Image.alpha_composite(bg, prev).convert("RGB").resize((W//6, H//6), Image.LANCZOS).save("/tmp/gangsheet_preview.jpg", quality=88)
import os
print("saved", OUT, f"{os.path.getsize(OUT)/1e6:.2f} MB", canvas.size)
