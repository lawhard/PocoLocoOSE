# -*- coding: utf-8 -*-
"""
Poco Loco Ranch — OS&E Sourcing Dashboard generator.
Single source of truth: the DATA list below.
Outputs:
  - data/items.json           (structured data artifact)
  - index.html                (dashboard, references assets/img/*)
  - dashboard-standalone.html  (self-contained, images inlined as base64)
Run:  python3 build.py
"""
import json, base64, pathlib, html as _html

ROOT = pathlib.Path(__file__).parent
IMG = ROOT / "assets" / "img"

META = {
    "property": "Poco Loco Ranch",
    "location": "Boerne, Texas",
    "prepared": "June 21, 2026",
    "branding": "In-house: laser engraving, embroidery & UVDTF",
    "inspiration": "Badrutt's Palace, St. Moritz",
}

CATEGORIES = [
    ("closet",  "Closet & Dressing", "Heavy, brandable pieces that stay put and feel hotel-grade."),
    ("bath",    "Bath",              "Refillable, premium fixtures that replace single-use plastic."),
    ("bar",     "Bar & Table",       "Durable bar tools and real linen for the table."),
    ("bedroom", "Bedroom & Comfort", "Soft goods guests touch — embroiderable and warm."),
    ("welcome", "Welcome & Desk",    "Take-home and everyday-carry pieces, easy to brand in bulk."),
    ("outdoor", "Entry & Outdoor",   "Big statement pieces for the porch, entry and yard."),
]

# tier -> (css class, default badge)
TIERS = {
    "recommended": ("rec",  "★ Recommended"),
    "premium":     ("prem", "Premium"),
    "value":       ("val",  "Value"),
    "alt":         ("alt",  "Alternative"),
}

def opt(tier, name, supplier, url, price, unit, terms, mn, specs, brand, why, img, badge=None):
    return dict(tier=tier, badge=badge or TIERS[tier][1], name=name, supplier=supplier, url=url,
                price=price, unit=unit, terms=terms, min=mn, specs=specs, brand=brand, why=why, img=img)

DATA = [
 # ---------------- CLOSET & DRESSING ----------------
 dict(id="hanger", cat="closet", name="Thick Engraveable Wood Hanger", tag="Anti-theft heft",
   reference="Your Badrutt's Palace reference: warm wood, brass hook, an understated engraved crest on the flat shoulder. These chase that heft + engraveable face in Hill-Country tones.",
   note="Engraving tip: natural/light wood gives the crispest logo contrast; warm walnut gives the subtle, elegant burn of the Badrutt's crest. Engrave the flat shoulder face.",
   options=[
     opt("recommended","Contoured Deluxe Suit Hanger — Walnut","OnlyHangers","https://www.onlyhangers.com/products/contoured-deluxe-wood-suit-hanger-wnon-slip-bar",
         "≈ $12.98","/ hanger","$38.95 / 3-pack","min 3","Beech, walnut finish · thick 18″ contour · chrome hook · non-slip bar",
         "In-house laser engrave","Genuinely thick & heavy, warm walnut suits the ranch, and a 3-pack lets you test your laser before scaling.","assets/img/hanger-primary-walnut.jpg"),
     opt("premium","Tailor Made® Coat Hanger — Butterscotch + Brass","Butler Luxury","https://www.butlerluxury.com/products/tailor-made-custom-suit-hanger",
         "$38.00","/ hanger","sold individually","min 1","Grade-A German beech · 2⅝″ sculpted shoulder · solid brass hook","In-house laser engrave",
         "Closest to Badrutt's — heirloom weight, brass hook, warm wood. Buy one to prototype.","assets/img/hanger-premium-butler.jpg"),
     opt("value","Contoured Suit Hanger w/ Locking Bar — Natural","OnlyHangers","https://www.onlyhangers.com/products/contoured-wooden-suit-hanger-wlocking-bar-natural",
         "≈ $2.44","/ hanger","$60.95 / box of 25","min 25","Natural hardwood, clear lacquer · 17″ · wooden locking bar","In-house laser engrave",
         "Lowest cost per unit and the crispest engraving contrast; trade-off is a slimmer profile.","assets/img/hanger-value-natural.jpg"),
   ]),
 dict(id="shoehorn", cat="closet", name="Long-Handled Shoehorn", tag="Entry valet",
   options=[
     opt("recommended","Hanger Project Walnut Long-Handle Shoe Horn","Kirby Allison","https://kirbyallison.com/products/hanger-project-walnut-long-handle-shoe-horn",
         "$210","/ ea","sold individually","min 1","Solid walnut, ~24″+, deerskin strap · handcrafted in Dallas, TX","In-house laser engrave handle",
         "Heirloom US-made walnut from the same house as the hanger pick — premium and on-brand.","assets/img/shoehorn-rec.jpg"),
     opt("value","Personalized Engraved 7″ Natural Wood Shoe Horn","Teals Prairie & Co.","https://www.tealsprairie.com/products/personalized-engraved-7-in-natural-wood-shoe-horn-with-quote/",
         "$29.99","/ ea","single · 5% off 5+","min 1","Natural wood 7″ · handheld · smooth engraving face","Supplier-engraved (turnkey)",
         "The only turnkey option where the supplier laser-engraves your seal for you — no equipment needed.","assets/img/shoehorn-alt1.jpg"),
     opt("value","Long Wooden Shoehorn","MUJI","https://www.muji.us/products/wooden-shoehorn-long-23aw",
         "$8.90","/ ea","sold individually","min 1","Birch, 22″ · hangs by cord loop","In-house UVDTF / engrave",
         "Rock-bottom price for a real long wood shoehorn; brand the handle in-house. The everyday workhorse.","assets/img/shoehorn-alt2.jpg"),
   ]),
 dict(id="shoehornstand", cat="closet", name="Standing Shoehorn / Valet Block", tag="Niche category",
   note="Honest note: a long shoehorn seated in its own wooden base block is a genuinely scarce category — only two US-buyable pieces verified. The third is the closest verified low-cost engravable wood shoehorn (handheld). Or pair a Shoehorn pick above with an in-house-engraved walnut block.",
   options=[
     opt("recommended","Standing Shoehorn (Kime, by Mikiya Kobayashi)","Nalata Nalata (NYC)","https://shop.nalatanalata.com/products/standing-shoehorn-1",
         "$210","/ ea","sold individually","min 1","Walnut horn 28″ + walnut base block 4.7″ · leather loop · Asahikawa craft","In-house laser-engrave the base block",
         "Best-in-class: a true standing shoehorn in a substantial walnut block — a flat face made for your seal.","assets/img/shoehornstand-rec.jpg"),
     opt("alt","Kime Shoehorn with Wooden Stand","Amazon (ships from Amazon)","https://www.amazon.com/Shoehorn-Stand-Handle-Wooden-Walnut/dp/B0D9LPXZNJ",
         "$119","/ ea","sold individually","min 1","Solid walnut 27.5″ + matching wooden stand · made in Japan","In-house laser-engrave the base",
         "Nearly the same concept at ~half the price, with frictionless Amazon stock and US shipping.","assets/img/shoehornstand-alt1.jpg"),
     opt("value","Personalized Engraved Wood Shoe Horn (closest verified)","Teals Prairie & Co.","https://www.tealsprairie.com/products/personalized-engraved-7-in-natural-wood-shoe-horn-with-quote/",
         "$29.99","/ ea","single · 5% off 5+","min 1","Natural wood 7″ · handheld (does not stand) · supplier-engraved","Supplier-engraved (turnkey)",
         "Flagged honestly: handheld, not standing — the closest verified low-cost engravable wood piece if the standing form isn't essential.","assets/img/shoehornstand-alt2.jpg"),
   ]),
 # ---------------- BATH ----------------
 dict(id="shower", cat="bath", name="Shower-Mounted Refillable Bottles", tag="Replaces single-use",
   options=[
     opt("recommended","Triple Wall Mount + Signature Amber Glass Dispensers","The Polished Jar","https://thepolishedjar.com/products/triple-wall-mount-for-soap-dispensers",
         "≈ $177","/ station","$108 bracket + $23/bottle","min 1","Matte-black or brass triple bracket + 16oz amber glass pumps","In-house laser/UVDTF on glass, or supplier-engraved",
         "Amber glass + matte-black/brass reads premium-rustic, and the smooth glass is the only option you can truly brand in-house.","assets/img/shower-rec.png"),
     opt("value","Hotel-at-Home Triple Wall-Mounted Set — Amber","MaisonOvo","https://www.maisonovo.com/products/wall-mounted-soap-dispenser-amber-bronze",
         "$45","/ set","3 bottles + mounts + labels","min 1","Shatter-safe amber PET ×3 · no-drill adhesive mounts · funnel","In-house UVDTF labels",
         "Cheapest turnkey amber system, shatter-safe for a rental shower — buy one, UVDTF a label, done.","assets/img/shower-alt1.jpg"),
     opt("premium","Wall Mount Pump — Triple (or Single $50)","simplehuman","https://www.simplehuman.com/products/wall-mount-pump-triple",
         "$100","/ triple","sealed refillable chambers","min 1","Brushed stainless, rust-proof, 15oz/chamber · 5-yr warranty","In-house laser/label",
         "The genuine hotel-grade fixture — bulletproof sealed metal, no glass to break. Modern-luxe lean.","assets/img/shower-alt2.jpg"),
   ]),
 # ---------------- BAR & TABLE ----------------
 dict(id="opener", cat="bar", name="Bottle Opener", tag="Stays on the bar",
   options=[
     opt("recommended","Wooden Bottle Opener — Walnut/Cherry + Stainless","BirchBarn Designs (USA)","https://birchbarndesigns.com/product/wood-bottle-opener/",
         "$20","/ ea","free engraving included","min 1","Stainless speed-opener faced with real hardwood · made in USA","Supplier engraves free — or in-house on the wood face",
         "Real walnut + solid stainless reads exactly 'Hill Country bar,' buyable as one, and the only pick that supports both supplier and in-house branding.","assets/img/opener-rec.jpg"),
     opt("value","Stainless + Leather Bottle Opener (8-pack blanks)","PYD Life","https://shop.pydlife.com/products/craft-blanks-stainless-steel-bottle-opener-with-leather-cover-for-custom-laser-engraving-card-shape-5-color-options-8-pack",
         "$2.75","/ ea","$21.99 / 8-pack","min 8","Stainless + genuine leather face · brown tones","In-house laser-engrave the leather",
         "Crushes the price target, leather-on-steel matches the palette, and it's purpose-built as a laser blank.","assets/img/opener-alt1.jpg"),
     opt("alt","Rustic Cast Iron Wall-Mounted Opener","BarnwoodUSA","https://barnwoodusa.com/products/rustic-cast-iron-wall-mounted-bottle-opener",
         "$9.99","/ ea","sold individually","min 1","Solid cast iron, antique-brown, wall-mount fixture","Mount on an in-house engraved wood backer",
         "The most 'ranch fixture' look at under $10; brand it via a laser-engraved wood backer board.","assets/img/opener-alt2.jpg"),
   ]),
 dict(id="napkins", cat="bar", name="Linen Cocktail Napkins", tag="Real linen",
   options=[
     opt("recommended","Ecru Hemstitched Linen Cocktail Napkins (dozen)","Bumblebee Linens","https://bumblebeelinens.com/dozen-ecru-hemstitched-linen-cocktail-napkins-p-201.html",
         "≈ $1.58","/ napkin","$18.99 / dozen","min 12","100% linen, ecru · 6×6″ · ladder hemstitch","In-house corner embroidery",
         "Genuine pure linen in an earthy ecru, true cocktail size, by the dozen, purpose-made as an embroidery blank.","assets/img/napkin-rec.jpg"),
     opt("premium","Cocktail Napkins — 100% Pure Linen (Beige)","All Cotton and Linen","https://www.allcottonandlinen.com/products/cocktail-napkins",
         "≈ $6.25","/ napkin","$24.99 / set of 4","min 4","100% linen, beige · 12×12″ · wide hem","In-house embroidery / UVDTF",
         "Premium pure linen at the lowest minimum (just 4) in an on-brand beige.","assets/img/napkin-alt1.webp"),
     opt("value","Saro Hemstitched Cocktail Napkins (set of 6)","Tres Belle Fete","https://tresbellefete.com/products/hemstitched-cocktail-napkins",
         "≈ $3.75","/ napkin","$22.50 / set of 6","min 6","55% linen / 45% cotton · 6×6″ · hemstitched · white","In-house embroidery",
         "Durable linen-cotton blend that launders and embroiders easily for heavy rental turnover.","assets/img/napkin-alt2.jpg"),
   ]),
 # ---------------- BEDROOM & COMFORT ----------------
 dict(id="blankets", cat="bedroom", name="Small Individual Blankets", tag="Embroiderable",
   options=[
     opt("recommended","Yakima Camp Throw (54×66″)","Pendleton","https://www.pendleton-usa.com/product/yakima-camp-throw/72266.html",
         "$188","/ ea","sold individually","min 1","Virgin wool/cotton, camp stripe · earthy colorways · USA mills","In-house corner embroidery",
         "The genuine Pendleton-style southwestern throw — made-in-USA wool, earthy tones, embroiderable, buyable one at a time.","assets/img/blanket-rec.jpg"),
     opt("premium","Frontier Wool Throw (50×72″)","Faribault Mill","https://www.faribaultmill.com/products/frontier-throw",
         "$195","/ ea","sold individually","min 1","100% US wool, natural/gray · heritage MN mill since 1865","In-house embroidery",
         "A quieter solid-tone American wool throw for a more understated, modern-rustic look.","assets/img/blanket-alt1.jpg"),
     opt("value","Core Fleece Blanket BP60 (50×60″)","Port Authority / Full Source","https://www.fullsource.com/port-authority-1013143/",
         "$7.68","/ ea","sold individually (blank)","min 1","9oz anti-pill fleece · neutral tones · exact 50×60″","In-house embroidery or UVDTF",
         "The value play and the only exact 50×60 spec — outfit every bed cheaply and brand in-house.","assets/img/blanket-alt2.jpg"),
   ]),
 dict(id="sewing", cat="bedroom", name="Sewing Kit", tag="Guest amenity",
   options=[
     opt("recommended","#8205 Hard-Case Travel Sewing Kit (28-pc)","Coghlan's","https://www.coghlans.com/sewing-kit-8205",
         "$2.99","/ ea","no minimum","min 1","Hard clamshell case 3.3×2.3″ · rugged outdoor brand","In-house UVDTF on the lid",
         "Only option with a true minimum of 1 and a smooth hard lid purpose-built for your UVDTF seal.","assets/img/sewing-rec.jpg"),
     opt("alt","Compact Zippered Sewing Kit","4imprint","https://www.4imprint.com/product/120055/Compact-Zippered-Sewing-Kit",
         "$2.99","/ ea","min 100 + $40 setup","min 100","Soft vinyl zip case · black · 10 threads, scissors, tape","Supplier-printed",
         "Closest to a turnkey pre-branded hotel amenity if you'd rather not UVDTF them yourself.","assets/img/sewing-alt1.jpg"),
     opt("premium","In a Pinch 15-Piece Essentials Kit","4imprint","https://www.4imprint.com/product/169888/In-a-Pinch-15-Piece-Essentials-Kit",
         "$7.75","/ ea","min 50 + $55 setup","min 50","Recycled-poly pouch · sewing + grooming multi-amenity","Supplier-printed",
         "An elevated all-in-one guest essentials pouch with the lowest branded MOQ (50).","assets/img/sewing-alt2.jpg"),
   ]),
 # ---------------- WELCOME & DESK ----------------
 dict(id="pens", cat="welcome", name="Nice Thick Pens", tag="≤ $5 target",
   options=[
     opt("recommended","Venetian Metal Pen — Laser Engraved","4imprint","https://www.4imprint.com/product/105100-L/Venetian-Metal-Pen-Laser-Engraved",
         "$1.99","/ pen","min 75 + $30 setup · ~$1.45@250","min 75","Solid aluminum barrel, chrome accents · black/green","Supplier laser-engraved",
         "Hits the target dead-on: well under $5, real metal, engraved-for-you, in stock. Pick black or green for the palette.","assets/img/pen-alt1.jpg"),
     opt("premium","Parker IM Metal Pen — Laser Engraved","4imprint","https://www.4imprint.com/product/146783-L/Parker-IM-Metal-Pen-Laser-Engraved",
         "$31.25","/ pen","min 15 + $20 setup","min 15","Genuine Parker · solid brass barrel · substantial weight","Supplier laser-engraved",
         "The showpiece: real Parker brand, heavy brass barrel — rugged-luxury weight in a guest's hand. Lowest MOQ (15).","assets/img/pen-rec.jpg"),
     opt("value","Soft Touch Metal Pens (50-pack blanks)","BulkLaser","https://bulklaser.com/products/bulk-soft-touch-metal-pens",
         "$0.46","/ pen","$23 / 50-pack · no setup","min 50","Aluminum, soft-touch coating · 15 colors · stylus tip","In-house laser-engrave",
         "Cheapest path to a custom metal pen if you engrave in-house — $0.46 each, no setup, full control.","assets/img/pen-alt2.jpg"),
   ]),
 dict(id="totes", cat="welcome", name="Canvas Tote Bags", tag="Embroider / UVDTF",
   options=[
     opt("recommended","Bayside 12oz USA Cotton Canvas Tote — Natural","BagzDepot","https://www.bagzdepot.com/products/made-in-usa-tote-bags-ba750",
         "$19.35","/ ea","qty breaks at 6/50/250","min 1","12oz cotton canvas, MADE IN USA · gusset · natural","In-house embroidery / UVDTF",
         "Blank natural heavy canvas, made in USA, buyable as singles — substantial enough to feel premium, cheap enough to brand a stack.","assets/img/tote-rec.jpg"),
     opt("premium","Day Tote in Waxed Canvas (No. 103)","ARTIFACT Bags (USA)","https://artifactbags.com/products/day-tote-in-waxed-canvas",
         "$140","/ ea","sold individually","min 1","14oz waxed canvas · full-grain leather straps · solid brass · handmade Omaha","In-house UVDTF / maker monogram",
         "The true luxury-rustic piece — waxed canvas, leather, brass, made by hand. A flagship welcome gift.","assets/img/tote-alt1.jpg"),
     opt("value","Heavy Duty 13oz Canvas Tote — Natural","BagzDepot","https://www.bagzdepot.com/products/canvas-tote-bags-bs148",
         "$7.25","/ ea","qty breaks at 24/250","min 1","13oz cotton canvas, natural · gusset","In-house embroidery / UVDTF",
         "Heaviest fabric (13oz) at the lowest price — best dollar-for-quality if you're branding a quantity in-house.","assets/img/tote-alt2.jpg"),
   ]),
 dict(id="bandana", cat="welcome", name="Bandana", tag="Print or blank",
   options=[
     opt("recommended","Port Authority C960 Cotton Bandana","DTLA Print","https://www.dtlaprint.com/products/port-authority-cotton-bandana-c960/",
         "$3.40","/ ea","blank min 1 · printed no-min (DTG)","min 1","100% cotton, 21.5×21.5″ · serged seams · many colors","In-house UVDTF/embroidery, or supplier print",
         "The only option that's both buyable at qty 1 AND printable with no minimum — brand in-house or have them print it.","assets/img/bandana-rec.jpg"),
     opt("alt","Custom Printed Bandana (C960 base)","Broken Arrow Wear","https://www.brokenarrowwear.com/catalog/accessories/bandanas.html",
         "quote","/ ea","screen min 6 · DTG no-min","min 6","100% cotton · full-color DTG or 1-color screen","Supplier-printed",
         "Best dedicated low-MOQ custom-printed route — your seal printed on the same premium cotton.","assets/img/bandana-alt1.webp"),
     opt("value","Border 50 Custom Screen-Printed Bandana","WholesaleForEveryone","https://custom.wholesaleforeveryone.com/product/border-50-custom-printed-bandanas-design-your-own-screen-printed/",
         "$25","/ ea","at 12 pcs · scales down with volume","min 12","100% cotton 22×22″ · earth-tone base colors (khaki/rust/brown)","Supplier screen-print",
         "The only custom option with true earth-tone base fabric to match the ranch palette.","assets/img/bandana-alt2.jpg"),
   ]),
 # ---------------- ENTRY & OUTDOOR ----------------
 dict(id="mat", cat="outdoor", name="Thick Branded Outdoor Rubber Mat", tag="Logo molded-in",
   options=[
     opt("recommended","SuperScrape Impressions Custom Logo Mat","FloorMatShop (USA)","https://www.floormatshop.com/Superscrape-Impressions-Logo-Mat.aspx",
         "$147.98","/ mat","2.5×3′ ($151.81 for 3×4′)","min 1","100% nitrile rubber, 3/16″ thick · up to 6×8′ · logo molded in","Supplier-molded full-color logo",
         "A genuinely thick, heavy all-rubber scraper with the seal permanently molded in — survives Hill-Country sun, rain and boots.","assets/img/mat-rec.jpg"),
     opt("value","Rubber Logo Scraper Mat (Custom)","Custom-Mats.com","https://custom-mats.com/collections/outdoor-logo-mats/products/rubber-logo-scraper-mat",
         "$95.16","/ mat","2×3′ on sale","min 1","All-rubber scraper cleats · HD 4-color print + PMS match","Supplier-printed",
         "Same all-rubber outdoor concept ~$50 cheaper at the small size, still qty 1.","assets/img/mat-alt1.jpg"),
     opt("alt","Completely Custom Coir Doormat","Nickel Designs (USA)","https://nickel-designs.com/products/completely-custom-personalized-doormat",
         "$74.99","/ mat","18×30″ standard","min 1","Natural coir on thick vinyl base · UV-printed · made in USA","Supplier UV-print (or blank for in-house)",
         "Warmest 'ranch-porch' look — natural coir, US small-shop made, the cheapest of the three. Confirm made-to-order stock.","assets/img/mat-alt2.png"),
   ]),
 dict(id="umbrellaholder", cat="outdoor", name="Umbrella Holder / Stand", tag="Entry fixture",
   options=[
     opt("recommended","Scroll Forged Wrought Iron Umbrella Stand","Iron Accents (USA)","https://www.ironaccents.com/products/scroll-umbrella-stand",
         "$315","/ ea","made-to-order","min 1","Hand-forged iron, 25″H, 13 lbs · aged-patina finishes · US-made","In-house laser-engrave / UVDTF",
         "Hand-forged American iron reads rugged Hill Country, and solid iron is the cleanest engraving substrate. Order early (multi-week build).","assets/img/umbrellaholder-rec.jpg"),
     opt("value","Galvanized Metal Umbrella Stand, 28″","Globedecor","https://globedecor.com/product/metal-umbrella-stand-galvanized-gray-28/",
         "$109.99","/ ea","in stock now","min 1","Galvanized steel barrel + brass-tone footed base · 28″H","In-house engrave / UVDTF the barrel",
         "The galvanized-bucket look the brief asked for, in stock, at a third of the premium price.","assets/img/umbrellaholder-alt1.jpg"),
     opt("alt","Country Stump Vintage Umbrella Stand","Bushy Box","https://www.bushybox.com/products/country-stump-vintage-farmhouse-umbrella-stand-unique-indoor-outdoor-walking-stick-umbrella-holder-rustic-home-entryway-log-bin",
         "$159","/ ea","in stock","min 1","Cement composite faux tree-stump · 32″H · weatherproof","In-house UVDTF or engraved medallion",
         "A memorable rustic statement piece; brand via UVDTF or an applied engraved tag (textured surface).","assets/img/umbrellaholder-alt2.jpg"),
   ]),
 dict(id="umbrellas", cat="outdoor", name="Long Umbrellas", tag="Print or blank",
   options=[
     opt("recommended","The Selva Auto-Open Bamboo Stick Umbrella (48″)","4imprint","https://www.4imprint.com/product/156465/The-Selva-Auto-Open-Stick-Umbrella-48-Arc",
         "$20.99","/ ea","min 25 · print included, no setup","min 25","Bamboo shaft + handle · vented RPET canopy · auto-open","Supplier 4-color print included",
         "Natural bamboo = the warm wood/canvas look, vented = windproof, and a full multi-color logo print is included with zero setup fee.","assets/img/umbrella-rec.jpg"),
     opt("value","Aluminum Stick Umbrella with Wood Handle (48″)","Umbrellas & Beyond","https://umbrellasandbeyond.com/products/ht-4020-wood-handle-stick-umbrella-48",
         "$12.23","/ ea","blank, qty 1","min 1","Aluminum shaft · wood grip · nylon canopy · khaki · auto-open","In-house UVDTF / engrave the handle",
         "The qty-1, lowest-cost, brand-it-yourself play — khaki + wood handle nails the neutral palette.","assets/img/umbrella-alt1.jpg"),
     opt("premium","Classic Curved-Handle Umbrella (54″)","4AllPromos","https://www.4allpromos.com/product/classic-curved-handle-umbrella",
         "$18.05","/ ea","min 36 + $50/color","min 36","54″ arc · dark wood crook handle with brass accents · auto-open","Supplier screen-print",
         "The dressiest silhouette — full walking-stick with real wood crook + brass. Wood + brass = the Poco Loco material story.","assets/img/umbrella-alt2.jpg"),
   ]),
 dict(id="cornhole", cat="outdoor", name="Poco Loco Cornhole", tag="Custom printed",
   options=[
     opt("recommended","Custom Tournament Series Set + Pro Bags","Cornhole Solutions (USA)","https://cornholesolutions.com/products/custom-cornhole-set-direct-printed-regulation-2-by-4-tournament-set",
         "≈ $440","/ set","$379.99 boards + $59.99 bags","min 1 set","Regulation 2×4′ · 3/4″ Baltic birch · edge-to-edge UV print · folding legs","Supplier-printed full color",
         "Premium 3/4″ Baltic birch with edge-to-edge logo printing, orderable as one set, fast turnaround. The natural birch suits the ranch.","assets/img/cornhole-rec.jpg"),
     opt("value","Business Design #28 Custom Birch Boards","Cornhole Pro LLC (USA)","https://cornholepromn.com/business-design-28-custom-with-your-business-logo-regulation-size-cornhole-boards-baltic-birch-cornhole-boards-custom-cornhole-boards/",
         "$265","/ set","boards only (bags extra)","min 1 set","Regulation 2×4′ · Baltic birch (1/2″ or 3/4″ Pro) · full UV print","Supplier-printed full color",
         "Same premium birch + full-color print ~$115 cheaper at the board level; add the 3/4″ Pro tier for max heft.","assets/img/cornhole-alt1.jpg"),
     opt("alt","Lightweight Regulation Set + 8 Bags + Case (blank)","Tailgating Pros (USA)","https://www.tailgatingpros.com/4x2-lightweight-regulation-cornhole-boards/",
         "$129.85","/ set","includes bags + carry case","min 1 set","Solid-wood frame, 1/2″ ply top · 8 bags + case","In-house UVDTF or laser-engrave",
         "The budget/control route — a complete set for ~a third the price; laser-engrave or UVDTF the seal yourself.","assets/img/cornhole-alt2.jpg"),
   ]),
]

# ---------------- rendering ----------------
CSS = """
:root{--cream:#f8f2e6;--parch:#fffdf7;--espresso:#3b2a1d;--bark:#4f3a28;--rust:#b5532a;--rustsoft:#c87a4f;--sage:#7c7f4e;--brass:#b0894f;--ink:#2c211a;--muted:#7a6a59;--line:#e6dcc8;--good:#3f7d4f;--sh:0 6px 22px rgba(59,42,29,.10);--shlg:0 14px 40px rgba(59,42,29,.16);}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:radial-gradient(1200px 600px at 82% -10%,#f3e8d4 0,transparent 60%),var(--cream);line-height:1.55}
h1,h2,h3,h4{font-family:Georgia,"Times New Roman",serif}a{color:var(--rust);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:1200px;margin:0 auto;padding:0 22px}
header.top{background:linear-gradient(135deg,var(--espresso),var(--bark));color:#f6ecdc;padding:30px 0 26px;border-bottom:4px solid var(--brass)}
.brandrow{display:flex;align-items:center;gap:20px;flex-wrap:wrap}
.seal-chip{background:#f3e8d4;border-radius:50%;width:92px;height:92px;flex:0 0 auto;display:flex;align-items:center;justify-content:center;border:2px solid var(--brass);box-shadow:0 4px 14px rgba(0,0,0,.25);padding:8px}
.seal-chip img{width:100%;height:100%;object-fit:contain}
header.top h1{margin:0;font-size:29px;letter-spacing:.3px}header.top .sub{margin:3px 0 0;color:#d9c7ac;font-size:14.5px}
.meta{margin-top:16px;display:flex;gap:24px;flex-wrap:wrap;font-size:13px;color:#e9dcc6}.meta b{color:#fff}
nav.cats{position:sticky;top:0;z-index:20;background:rgba(59,42,29,.97);backdrop-filter:blur(6px);border-bottom:1px solid #5a4430;box-shadow:var(--sh)}
nav.cats .wrap{display:flex;gap:6px;flex-wrap:wrap;padding-top:9px;padding-bottom:9px}
nav.cats a{color:#ecdcc4;font-size:12.5px;font-weight:600;padding:5px 11px;border-radius:20px;border:1px solid transparent;white-space:nowrap}
nav.cats a:hover{background:var(--rust);color:#fff;text-decoration:none}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin:22px 0 6px}
.stat{background:var(--parch);border:1px solid var(--line);border-radius:14px;padding:15px 17px;box-shadow:var(--sh)}
.stat .n{font-family:Georgia,serif;font-size:24px;color:var(--bark);line-height:1}.stat .l{font-size:12px;color:var(--muted);margin-top:6px;text-transform:uppercase;letter-spacing:.6px}
section.cat{padding:30px 0 6px}
.cat-h{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;border-bottom:2px solid var(--line);padding-bottom:8px;margin-bottom:4px}
.cat-h h2{font-size:23px;margin:0;color:var(--espresso)}.cat-h .blurb{color:var(--muted);font-size:13.5px}
.item{padding:22px 0 6px}
.item-h{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:12px}
.item-h h3{font-size:19px;margin:0;color:var(--bark)}
.chip{font-size:11px;font-weight:800;letter-spacing:.5px;text-transform:uppercase;color:var(--rust);background:#f6e7d6;border:1px solid #ecdcc0;border-radius:20px;padding:3px 10px}
.ref{display:flex;gap:13px;background:#fff6e9;border:1px solid #ecdcc0;border-left:4px solid var(--brass);border-radius:11px;padding:12px 15px;margin:0 0 14px;font-size:13.5px;color:#5a4836}
.ref .tg{font-size:10.5px;font-weight:800;letter-spacing:.7px;text-transform:uppercase;color:var(--brass);white-space:nowrap}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;align-items:stretch}
.card{background:var(--parch);border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:var(--sh);display:flex;flex-direction:column;transition:transform .15s,box-shadow .15s;position:relative}
.card:hover{transform:translateY(-4px);box-shadow:var(--shlg)}
.card.rec{border:2px solid var(--good)}
.ribbon{position:absolute;top:13px;left:0;z-index:2;color:#fff;font-size:10.5px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;padding:5px 11px 5px 13px;border-radius:0 14px 14px 0;box-shadow:var(--sh)}
.r-rec{background:var(--good)}.r-prem{background:var(--brass)}.r-val{background:var(--sage)}.r-alt{background:var(--muted)}
.imgbox{background:#fff;height:200px;display:flex;align-items:center;justify-content:center;border-bottom:1px solid var(--line);padding:12px}
.imgbox img{max-width:100%;max-height:100%;object-fit:contain;mix-blend-mode:multiply}
.body{padding:14px 16px 16px;display:flex;flex-direction:column;flex:1}
.supplier{font-size:11.5px;text-transform:uppercase;letter-spacing:.6px;color:var(--muted);font-weight:700}
.pname{font-size:16px;margin:3px 0 8px;color:var(--espresso);line-height:1.25}
.price{display:flex;align-items:baseline;gap:7px}.price .big{font-family:Georgia,serif;font-size:24px;color:var(--rust)}.price .per{font-size:12.5px;color:var(--muted)}
.terms{font-size:12.5px;color:#6a5848;margin:2px 0 10px}.terms .mn{display:inline-block;background:#eef0df;color:#5f6235;border-radius:6px;padding:1px 7px;font-weight:700;margin-left:4px}
.specs{font-size:12.5px;color:#5a4836;border-top:1px dashed var(--line);padding-top:9px;margin:0 0 9px}
.brand{font-size:12px;color:var(--sage);font-weight:700;margin:0 0 9px;display:flex;gap:6px;align-items:flex-start}
.brand svg{flex:0 0 auto;margin-top:2px}
.why{font-size:12.5px;background:#f5efe2;border-radius:9px;padding:9px 11px;color:#5a4836;margin:0 0 12px}
.btn{margin-top:auto;display:block;text-align:center;background:var(--espresso);color:#fff;padding:10px 12px;border-radius:9px;font-weight:700;font-size:13px}
.btn:hover{background:var(--rust);text-decoration:none}
.note{font-size:12.5px;color:#6a5848;background:#faf4e8;border:1px dashed var(--line);border-radius:10px;padding:10px 13px;margin:13px 0 0}.note b{color:var(--bark)}
footer{background:var(--espresso);color:#d9c7ac;padding:24px 0 32px;margin-top:30px;border-top:4px solid var(--brass)}footer .wrap{font-size:12.5px}footer b{color:#fff}footer a{color:var(--rustsoft)}
@media(max-width:920px){.grid{grid-template-columns:1fr}.stats{grid-template-columns:repeat(2,1fr)}}
@media print{.card:hover{transform:none}.btn{display:none}nav.cats{display:none}header.top{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
"""

ENGRAVE_SVG = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#7c7f4e" stroke-width="2.2"><path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/></svg>'

def esc(s): return _html.escape(str(s), quote=True)

def card_html(o):
    cls, _ = TIERS[o["tier"]]
    rec = " rec" if o["tier"] == "recommended" else ""
    return f"""<article class="card{rec}">
<div class="ribbon r-{cls}">{esc(o['badge'])}</div>
<div class="imgbox"><img src="{esc(o['img'])}" alt="{esc(o['name'])}" loading="lazy"></div>
<div class="body">
<div class="supplier">{esc(o['supplier'])}</div>
<h4 class="pname">{esc(o['name'])}</h4>
<div class="price"><span class="big">{esc(o['price'])}</span><span class="per">{esc(o['unit'])}</span></div>
<div class="terms">{esc(o['terms'])}<span class="mn">{esc(o['min'])}</span></div>
<div class="specs">{esc(o['specs'])}</div>
<div class="brand">{ENGRAVE_SVG}<span>{esc(o['brand'])}</span></div>
<div class="why">{esc(o['why'])}</div>
<a class="btn" href="{esc(o['url'])}" target="_blank" rel="noopener">View &amp; buy &rarr;</a>
</div></article>"""

def item_html(it):
    parts = [f'<div class="item" id="item-{it["id"]}"><div class="item-h"><h3>{esc(it["name"])}</h3><span class="chip">{esc(it["tag"])}</span></div>']
    if it.get("reference"):
        parts.append(f'<div class="ref"><span class="tg">Your<br>Reference</span><span>{esc(it["reference"])}</span></div>')
    parts.append('<div class="grid">' + "".join(card_html(o) for o in it["options"]) + '</div>')
    if it.get("note"):
        parts.append(f'<div class="note">{esc(it["note"])}</div>')
    parts.append('</div>')
    return "".join(parts)

def render():
    n_items = len(DATA)
    n_opts = sum(len(i["options"]) for i in DATA)
    cat_nav = "".join(f'<a href="#cat-{cid}">{esc(name)}</a>' for cid, name, _ in CATEGORIES)
    secs = []
    for cid, name, blurb in CATEGORIES:
        items = [i for i in DATA if i["cat"] == cid]
        body = "".join(item_html(i) for i in items)
        secs.append(f'<section class="cat" id="cat-{cid}"><div class="wrap"><div class="cat-h"><h2>{esc(name)}</h2><span class="blurb">{esc(blurb)}</span></div>{body}</div></section>')
    html_doc = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Poco Loco Ranch — OS&amp;E Sourcing Dashboard</title><link rel="icon" href="assets/img/poco-loco-logo.png"><style>{CSS}</style></head><body>
<header class="top"><div class="wrap"><div class="brandrow">
<div class="seal-chip"><img src="assets/img/poco-loco-logo.png" alt="Poco Loco Ranch"></div>
<div><h1>OS&amp;E Sourcing Dashboard</h1><p class="sub">Low-volume, brandable, luxury-feel guest supplies &mdash; vetted for the {esc(META['property'])}, {esc(META['location'])}</p></div>
</div><div class="meta"><div>Prepared <b>{esc(META['prepared'])}</b></div><div>Inspiration <b>{esc(META['inspiration'])}</b></div><div>Branding <b>{esc(META['branding'])}</b></div></div></div></header>
<nav class="cats"><div class="wrap">{cat_nav}</div></nav>
<div class="wrap"><div class="stats">
<div class="stat"><div class="n">{n_items}</div><div class="l">Items sourced</div></div>
<div class="stat"><div class="n">{n_opts}</div><div class="l">Options vetted</div></div>
<div class="stat"><div class="n">$0.46&ndash;$440</div><div class="l">Per-unit range</div></div>
<div class="stat"><div class="n">1</div><div class="l">Lowest min order</div></div>
</div></div>
{''.join(secs)}
<footer><div class="wrap"><p><b>How these were vetted.</b> Every option was checked against four constraints &mdash; <b>brandable</b> (in-house laser/embroidery/UVDTF or supplier customization), <b>low minimum order</b> (mostly 1&ndash;25 units, no overseas MOQ), <b>price fit</b> (low cost preferred, quality first), and <b>currently available</b> (in-stock US suppliers). Prices, minimums, specs and the product photos were pulled directly from each supplier's live product page on <b>{esc(META['prepared'])}</b>; confirm current price at checkout as retail pricing can change. A few items note an honest caveat where a category is genuinely scarce in low volume.</p>
<p style="margin-top:9px;color:#9c8a72">{esc(META['property'])} &middot; {esc(META['location'])} &middot; OS&amp;E Sourcing Dashboard &middot; {n_items} items &middot; {n_opts} options</p></div></footer>
</body></html>"""
    return html_doc

def inline_images(doc):
    import re
    def repl(m):
        path = m.group(1)
        p = ROOT / path
        if not p.exists():
            return m.group(0)
        mime = "image/png" if p.suffix.lower()==".png" else ("image/webp" if p.suffix.lower()==".webp" else "image/jpeg")
        b64 = base64.b64encode(p.read_bytes()).decode()
        return f'src="data:{mime};base64,{b64}"'
    return re.sub(r'src="(assets/img/[^"]+)"', repl, doc)

if __name__ == "__main__":
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / "items.json").write_text(json.dumps(
        {"meta": META, "categories": [{"id":c,"name":n,"blurb":b} for c,n,b in CATEGORIES], "items": DATA}, indent=2))
    doc = render()
    (ROOT / "index.html").write_text(doc)
    (ROOT / "dashboard-standalone.html").write_text(inline_images(doc))
    print("items:", len(DATA), "options:", sum(len(i['options']) for i in DATA))
    print("wrote index.html, dashboard-standalone.html, data/items.json")
