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

def opt(tier, name, supplier, url, price, unit, terms, mn, specs, brand, why, img, badge=None, learn=None):
    return dict(tier=tier, badge=badge or TIERS[tier][1], name=name, supplier=supplier, url=url,
                price=price, unit=unit, terms=terms, min=mn, specs=specs, brand=brand, why=why, img=img, learn=learn)

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
 dict(id="shoehorn", cat="closet", name="Long-Handled Shoehorn", tag="Oak · brass · oxhorn",
   note="Re-sourced to the $25–70 sweet spot the category was missing (the $210 Dallas-made walnut horns are the ceiling, not the target). Restock watch: Jefferson Brass Gentleman's Shoe Horn ($62, hand-cast, sold out). Dead ends verified so you don't chase them: Izola defunct, Sid Mashburn's brass $115 sold out, Yamazaki's steel horn delisted.",
   options=[
     opt("recommended","Redecker Extra-Long Shoe Horn — Oiled Oak (~25″)","Lehman's (Kidron, OH)","https://www.lehmans.com/product/extra-long-shoe-horn",
         "$24.99","/ ea","qty 1 · ships same day","min 1","One-piece oiled oak, ~24¾″ · leather hanging strap · Redecker (Germany)","In-house laser on the broad oak handle",
         "The full-length entryway horn done right — the same oak horn Sid Mashburn retails at $30 (sold out there). Engrave the seal near the strap and hang one in every closet.","assets/img/shoehorn-redecker.png"),
     opt("premium","No. 2 Shoehorn — Brass + Italian Bridle Leather","Colonel Littleton (Lynnville, TN)","https://www.colonellittleton.com/shop/leather-shoe-horn-no2/",
         "$67.00","/ ea","qty 1 · same-day ship incl. engraved","min 1","Solid brass horn · full-grain Italian bridle-leather grip · brass plaque · canvas drawstring bag","Maker engraves the plaque, or in-house on brass/leather",
         "Southern-made rustic-luxe — brass and saddle leather suit a Hill Country ranch better than an English dressing horn, at a third of the Kirby Allison price.","assets/img/shoehorn-littleton.webp",
         badge="Southern-made"),
     opt("alt","Long Shoe Horn — Oiled Beech","Iris Hantverk · at Goodee","https://www.goodeeworld.com/products/long-shoe-horn",
         "$28.00","/ ea","qty 1","min 1","15¾″ hand-carved oiled beech · leather loop · Stockholm workshop employing visually impaired craftspeople since the 1800s","In-house laser on the beech paddle",
         "Hand-carved Scandinavian mid-length with a real provenance story for the guest book — reads far more expensive than $28.","assets/img/shoehorn-iris.jpg"),
     opt("alt","AbbeyHorn Wellington 8″ Shoehorn — Real Oxhorn","Kirby Allison","https://kirbyallison.com/products/abbeyhorn-8-inch-tong-shoehorn-us",
         "$70.00","/ ea","qty 1 · 119 in stock at check","min 1","Genuine handcrafted ox horn · leather tab · Abbeyhorn, Cumbria, England (est. 1749)","Add a stamped-leather tag (horn itself doesn't laser well)",
         "The real-oxhorn dresser piece — each one unique. Short 8″ handle, so pair it with the Redecker for the bend-free long horn.","assets/img/shoehorn-abbeyhorn.jpg",
         badge="Real oxhorn"),
   ]),
 dict(id="shoehornstand", cat="closet", name="Standing Shoehorn / Boot Jack", tag="The Texas answer",
   note="Reframed: the standing-shoehorn-in-a-block is a scarce, $200 Japanese-craft category — but the TEXAS answer to the same 'help by the door' need is a wooden BOOT JACK, and guests in boots will actually use it. Package idea from the research: Redecker horn ($25) in each closet, Colonel Littleton brass on the primary dresser, a Don Orrell cherry jack ($35) at every exterior door, and the Chuck's Woodbarn Beefcake as the entry hero — ≈ $272 all-in, still under 1.5× one Kime stand. Restock watch: Pate Ranch Creations (TX) leather-inlay jacks, $60–210 — squarely the aesthetic, currently sold out; worth an email for a custom run.",
   options=[
     opt("recommended","Custom Hardwood Boot Jack — Made in Texas","TexasCrazy.com","https://www.texascrazy.com/product/custom-hardwood-boot-jack/",
         "$59","/ ea","qty 1 · volume pricing for logo runs · ~2-wk ship","min 1","Hand-selected oiled beechwood · soft rubber heel bumper · classic longhorn-fork profile","Maker engraves your brand/logo — or in-house laser",
         "Dead-center of the brief: Texas-made, engraveable, and the single most on-brand 'stand' alternative for a Boerne ranch.","assets/img/bootjack-texascrazy.jpg",
         badge="Texas-made"),
     opt("premium","'Beefcake' Boot Jack — Oak + Bison Leather","Chuck's Woodbarn (Plano, TX)","https://chuckswoodbarn.com/product/beefcake-with-initials/",
         "$145","/ ea","qty 1 · initials included","min 1","Solid oak · genuine bison-leather-lined fork + grip pad · oversized heirloom build","Maker personalizes — ask for the ranch brand instead of initials",
         "The boutique-hotel version of a boot jack: heirloom oak and bison leather from a Texas family shop. The entryway hero piece.","assets/img/bootjack-chucks.jpg"),
     opt("value","Engravable Boot Jack — Solid Cherry","Don Orrell Stirrups (USA)","https://www.donorrellstirrups.com/products/engravable-boot-jack",
         "$34.99","/ ea","qty 1 · free US ship over $100 · ~2-wk ship","min 1","Solid cherry 15×5¼″ · rounded edges, oiled finish · equestrian hardware maker","Maker laser-engraves ranch brands/logos — ideal for a branded multi-unit run",
         "Best value in the category — cherry looks richer than pine at the same money, and the maker explicitly engraves ranch brands. One at every exterior door.","assets/img/bootjack-donorrell.jpg"),
     opt("alt","Standing Shoehorn (Kime, by Mikiya Kobayashi)","Nalata Nalata (NYC)","https://shop.nalatanalata.com/products/standing-shoehorn-1",
         "$210","/ ea","sold individually","min 1","Walnut horn 28″ + walnut base block 4.7″ · leather loop · Asahikawa craft","In-house laser-engrave the base block",
         "The original Japanese-craft standing horn if you still want one in the primary suite — the in-stock White Oak sibling runs $195.","assets/img/shoehornstand-rec.jpg",
         badge="The Japanese stand"),
   ]),
 # ---------------- BATH ----------------
 dict(id="shower", cat="bath", name="Shower-Mounted Refillable Bottles", tag="Hotel locking 3-rack",
   note="Avoid: the simplehuman-style sealed pump and any clear 'see-the-liquid' bottle, and the retail Better Living AVIVA (translucent, no lock). If you'll accept three separate brackets, FINESSY / MaisoNovo do opaque amber/black sets (no lock). Custom logo labels are a Dispenser Amenities factory program (setup + label minimum) — ask your reseller.",
   options=[
     opt("recommended","SOLera III 3-Chamber Locking — Solid BLACK (opaque)","Dispenser Amenities · buy at WebstaurantStore","https://www.webstaurantstore.com/dispenser-amenities-39388-03-bkfa-solera-36-oz-black-abs-plastic-wall-mounted-adjustable-3-chamber-locking-shower-dispenser-with-oval-bottles-and-beekman-label/5263938803BKFA.html",
         "≈ $109","/ station","qty 1 · no account","min 1","ONE adjustable backplate · 3 individual locking refillable bottles · solid BLACK opaque ABS · 12oz/chamber","Supplier custom-printed label (factory program)",
         "The genuine hotel product, and it hits every ask: one locking backplate, three individual refillable bottles, SOLID BLACK (opaque — not see-through), brandable label — buyable qty 1, no account.","assets/img/shower-rec.jpg",
         learn="<span class='hd'>Where hotels actually buy these</span>One company dominates: <b>Dispenser Amenities</b> (makers of <b>SOLera</b> & <b>AVIVA</b>). Hotels buy through gated B2B distributors — <b>GuestSupply</b> (Sysco), <b>HD Supply</b>, <b>American Hotel Register</b> — which require a trade account and hide prices behind a login.<span class='hd'>How a single property buys the same unit</span>Open e-commerce resellers sell the identical SKUs at qty 1, no account: <b>WebstaurantStore</b>, <b>HotelSupplyDepot</b>, <b>Zogics</b>, <b>Rapid Hotel Supplies</b>, <b>Pineapple Hospitality</b>.<span class='hd'>The opaque catch</span>SOLera/AVIVA default to <b>translucent</b> bottles (so staff see fill levels). Insist on a <b>SOLID/opaque</b> SKU — SOLera <b>Solid Black</b> (39388-O3-BKFA) or AVIVA <b>Solid White</b> (37350) — not the translucent versions.<span class='hd'>Branding</span>Custom logo labels/faceplates are a <b>factory program</b> (Dispenser Amenities' design team, via your reseller) with a setup + label minimum — confirm cost/MOQ; the dispenser itself is qty 1.<span class='hd'>How it mounts</span>One height-adjustable ABS backplate (maximum adhesive surface = strongest hold) + double-faced tape & silicone, no drilling; each bottle locks front-facing behind a tamper gate and lifts out to refill from bulk."),
     opt("alt","SOLera III Locking — Black Rectangular (45oz)","Dispenser Amenities · WebstaurantStore","https://www.webstaurantstore.com/dispenser-amenities-39388-r3-wht-solera-45-oz-black-abs-plastic-wall-mounted-adjustable-3-chamber-locking-shower-dispenser-with-rectangular-bottles/52639388R3WHT.html",
         "≈ $120","/ station","qty 1 · no account","min 1","Same locking rack · larger 15oz/chamber rectangular bottles · solid black opaque","Supplier custom label (factory program)",
         "Same opaque-black locking system with bigger 15oz chambers — fewer refills for a busy bath. AVIVA Solid White (~$78) is the smaller, cheaper sibling.","assets/img/shower-alt1.jpg"),
     opt("premium","Triple Wall Mount + Matte Bottles (brandable)","The Polished Jar","https://thepolishedjar.com/products/triple-wall-mount-for-soap-dispensers",
         "≈ $177","/ station","$108 bracket + bottles","min 1","One triple bracket + 3 bottles · matte-black or brass · choose matte (opaque) finish","In-house laser/UVDTF, or supplier-engraved",
         "The boutique, fully-brandable route — a triple bracket + bottles you can engrave or UVDTF yourself (pick the matte/opaque finish, not clear amber). Premium rustic look.","assets/img/shower-pj.png"),
   ]),
 # ---------------- BAR & TABLE ----------------
 dict(id="opener", cat="bar", name="Bottle Opener", tag="Brass & walnut",
   note="Three tiers: the walnut rec, the solid-brass showpiece you liked, and now cheap plain-stainless punches for coolers and take-homes — bare stainless takes a crisp dark laser mark (avoid nickel-plated churchkeys like the Winco CO-201; they mark gray). Also verified: The Local Branch leather-wrapped paddle ($28, two branding surfaces) and Civil Alchemy solid brass ($24). Restock watch: Standard Pattern hex opener ($32, Indiana-machined since 1937).",
   options=[
     opt("recommended","Wooden Bottle Opener — Walnut/Cherry + Stainless","BirchBarn Designs (USA)","https://birchbarndesigns.com/product/wood-bottle-opener/",
         "$20","/ ea","free engraving included","min 1","Stainless speed-opener faced with real hardwood · made in USA","Supplier engraves free — or in-house on the wood face",
         "Real walnut + solid stainless reads exactly 'Hill Country bar,' buyable as one, and the only pick that supports both supplier and in-house branding.","assets/img/opener-rec.jpg"),
     opt("premium","Ripple Opener — Solid Brass","Craighill (milled in Wisconsin)","https://craighill.co/products/ripple-opener",
         "$58.00","/ ea","qty 1 · B2B program available","min 1","Machined from a single brass rod · 7″ · a full half-pound · wave-profile grip · patinas naturally","In-house fiber laser along the shaft",
         "The heavy brass boutique-bar tool — sculptural, widely used in high-end hospitality, and a perfect laser canvas. The one guests pick up and weigh in their hand.","assets/img/opener-ripple.jpg",
         badge="The heavy brass one"),
     opt("value","Speed Bottle Opener / Bar Blade — Stainless","BarProducts.com","https://barproducts.com/products/speed-bottle-opener-bar-key-stainless-steel",
         "$0.99","/ ea","$15.28 / box of 12","min 1","Thick-gauge bare stainless · classic 7″ flat speed-opener · thumb ring","In-house fiber laser — dark anneal mark down the blade",
         "The archetypal bartender blade at under a buck — laser the seal and 'POCO LOCO RANCH' down the blade and it doubles as a take-home guest amenity.","assets/img/opener-speedblade.png",
         badge="Under a buck"),
     opt("alt","Tablecraft CP42 Churchkey / Can Punch — Stainless","WebstaurantStore","https://www.webstaurantstore.com/tablecraft-7-stainless-steel-bottle-opener-can-punch-cp42/808CP42.html",
         "$3.36","/ ea","case pack of 12","min 12","7″ uncoated stainless · cap lifter one end, triangular can punch the other","In-house laser on the long flat shank",
         "The vintage churchkey silhouette reads instantly 'ranch cooler and tallboys' — and unlike most churchkeys (nickel-plated), this one is bare stainless, so it lasers clean.","assets/img/opener-churchkey.jpg",
         badge="Ranch churchkey"),
     opt("alt","Rustic Cast Iron Wall-Mounted Opener","BarnwoodUSA","https://barnwoodusa.com/products/rustic-cast-iron-wall-mounted-bottle-opener",
         "$9.99","/ ea","sold individually","min 1","Solid cast iron, antique-brown, wall-mount fixture","Mount on an in-house engraved wood backer",
         "The most 'ranch fixture' look at under $10; brand it via a laser-engraved wood backer board.","assets/img/opener-alt2.jpg",
         badge="Cabin fixture"),
   ]),
 dict(id="napkins", cat="bar", name="Linen-Feel Cocktail Napkins", tag="Disposable · printed",
   note="Like the Badrutt's napkin: disposable linen-feel with a printed seal. Limelight's Linun stays the rec (min 25, $10 setup). New premium: a FOIL seal — honest flag: true airlaid + foil runs ~$0.77–0.83/ea at For Your Party (their 3-ply foil base is $0.48–0.54); Weddingstar's hand-stamped foil hits $0.44 on 3-ply. Also verified: Bella Lino Italian bamboo 'linen-feel' (Limelight, min 25, ~$1.08–2.50/ea printed) — the most genuinely linen-like sheet if you want the ultra-premium hand.",
   options=[
     opt("recommended","\"Linun\" Personalized Linen-Feel Cocktail Napkins","Limelight Paper","https://limelightpaper.com/products/linun-beverage-napkin",
         "≈ $0.34","/ napkin","$10 flat setup · min 25","min 25","Airlaid linen-feel · 5×5″ · one-time use · cream/natural","Supplier-printed (1-color or foil)",
         "Lowest MOQ (25) and a $10 flat setup — the closest match to the Badrutt's printed linen-feel napkin at boutique quantity.","assets/img/napkin-rec.jpg"),
     opt("premium","Linen-Like Cocktail Napkins — Foil-Stamped Seal","For Your Party","https://www.foryourparty.com/linen-cocktail-napkins",
         "≈ $0.77–0.83","/ napkin","min 50 · airlaid +$0.29 over 3-ply foil base","min 50","5×5″ airlaid cloth-texture · single or 2-color FOIL (gold/copper on white or oatmeal) · huge monogram template library","Supplier foil-stamps your seal",
         "The foil-on-linen-feel cocktail-hour napkin — a gold seal on oatmeal airlaid is the most Badrutt's thing on this page. Their 3-ply foil base is the $0.48–0.54 budget route.","assets/img/napkin-fyp.webp",
         badge="Foil seal"),
     opt("value","Personalized Foil-Stamped Napkins (3-ply)","Weddingstar","https://www.weddingstar.com/personalized-foil-printed-paper-napkins-but-first-cocktails.html",
         "$0.44","/ napkin","$21.99 / 50 + $4.95 setup","min 50","4.75″ 3-ply tissue · 13 foil colors incl. gold + copper · hand-stamped foil","Supplier foil-stamps custom text/monogram",
         "Real hand-stamped foil under fifty cents — trades the airlaid body for 3-ply, but the foil seal still reads upscale in the hand.","assets/img/napkin-weddingstar.jpg"),
     opt("alt","Linen Border Cocktail Napkins — Natural (blank)","Caspari","https://www.casparionline.com/products/linen-border-paper-cocktail-napkins-in-natural-20-per-package",
         "≈ $0.30","/ napkin","$5.95 / 20-pack","min 20","Triple-ply paper-linen · natural linen border · 5×5″","Blank: stamp seal in-house or use as-is",
         "The most premium-feeling blank in a true cream/natural tone at the lowest commitment — Caspari is the luxury name in paper-linen.","assets/img/napkin-alt1n.jpg"),
   ]),
 dict(id="coasters", cat="bar", name="Coasters — Leather & Blanks", tag="Saddle-shop leather",
   note="Upgraded to real saddle-shop leather as the lead. English bridle at 10/12 oz is the thick, waxy tier a boutique bar sets out — under $3/coaster as blanks you brand in-house. Slate stays as the cheap flexible blank (white laser etch, UVDTF-friendly). Runner-up verified: 23 Plus Hermann Oak 4″ square blanks, $14/4-pack.",
   options=[
     opt("recommended","Wickett & Craig English Bridle Coasters (4-pc)","Buckleguy (Newburyport, MA)","https://www.buckleguy.com/leather-coasters-wickett-craig-english-bridle-circle-chestnut-4pc-set/",
         "≈ $2.68","/ coaster","$10.70 / 4-pc set · bulk on request","min 1 set","Genuine Wickett & Craig English bridle · choose 8/10 oz or thick 10/12 oz (4–4.8mm) · Chestnut / Dark Brown / Burgundy · squares + Horween versions too","In-house stamp or fiber laser (Buckleguy also offers foil/logo service)",
         "English bridle at 10/12 oz for under $3 a coaster — thick, waxy, saddle-shop feel. The exact upgrade over thin veg-tan blanks.","assets/img/coaster-buckleguy.jpg"),
     opt("premium","Monogrammed Circle Coasters (set of 4)","Clayton & Crume (Louisville, KY)","https://claytonandcrume.com/products/monogrammed-circle-coasters",
         "≈ $11.25","/ coaster","$45 / set of 4 · ~2-week ship","min 1 set","Thick full-grain, water-resistant leather · hand-burnished edges · hand-stamped","Their stamping included; custom/corporate shop for branded runs",
         "The polished 'bourbon bar' finish with zero work on your end — burnished edges and hand-stamping from a Louisville leather house.","assets/img/coaster-claytoncrume.jpg"),
     opt("alt","Laser-Engraved Leather Coasters (set of 4)","Thirteen50 Leather (Texas)","https://www.thirteen50leather.com/products/leather-coasters-engraved",
         "$7.00","/ coaster","$28 / set of 4","min 1 set","4×4″ USA-tanned veg-tan (3–4 oz — thinner) · burnished waxed edges · 7 colors · lifetime warranty","They laser-engrave custom, or buy Natural and brand in-house",
         "Texas-made with finished edges at a fair price — the local-provenance story; note it's a thinner cut than the Buckleguy bridle.","assets/img/coaster-1350.jpg",
         badge="Texas maker"),
     opt("value","Slate Coaster — round or square","BulkLaser","https://bulklaser.com/products/slate-coaster",
         "$1.15","/ ea","no minimum","min 1","Natural black slate · 4×4″ · non-slip pads · round + square","In-house laser (white etch) or UVDTF",
         "Still the cheapest, most flexible blank — white-on-black etch, takes UVDTF, no minimum. Keep for the outdoor tables.","assets/img/coaster-rec.png"),
   ]),
 dict(id="coffeecups", cat="bar", name="Branded Coffee Cups", tag="White cup · black lid",
   note="Redone to the white-cup / black-lid spec (kraft retired). The rec is a single SKU that solves it: smooth white double-wall with the BLACK lid included, $27/100 — brand in-house with the seal stamp or UVDTF on the smooth white face. Supplier-printed routes verified at 50 and 100 MOQ. Runner-ups: UNICUP white double-wall full-print at 100 (configurator pricing); CustomPaperCup full-wrap $0.36/cup but min 500; Your Brand Cafe printed program now min 500.",
   options=[
     opt("recommended","Choice 12oz White Smooth Double-Wall Cup + BLACK Lid (100 sets)","WebstaurantStore","https://www.webstaurantstore.com/choice-12-oz-white-smooth-double-wall-paper-hot-cup-and-lid-pack/50012DWW100.html",
         "$0.27","/ serving","$26.99 / 100 cup+lid sets","min 100","12oz smooth white double-wall, no-PFAS · matching BLACK lid included in the pack · rolled rim","In-house: seal stamp or UVDTF on the smooth white face",
         "The exact spec in one SKU — clean white double-wall with the black lid already in the box, $27 per hundred. The smooth (not ripple) face is the best branding surface.","assets/img/cup-choicewhite.jpg",
         badge="White + black lid"),
     opt("alt","Restpresso White DW Cup + Black Lid (25-ct trial)","Restaurantware","https://www.restaurantware.com/products/restpresso-12-oz-white-paper-coffee-cup-double-wall-3-1-2-x-3-1-2-x-4-1-4-25-count-box",
         "$0.63","/ serving","~$16 tries 25 · drops to ~$0.36 by the case","min 25","Premium 'Restpresso' 12oz smooth white double-wall · black PS vented lid confirmed (fits 8–20oz)","In-house stamp / UVDTF",
         "The only true 25-unit entry — test the stamped white-cup look for about sixteen dollars before committing to anything.","assets/img/cup-restpresso.jpg",
         badge="Test at 25"),
     opt("premium","12oz White Double-Wall — Supplier-Printed + Black Dome Lid","The Cup Store","https://thecupstore.com/products/12-oz-custom-printed-recyclable-double-walled-paper-cup",
         "≈ $1.49","/ serving","$133 / 100 printed + $16 / 100 black dome lids","min 100","White double-wall, poly-lined · 1-color seal print (free second side) · black dome lid verified compatible","Supplier prints the seal",
         "The zero-labor version of the brief — your seal professionally printed on white double-wall, black dome lid on top, at exactly 100.","assets/img/cup-cupstorewhite.jpg",
         badge="Supplier-printed"),
     opt("alt","12oz FSC Full-Color Printed Cup + Black PLA Lid","DiscountMugs","https://www.discountmugs.com/product/ascpp6857-12-oz-fsc-full-color-paper-cup-with-lid/",
         "$2.16","/ serving","+$49 setup · lid included · black PLA lid confirmed","min 50","FSC white paper, made in USA · biodegradable PLA lid in black or white · near-full-wrap print · likely single-wall (confirm)","Supplier full-color print",
         "Lowest printed MOQ anywhere (50 sets) with the black lid bundled — the small-batch printed play.","assets/img/cup-discountmugs.jpg",
         badge="Full print at 50"),
     opt("value","Reliance 12oz Bright-White DW Cups + Black Sipper Dome Lids","Your Brand Cafe","https://www.yourbrandcafe.com/products/reliance-12oz-double-wall-coffee-cups/",
         "≈ $0.17","/ serving","$47.84 / 500 cups + $38.90 lids case","min 500","Bright-white double-wall · page links the matching BLACK sipper dome lids · blank","In-house stamp / UVDTF",
         "Cheapest per-serving white+black pairing anywhere — ~$87 outlay is a year of stock, if storing 500 isn't a problem.","assets/img/cup-ybcwhite.png",
         badge="Bulk value · 500"),
   ]),
 # ---------------- BEDROOM & COMFORT ----------------
 dict(id="blankets", cat="bedroom", name="Guest Throw Blankets", tag="Heritage mills · washable",
   note="Re-sourced from big-box waffle throws to heritage-mill grade. The play: Faribault or Pendleton on the bed-end (corner-embroider the seal in-house, or Pendleton embroiders for +$15/pc), and a stack of $23–26 El Paso camp blankets for porches, picnics and the firepit so the wool stays indoors. Restock watch: Pendleton Eco-Wise washable-wool fringed throw ($188) and Sackcloth & Ashes' Vintage Rust/Saddle plaids ($140). Faribault and In2Green both quote custom-program MOQs off-site — a two-line inquiry citing 'boutique ranch property, 10–25 units' gets real numbers.",
   options=[
     opt("recommended","Cabin Wool Throw, 50×72","Faribault Mill (Minnesota, est. 1865)","https://faribaultmill.com/products/cabin-wool-throw",
         "$195","/ ea","qty 1 · corporate/co-label program on quote","min 1","100% Merino-grade wool · flat cabin-stripe weave, whipstitch edge · MACHINE WASHABLE · Charcoal / Heather / Smoke","In-house corner embroidery · co-label program · leather patch",
         "The heritage-mill upgrade in one object: 160-year US mill, boutique-hotel hand feel, and washable wool — rare, and exactly what an Airbnb turnover needs.","assets/img/blanket-faribault.jpg"),
     opt("premium","Yakima Camp Throw, 54×66","Pendleton Woolen Mills","https://www.pendleton-usa.com/product/yakima-camp-throw/72266.html",
         "$188","/ ea","qty 1 · Pendleton embroiders +$15/pc","min 1","Pure virgin wool / cotton warp · US-woven camp stripe · Umber & Tobacco = dead-on rust/brown · dry clean","Pendleton monogram service (+$15) or in-house corner seal",
         "The iconic American camp blanket — instantly signals ranch luxury, the earthiest palette of the wools, and brand equity guests recognize. One drawback: dry-clean only.","assets/img/blanket-pendleton.jpg"),
     opt("alt","American Made Cotton Throw, 52×73 — Tan","Sackcloth & Ashes","https://sackclothandashes.com/products/american-made-cotton-tan",
         "$120","/ ea","qty 1 · wholesale program on contact","min 1","100% US-woven cotton · oatmeal/tan herringbone · machine washable · buy-one-give-one (one donated to a shelter per sale)","In-house corner embroidery or leather patch",
         "Washable woven US cotton at the friendliest premium price, and the give-back story is a great guest-book line.","assets/img/blanket-sackcloth.png"),
     opt("alt","Hotel Collection Knit Throw — Herringbone Taupe","In2Green (knit in USA)","https://www.in2green.com/collections/hotel-throw-blanket-collection",
         "$185","/ ea","qty 1 retail · hospitality program, low minimums on quote","min 1","Eco recycled-cotton knit · 50×60 · machine washable · 300+ recolorable patterns for custom runs","They knit your logo INTO the blanket, or add their leather patch",
         "The purpose-built hospitality vendor — the only one that will knit 'Poco Loco Ranch' into the fabric itself at boutique volume.","assets/img/blanket-in2green.jpg",
         badge="Knits the logo in"),
     opt("value","Classic Southwest Camp Blanket (~6×7 ft)","El Paso Saddleblanket Co. (El Paso, TX)","https://elpasosaddleblanket.com/collections/southwest-camp-blankets",
         "$23–26","/ ea","tiered: $26 qty 1 → $23 at 16 · no account gate","min 1","Oversized ~6×7 ft, ~6 lb · brushed acrylic serape in rust/brown/sand · Texas wholesale house","Stamped-leather patch (embroidery on acrylic pile reads budget)",
         "Honest tier: trading-post acrylic, not mill wool — but huge southwestern character at $23. The sacrificial porch/firepit/truck layer that protects the Faribaults.","assets/img/blanket-elpaso.jpg",
         badge="Porch & firepit tier"),
   ]),
 dict(id="sewing", cat="bedroom", name="Disposable Sewing Kit", tag="Paper / fabric — no plastic",
   note="Re-sourced to true low MOQs (the old picks needed 250–500). All non-plastic. Runner-ups verified: World Amenities KRAFT SACHET grooming kit — plastic-free, sewing kit inside, $0.54/kit at 100 on Amazon ($0.35 direct at 300, custom-brand runs offered); Luxe Comfort white paper-box kits ($0.165 at 100, but pre-printed with their own gold logo); Hotel Emporium kraft eco-sachet ($0.136, 500/case); Merveyl (EU) plain-kraft box at qty 1. Buyer beware, image-confirmed: Amazon's cheap '100-pack hotel sewing kits' (Tatuo, Honbay, safycaby) are bare thread-cards in CLEAR PLASTIC cello bags. Dead leads: Nomkin and Sunrise Amenities (domains dead), Appearus and Amenity Services (no sewing kits), Hunter and Gilchrist & Soames (plastic packaging).",
   options=[
     opt("recommended","Paper Matchbook Sewing Kit (100/case)","Hotel Supplies USA","https://www.hotelsuppliesusa.com/product/sewing-kit-matchbook-100-cs/",
         "$0.60","/ kit","$60 / case of 100","min 100","True paper matchbook · needles, threads, buttons, safety pin · flat stampable cover","In-house stamp / UVDTF over the cover",
         "The tidy matchbook format at exactly 100 minimum from a US supplier — under half the price ceiling. Confirm current cover print before decaling over it.","assets/img/sewing-matchbook.jpg",
         badge="Matchbook · min 100"),
     opt("alt","ECO Sciences Raw-Kraft Box Mending Kit","Branded Amenities (CA) / CustomAmenities (US)","https://brandedamenities.com/products/hotel-toiletries-sewing-kit-eco-sciences",
         "≈ $0.26","/ kit","≈ CAD $35 / 100 · US sister site $28/100 (restock watch)","min 100","Raw brown kraft upright carton, soy ink · 6-color thread card, needle, pins, 2 buttons","Best seal canvas of all: four uninterrupted kraft panels for stamp/UVDTF",
         "The exact Hill Country look — a plain kraft box that takes the ranch seal beautifully. Sole tradeoff: ships from Canada until the US site restocks.","assets/img/sewing-kraftbox.jpg",
         badge="Raw kraft canvas"),
     opt("value","Boxed Sewing Kit, premium paperboard (200/box)","HospitalityEmporium (Gardena, CA)","https://www.hospitalityemporium.com/products/sewing-kit-hotel-guest-room-amenity-premium-individual-box-packing-200s-box",
         "$0.18","/ kit","$36 / 200","min 200","Individual matte paperboard box (light gray) · 6 threads, needle, gold safety pin, 2 buttons","Stamp/UVDTF the flat lid (a 1–1.5″ seal covers their small logo)",
         "The safe, cheap US workhorse — $36 all-in from a hotel-amenity house, at 12% of the price ceiling.","assets/img/sewing-hospemporium.jpg"),
     opt("premium","'Hussif' Fabric Sewing Roll — customizable","FashionableFrolick (Etsy)","https://www.etsy.com/listing/505916892/design-your-own-18th-century",
         "$65–80","/ ea","roll vs. with-tools · confirm on Etsy","min 1","Linen/cotton/wool roll that ties shut · pick your fabrics · scissors, needles, winders, tape","Embroider the seal / add a leather tag",
         "The luxury, zero-packaging touch — a handmade fabric roll in your own fabrics for the primary suites. Very Badrutt's-in-the-drawer.","assets/img/sewing-hussif.jpg"),
   ]),
 # ---------------- WELCOME & DESK ----------------
 dict(id="pens", cat="welcome", name="Pens with Heft & Character", tag="Solid brass · qty 1",
   reference="Your exemplar: a substantial cream-lacquer barrel with gold trim — a real hotel pen, not promo SWAG.",
   note="Restructured around the ~$5–10 everyday tier you asked for, keeping two brass heroes on top. Fleet sibling with no fetchable photo but fully verified: Zebra F-301 — stainless barrel, $1.75/pen in Staples dozen boxes ($20.99) — the walk-off pen if even the F-701 feels precious. Parker Jotter only verified live at $16.88 (Goldspot), not the rumored $11. MUJI hex aluminum ($8.90) flagged: bare aluminum lasers light-gray, and it's marked final-sale. Still-verified brass from the last round if you want them: Fisher Cap-O-Matic $25.50, Traveler's Company $33, Kaweco Brass Sport $88.",
   options=[
     opt("recommended","Zebra F-701 — All-Stainless Retractable","Staples / Nordisco (bulk)","https://www.staples.com/zebra-f-701-retractable-ballpoint-pen-fine-point-black-ink-29411/product_710693",
         "$8.83","/ pen","$52.97 / box of 6 (Nordisco) · $11.49 single","min 1","100% stainless barrel + knurled grip · silent click · $1.50 refills · takes a Fisher pressurized refill with a trivial mod","In-house fiber laser — bare stainless anneals crisp black",
         "The pen-community budget icon — 'the $10 pen that feels like $50.' All metal, zero SWAG vibes, and stainless is the best-case laser surface. The everyday guest pen.","assets/img/pen-f701.jpg"),
     opt("alt","EnerGel Alloy RT — Aluminum Gel","Pentel of America (direct)","https://www.pentel.com/products/energel-alloy-gel-pen-black-barrel",
         "$9.46","/ pen","sale (reg. $11.13) · low stock on black","min 1","Aluminum-alloy barrel · retractable gel · ubiquitous $1.50 LR7 refills","In-house laser — black coating ablates to bright silver",
         "The best writer of the set — EnerGel smoothness in a metal body, and the black barrel gives a high-contrast silver mark.","assets/img/pen-energel.jpg",
         badge="The gel writer"),
     opt("alt","OHTO Horizon GS01 — Hex Aluminum","OHTO (Japan) · at Hunter Paper Co.","https://hunterpaperco.com/en-us/products/ohto-gs01-horizon-needlepoint-0-7mm-aluminium-pen",
         "$11.28","/ pen","qty 1 · JetPens quotes bulk","min 1","Hex aluminum body, brass clip + taper · side-release click · made in Japan · Parker G2-compatible refill","In-house laser on the flat hex facets — no rotary needed",
         "Japanese stationery-nerd credibility with an architectural hex look; the brass details echo your upper tier. Flat facets are the easiest laser target here.","assets/img/pen-ohto.jpg",
         badge="Design pick"),
     opt("premium","Fisher Space Pen Bullet — Raw Brass (#400RAW)","Goldspot Pens (also spacepen.com)","https://goldspot.com/products/fisher-bullet-space-400raw-classic-raw-brass-bullet-space-ballpoint-pen",
         "$30.60","/ pen","retail · Fisher dealer program for volume","min 1","Solid raw brass · 3.7″ capped, 5.3″ posted · pressurized refill writes at any angle","In-house fiber laser on the mid-barrel",
         "A 1948 American design icon (it's in MoMA) that patinas like a saddle fitting — the stolen pen becomes the souvenir. Keep it for the desks that deserve it.","assets/img/pen-fisherbullet.jpg",
         badge="The souvenir"),
     opt("premium","Kepler Pen — Machined Brass","Craighill (Brooklyn · milled in Wisconsin)","https://craighill.co/products/kepler-pen",
         "$78.00","/ pen","retail · real B2B / corporate program","min 1","Machined solid brass · 2.0 oz · 5″ click · Schmidt refill · For-Life guarantee","In-house laser on the upper barrel",
         "The writing-desk pen you'd find at an Auberge property — one per suite, not a fleet. Craighill's corporate program makes reorders painless.","assets/img/pen-kepler.jpg",
         badge="Writing-desk hero"),
   ]),
 dict(id="totes", cat="welcome", name="Waxed Canvas Tote Bags", tag="ARTIFACT look for less",
   note="The genuine waxed-canvas + full-grain leather + brass combo from US makers mostly lands $130+ (which is why ARTIFACT is $140). Rogue ($65, in stock) is the best 'same look for less.' Still want a plain cheap canvas tote to brand a stack? The BagzDepot 12oz USA natural (~$19) is the bulk play.",
   options=[
     opt("recommended","Waxed Canvas Tote — leather + antique brass","Rogue Industries","https://www.rogue-industries.com/products/waxed-canvas-tote-bag",
         "$65","/ ea","in stock · sold individually","min 1","Waxed canvas · full-grain leather strap · antique brass rivets · Brown/Green","In-house UVDTF / embroidered patch",
         "The ARTIFACT look at ~half price and buyable today — real leather + antique brass + waxed canvas in earthy brown/green.","assets/img/tote-rec.jpg"),
     opt("value","Market Tote in Waxed Canvas","Blue Claw Co. (USA)","https://www.blueclawco.com/products/market-tote-tan",
         "$49","/ ea","Made in USA · confirm restock","min 1","14.7oz waxed canvas · full-grain veg-tan leather · SOLID brass · Tan/Olive/Charcoal","In-house UVDTF / embroidered patch",
         "Spec-for-spec the closest ARTIFACT clone and cheapest — solid brass, US-made, perfect palette. Caveat: colors were sold out (set a restock alert).","assets/img/tote-alt1.jpg"),
     opt("alt","Utility Tote — 18oz Waxed (Made in USA)","Steele Canvas","https://www.steelecanvas.com/products/steele-utility-tote",
         "$129.95","/ ea","in stock · made to order","min 1","18oz waxed duck canvas · full-grain leather grips · Brown/Briquette","In-house UVDTF / embroidered patch",
         "The in-stock American-made step-up — heavyweight 18oz waxed canvas and full-grain leather; under the $140 ARTIFACT (no brass).","assets/img/tote-alt2.jpg"),
   ]),
 dict(id="bandana", cat="welcome", name="Custom Paisley Bandana", tag="Full-bleed cotton", subpage=("bandana.html","Full bandana breakdown — 16 vendors, methods & our pick"),
   note="Open the full breakdown above for all 16 vendors, the three approaches, and art/finishing notes. Short version: for full-bleed on COTTON at ~100, DTLA Print or Printology (US, all-over screen); for full-color digital on USA cotton with a published price, 4AllPromos ($11.76/100); for the easy/cheap poly route, Bandana Supply (local Sugar Land, TX, no min). bandana.com / NYBandana are defunct.",
   options=[
     opt("recommended","Custom All-Over Bandana — screen on cotton","DTLA Print (Vernon, CA)","https://www.dtlaprint.com/custom/bandanas/",
         "quote","/ ea","all-over · hemmed · MOQ ~24","min ~24","100% cotton, 22×22″ · edge-to-edge screen · hemmed 4 sides","Supplier all-over screen (your paisley + seal)",
         "The best practical full-bleed COTTON route — edge-to-edge on real cotton, hemmed 4 sides, US-made, at a low ~24 minimum. Built for a classic paisley + your seal.","assets/img/bandana-rec.jpg"),
     opt("premium","Authentic Rotary All-Over Cotton Paisley","The Bandanna Co. / Hav-A-Hank","https://thebandannacompany.com/custom-paisley/",
         "quote","/ ea","screen 50 · rotary all-over 3,000","min 50","100% cotton, USA-woven mill · true rotary all-over paisley","Supplier rotary/screen (full custom)",
         "The heirloom flagship — a genuine USA mill making authentic rotary all-over cotton paisley. The real thing; the all-over rotary look needs ~3,000.","assets/img/bandana-havahank.png"),
     opt("value","Open-Center Paisley Bandana (cotton)","OutfitYourLogo","https://www.outfityourlogo.com/detail.php?p=PAIS",
         "$4.97","/ ea","~$555 / 100 (incl. $58 setup)","min 100","100% cotton 22×22″ · stock paisley + 10×10 blank center","Supplier screen-print into the center",
         "The cheap cotton route if you don't need edge-to-edge — traditional paisley with your seal in the open center; every earthy color.","assets/img/bandana-outfit.jpg"),
   ]),
 dict(id="menucovers", cat="welcome", name="Hard Embossed Menu Covers", tag="Rigid · foil-stamped",
   reference="Like your Badrutt's 'In-Room Dining' and 'Le Restaurant' menus — permanent rigid hardcovers, foil-stamped or blind-debossed. Use for an in-room dining menu, welcome book, guest directory, or wine list.",
   note="Supplier foil-stamps/embosses these (not an in-house job). Burgundy + gold foil matches the 'In-Room Dining' look; a sage/tan linen with blind deboss + gold matches 'Le Restaurant.' For a refreshable wine list, choose a screw-post or ring version. Bespoke tier: Hartnack & Co (UK); true bookbindery: Monastery Hill.",
   options=[
     opt("recommended","Standard Hardcover Menu Cover (casebound)","Menu Cover Depot","https://www.menucoverdepot.com/formal-menu-covers/standard-hardcover-menu-covers.html",
         "≈ $57","/ cover","+$90 foil die · ~$1,000 for 15","min 15","True casebound — book cloth over rigid board · burgundy/black/brown/green · slip-in corners","Supplier gold/silver foil or blind deboss",
         "The closest match to your burgundy gold-foil 'In-Room Dining' menu — genuinely rigid, a real foil die, burgundy in stock, the lowest verified hardback minimum (15).","assets/img/menucover-rec.jpg"),
     opt("value","Summit Linen Hardback Menu Cover","Menu Cover Central","https://menucovercentral.com/menu-covers-with-diploma-corners/summit-linen-menu-covers/",
         "$14.95+","/ cover","foil/deboss die by quote · sub-25 min","min ~10","True hardback casebound · textured LINEN cloth · many sizes · corner/bar inserts","Supplier foil-stamp or blind deboss",
         "The actual linen/cloth hardcover at the lowest per-unit and most flexible quantity — best for a sage/tan linen welcome book with a blind-deboss + gold crest.","assets/img/menucover-alt1.jpg"),
     opt("alt","Casebound Leatherette Menu Cover","Menu Shoppe","https://www.menushoppe.com/leatherette-menu-covers",
         "quote","/ cover","foil/deboss included · die fee by quote","quote","Rigid bookbinder's cloth over board · 14 colors · screw-post & ring versions","Supplier foil-stamp or blind deboss",
         "Widest format range — including screw-post/ring casebound for an easily refreshable wine list — while still a true rigid hardcover with supplier foil.","assets/img/menucover-alt2.png"),
   ]),
 dict(id="stationery", cat="welcome", name="Hotel Stationery — Cards & Envelopes", tag="Bordered · crested",
   reference="Like your Badrutt's desk set: bordered correspondence cards with a small crest and matching envelopes, in cream/soft tones. (Embossing/foil on paper is a supplier job, not in-house.) Open any card's 'Learn more' for how that service works and what to watch for.",
   note="More big players: Crane & Co. 100% cotton bordered cards + envelopes, box of 10, $32–34 (crane.com — photos hotlink-protected, so not shown). CatPrint (catprint.com) — no minimum, real foil stamping + matching envelopes, open to small businesses (foil is email-to-order; request a card quote). Vistaprint — cheapest high-volume, min 1, but no foil/emboss on flat cards.",
   options=[
     opt("recommended","Bordered Correspondence Cards + Envelopes","Merrimade","https://www.merrimade.com/bordered-correspondence-cards.html",
         "$3.00","/ card","$75 / box of 25 (incl. 25 envelopes)","min 25","Bordered card · raised-ink your crest/text · white/ivory + red/navy/green border · 6.25×4.5″","Supplier raised-ink print of your crest",
         "Bordered hotel-style cards with your crest printed and matching envelopes included, at a low 25 minimum — the closest turnkey branded match to the Badrutt's set.","assets/img/stationery-rec.jpg",
         learn="<span class='hd'>How it works</span>You choose card color (white/ivory/blue), border color (red/navy/green), a typeface and ink color, and upload your crest + wording. They print by <b>raised-ink thermography</b> — a clear resin is fused over the ink so the design sits raised and glossy (the engraved look at a fraction of the cost). <b>Matching printed envelopes are included.</b><span class='hd'>What to know</span><ul><li><b>1 box = 25 cards + 25 envelopes, $75</b> (~$3/card) — that's the minimum.</li><li>Raised-ink is <b>one ink color</b> per design — ideal for a single-color seal.</li><li>Envelope return-address printing is an add-on.</li><li><b>Production ~21–28 business days</b> + shipping, so order ahead.</li><li>Card 6.25×4.5″; optional lined envelopes.</li></ul><span class='hd'>Pro tip</span>Ivory stock + a warm-black ink reads most Hill-Country. Raised-ink isn't a true deboss (the back stays flat), but it's the best value for a printed crest."),
     opt("premium","Luxe Note Cards (big-player, modern)","MOO","https://www.moo.com/us/luxe-notecards",
         "≈ $2.21","/ card","$221 / 100 · free envelopes · min 10","min 10","Mohawk Superfine 32pt · colored seam (8 colors) · A6 · digital crest","Supplier digital print (foil via MOO Foil Invitations)",
         "The big, easy, modern printer — upload your crest, live pricing, ships in ~2 days, envelopes free. Use MOO Foil Invitations for a true gold-foil crest.","assets/img/stationery-moo.jpg",
         learn="<span class='hd'>How it works</span>MOO is the big, modern, self-serve printer — online editor, upload your art, live price calculator, fast turnaround. The premium card is <b>Luxe Note Cards</b>: flat A6 cards on Mohawk Superfine 32pt with a <b>colored seam</b> through the middle (8 colors) and <b>free white envelopes</b>, minimum 10.<span class='hd'>What to know</span><ul><li><b>Luxe Note Cards ≈ $2.21/card at 100</b> (min 10), envelopes free, ships ~2 business days, no setup fee.</li><li><b>Foil & letterpress are NOT on note cards</b> — only business cards & invitations. For a true <b>gold-foil crest on a flat A6 card</b>, order MOO <b>Foil Invitations</b> (≈ $2.01/card at 100, no die fee).</li><li>Foil art needs a <b>separate B&amp;W vector PDF</b> marking the foil area, and foil must cover <b>under 50%</b> of the card (accents, not solid blocks).</li><li><b>Printfinity</b>: every card in a pack can be a different design at no charge.</li></ul><span class='hd'>Pro tip</span>Use Luxe Note Cards for an everyday crested card; switch to Foil Invitations when you want the gold-foil hotel look — both include envelopes with no die fee."),
     opt("value","Embossed Border Correspondence Cards (#3120)","American Stationery","https://www.americanstationery.com/embossed-border-correspondence-cards-7254.html",
         "≈ $2.24","/ card","$55.95 / box of 25","min 25","Embossed raised border + personalization · white/ivory · envelopes included · 6.25×4.5″","Supplier emboss + print",
         "A true embossed border plus your printed crest at the lowest branded price — the most 'embossed' look of the set.","assets/img/stationery-alt1.jpg",
         learn="<span class='hd'>How it works</span>A long-running US social-stationery house. You pick the <b>embossed border</b> style and add your crest/wording; they <b>emboss</b> the border (an inkless raised relief pressed into the paper) and print your personalization. <b>Matching envelopes included.</b><span class='hd'>What to know</span><ul><li><b>$55.95 / box of 25</b> (~$2.24/card), minimum 1 box — the cheapest branded route.</li><li>Embossing = a tactile raised frame with no ink; subtle and elegant.</li><li>White or ivory; card 6.25×4.5″.</li><li>Typical lead time ~1–2 weeks.</li></ul><span class='hd'>Pro tip</span>The embossed border gives the 'fine hotel' feel cheaply; pair it with a small printed crest. Best for a larger in-room run without a big spend."),
     opt("alt","A7 Ecru Embossed Panel Cards (blank)","LCI Paper","https://lcipaper.com/a7-panel-card-lci-smooth-80lb-blank-cards-ecru/pd/E7PC-80.html",
         "≈ $0.30","/ card","$14.78 / 50 · envelopes ~$8.91/25","min 50","Blind-embossed panel border · ecru · 80lb · blank, laser/inkjet printable","In-house: print/stamp your crest",
         "The cheapest path — premium blind-embossed bordered blanks you run your own crest onto (or letterpress).","assets/img/stationery-alt2.jpg",
         learn="<span class='hd'>How it works</span>The <b>DIY blank</b> path: buy premium <b>blind-embossed panel cards</b> (a raised frame + recessed center panel, no ink) and add your crest yourself — run them through a laser/inkjet printer, hand-stamp them, or take them to a local letterpress for a foil/letterpress crest.<span class='hd'>What to know</span><ul><li><b>$14.78 / 50 (~$0.30/card)</b>; matching A7 envelopes are <b>separate</b> (~$8.91/25).</li><li>80lb cover, ecru, smooth wood-pulp (not cotton); A7 = 5⅛×7″; acid-free.</li><li>The blind-embossed panel reads upscale even before you add anything.</li></ul><span class='hd'>Pro tip</span>Cheapest path and full control. For the richest result, have a local letterpress foil-stamp your seal into the panel — you supply the blanks, they run the die."),
   ]),
 dict(id="seedenvelopes", cat="welcome", name="Branded Seed Envelopes", tag="Take-home gift",
   note="Easiest prefilled-with-seeds path: Wonder Flora prints your seal AND fills with real Texas bluebonnet seed (MOQ 20). Scale cheaper at 100+ with Earthly Goods. Fully DIY: Seed Needs kraft envelopes (~$0.20) you stamp + fill yourself. Also worth a look: Botanical PaperWorks plantable seed-paper favors (plant the whole card).",
   options=[
     opt("recommended","Custom Bluebonnet Seed Packet Favors","Wonder Flora","https://www.wonderflorashop.com/shop/p/custom-seed-packet-favors-bluebonnet",
         "$3.00","/ packet","prefilled · personalization incl.","min 20","PREFILLED w/ real Texas bluebonnet seed · premium hand-folded paper · scalloped flap","Supplier-printed your seal",
         "The easiest prefilled path and the most on-brand — they print your seal AND fill with Texas bluebonnet (the state flower). MOQ just 20.","assets/img/seed-rec.jpg"),
     opt("value","Texas Bluebonnet Personalized Seed Packets","Earthly Goods","https://www.earthlygoods.com/texas-bluebonnet-personalized-seed-packets.html",
         "$2.50","/ packet","$1.35 @250 · free 4-color + setup","min 100","PREFILLED bluebonnet seed · recycled paper, soy ink · 3.25×4.5″","Supplier-printed (free 4-color)",
         "The best prefilled value if you scale — under $1.35 at 250+, free print + setup, genuinely eco/rustic recycled paper.","assets/img/seed-alt1.jpg"),
     opt("alt","Proterra Kraft Seed Envelopes (empty)","Seed Needs","https://www.seedneeds.com/products/kraft-seed-envelopes-2b",
         "≈ $0.20","/ envelope","$8.99 / 50-pack","min 50","EMPTY kraft, self-seal · 3.25×4.5″ · you fill with your own seed","In-house: stamp/print + fill",
         "Lowest cost and full control — a true kraft 'garden packet' look; stamp your seal and fill with locally-sourced bluebonnet. Trade-off is the hand-labor.","assets/img/seed-alt2.jpg"),
   ]),
 dict(id="postcards", cat="welcome", name="Branded Postcards", tag="Ranch photography",
   note="Only true mailable postcards (writable/addressable back, no envelope) come from Nations Photo Lab and Artifact Uprising — Mpix's 'postcard' is really a flat card with envelopes. For a foil / painted-edge premium card, MOO and Jukebox also apply (see the Stationery item's Learn-more).",
   options=[
     opt("recommended","Create-Your-Own Photo Postcard","Nations Photo Lab","https://www.nationsphotolab.com/products/cards-create-your-own",
         "≈ $1.72","/ card","$46.75 / 25 (promos drop it)","min 25","True mailable postcard · uncoated writable backs (Signature Matte / Cotton / Smooth) · many stocks","Supplier-printed (your photo + seal)",
         "Cheapest true mailable postcard, lowest MOQ (25), widest stock choice incl. uncoated writable backs — ranch photo front, seal + message on the back.","assets/img/postcard-rec.jpg"),
     opt("premium","Custom Photo Postcards (Classic Recycled)","Artifact Uprising","https://www.artifactuprising.com/photo-cards",
         "≈ $1.85","/ card","sets of 10–300 · no envelope needed","min 10","Heavyweight 100% recycled, eggshell matte · 5×3.5 or 6×4 · Photo+Text back","Supplier-printed (premium)",
         "The luxury pick — thick, tactile recycled stock and a true no-envelope postcard with a Photo+Text back. MOQ just 10.","assets/img/postcard-alt1.jpg"),
     opt("alt","Signature Flat Photo Card","Mpix","https://www.mpix.com/cards/diy/custom-horizontal-flat-card",
         "≈ $1.86","/ card","from 50 ($93)","min 50","Photo-lab quality, ultra-thick 130# Signature stock · 4×5.5–6×8","Supplier-printed (your photo + seal)",
         "Photo-lab quality for an enclosed flat card (ships with envelopes) — not a mail-the-back postcard, but the richest photo reproduction.","assets/img/postcard-alt2.jpg"),
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
 dict(id="boottray", cat="outdoor", name="Entry Boot Tray", tag="Home for the boot jack",
   note="New item per request — the tray the boot jack (and guest boots) lives in at the door. Sizing target ~32×16″ fits 2–3 pairs plus the jack. Runner-ups: Gardener's Supply recycled tray ($29.99 — great hidden liner inside the wood tray), their rubber-grid insert + river stones for the spa look, and Target Hearth & Hand black metal tray (~$50, page not independently verified). Etsy cedar makers exist but block verification — worth a manual browse for a true cedar tray.",
   options=[
     opt("recommended","Everyspace Recycled Waterhog Boot Mat — Camel","L.L.Bean","https://www.llbean.com/llb/shop/122708?page=everyspace-recycled-waterhog-boot-mat-large-16in-x-310in",
         "$34.95","/ ea","qty 1 · Large 18×46″ runs more","min 1","90%+ recycled 24oz polyester over rubber · raised water-dam border · 3/8″ thick · 15×35.5″ · Camel / Charcoal / Bluestone / Grey","Stamped-leather tag laced to the boot jack that sits on it",
         "The gold standard under muddy boots — holds 1.5 gal/sq yd behind its dam. Camel sits quietly under leather boots instead of going utility-gray.","assets/img/boottray-waterhog.jpg"),
     opt("premium","Double Circles Galvanized Steel Boot Tray","Plow & Hearth","https://plowhearth.com/products/cbbz8x",
         "$79.95","/ ea","qty 1 · preorder, ships ~Jul 7","min 1","Galvanized steel, dark hand-burnished zinc · embossed circle motif · 30×13″ with 2″ water lip","UVDTF a corner of the zinc rim, or rivet a lasered stainless nameplate",
         "Real-steel farmhouse with a 2″ lip — the dark burnished zinc reads boutique ranch, not feed store, and it photographs beautifully for the listing.","assets/img/boottray-plow.jpg",
         badge="Farmhouse steel"),
     opt("alt","Rustic Wooden Boot Tray — Solid Pine","L.L.Bean","https://www.llbean.com/llb/shop/128504?page=rustic-wooden-boot-tray",
         "$210","/ ea","qty 1 · ~3–4 wk delivery","min 1","Solid pine, dark natural, low-shine lacquer · 37.5×16.6×3.5″ · furniture-grade","Fiber-laser or hot-brand the ranch mark straight into the pine rail",
         "The only tray you can put the brand directly into — entry furniture, not a drip pan. Line it with the $30 Gardener's Supply tray and it stays pristine.","assets/img/boottray-wood.jpg",
         badge="Engraveable statement"),
   ]),
 dict(id="umbrellaholder", cat="outdoor", name="Umbrella Stand", tag="Cheaper + brass option",
   note="Cheaper than the $191 brass: rustic black/galvanized 'umbrella-shape' tapered stands at ~$110 with great flat branding panels (below). Ultra-budget UVDTF base: a galvanized bucket (~$10, Bucket Outlet) or IKEA NIPÅSEN ($12.99) — but open/round shapes give little branding area. Genuine solid brass stays vintage-only (Chairish, ~$450).",
   options=[
     opt("recommended","Black Metal Umbrella Stand, 27″ — brass handle","Globedecor","https://globedecor.com/product/black-metal-abstract-umbrella-stand-with-gold-handle-27/",
         "$109.99","/ ea","in stock · sold individually","min 1","Matte-black tapered tube · brass crook handle + gold interior · 27″H · ~3.7 lb","In-house UVDTF (white seal pops) or laser",
         "~$80 cheaper than the brass Glaro, the black + brass matches the seal, and its large flat black panels are the easiest of these to brand cleanly.","assets/img/umbrellaholder-rec.jpg"),
     opt("alt","Galvanized Metal Umbrella Stand, 28″","Globedecor","https://globedecor.com/product/metal-umbrella-stand-galvanized-gray-28/",
         "$109.99","/ ea","in stock (1 left)","min 1","Galvanized tapered tube · copper/bronze base + crook handle · 28″H","In-house UVDTF on the panels",
         "The most rustic Hill-Country look (galvanized + aged copper) at the same low price; UVDTF the smooth panels (galvanized resists clean laser color).","assets/img/umbrellaholder-alt1.jpg"),
     opt("premium","Glaro 921 Satin Brass Cylinder (the brass upgrade)","Glaro / Trashcans Unlimited","https://trashcansunlimited.com/satin-brass-or-aluminum-umbrella-stand-921-by-glaro/",
         "$191.45","/ ea","made in USA · sold individually","min 1","Clean 23″H × 9″ brass-finish cylinder · tarnish-proof · water tray","In-house laser-engrave / UVDTF",
         "If you still want the true clean 'brass tube,' this is it — commercial-grade and tarnish-proof so an engraved seal stays sharp. The premium upgrade.","assets/img/umbrellaholder-alt2.jpg"),
   ]),
 dict(id="umbrellas", cat="outdoor", name="Long Umbrellas", tag="Doorman-grade",
   note="Re-sourced from promo grade to doorman grade. Suggested play: 8× Totes (mixed Black / British Tan / Olive, crooks engraved in-house + leather tags) plus 2–3× GustBuster Doorman as the oversized hero pieces ≈ $475–570 all-in. Restock watch: ShedRain Vintage manual wood stick ($50, both colorways sold out). The splurge if you ever want one house showpiece: London Undercover City Gent (~$115–139 at US retail) — handmade, maple crook, brass fittings.",
   options=[
     opt("recommended","Classic Solid Wood Stick Umbrella (auto, 48″)","Totes (direct)","https://www.totes.com/products/blue-line-auto-wooden-stick-umbrella",
         "$36.00","/ ea","retail, any qty","min 1","48″ arc · solid wood shaft + wood crook · steel frame · auto-open · Black / British Tan / Olive in stock","In-house: engrave the wood crook + stamped leather tag",
         "The archetypal hotel-guest wood-crook stick at $36 in exactly the earthy solids you want — a legacy US umbrella brand, not promo SWAG. Buy 8–10, engrave, done.","assets/img/umbrella-totes.jpg"),
     opt("premium","Doorman 62″ Double-Canopy Umbrella","GustBuster · Golf Umbrella Heaven (authorized dealer)","https://www.golfumbrellaheaven.com/shop/shop-by-manufacturer/gustbuster-shop-by-manufacturer/gustbuster-doorman-62-umbrella/",
         "$94.00","/ ea","qty 1 · 20 in stock at check","min 1","True doorman scale: 62″ double canopy · 55-mph wind-tested · fiberglass shaft · lifetime warranty","Stamped-leather tag laced to the handle / embroidered sleeve",
         "Literally the umbrella named for the job — the huge two-guest canopy makes borrowing one at the door feel like a Ritz doorman moment. 2–3 as the stand's hero slots.","assets/img/umbrella-gustbuster.jpg",
         badge="The doorman piece"),
     opt("value","#4479 Premium All-Wood Guest Umbrella (48″)","tagUmbrella / The American Umbrella Co.","https://www.tagumbrella.com/hotel-guest-umbrellas",
         "$31.10","/ ea","≈$746 / 24 · $28.30 at 48","min 24","Wood J-crook, wood shaft, wood tips · fiberglass ribs · Black / Dark Brown / Dark Green / Taupe","Factory tie-band imprint — or engrave crooks in-house",
         "The genuine hotel-channel answer — the same all-wood guest umbrella Westin and Virgin Hotels stock, priced so one order outfits the stand plus loss spares.","assets/img/umbrella-tag.jpg",
         badge="Hotel channel · min 24"),
     opt("alt","Tartan Walker Umbrella (wood crook)","Barbour USA","https://www.barbour.com/us/barbour-tartan-walker-umbrella-uac0202tn11",
         "$80.00","/ ea","retail, qty 1","min 1","Full-length walker · ~36″ span · wooden crook · Barbour Classic Tartan (warm tan/olive)","Engrave the crook + leather tag",
         "One or two character pieces for the stand — heritage-country tartan guests recognize as quality, and it suits a Hill Country ranch surprisingly well.","assets/img/umbrella-barbour.jpg"),
   ]),
 dict(id="cornhole", cat="outdoor", name="Cornhole Boards (blank for DTF)", tag="DTF-ready blanks",
   note="You'll DTF the seal yourself, so these ship blank. Raw 3/4″ Baltic birch (CornholeAce) is the flattest, most premium transfer base — a light clear seal first improves UVDTF grip and weatherproofs it. Runner-up: Slick Woody's vinyl-coated white top is transfer-ready with no prep (confirm stock).",
   options=[
     opt("recommended","Plain Unfinished Set — 3/4″ Baltic Birch (No Poly)","CornholeAce (USA)","https://cornholeace.com/products/plain-unfinished-cornhole-board-set-professional-no-poly",
         "$249.99","/ set","regulation 2×4 · qty 1","min 1","2 boards · 3/4″ Baltic birch top + frame · folding legs · raw, no graphics","In-house DTF/UVDTF (light seal first)",
         "The only verified in-stock true 3/4″ Baltic birch blank with no poly and no graphics — the smoothest, most premium DTF base, tournament-grade.","assets/img/cornhole-rec.jpg"),
     opt("value","4×2 Natural Wood Set + Case","GoSports","https://www.playgosports.com/products/gosports-4x2-regulation-size-wooden-cornhole-boards-set-includes-carrying-case-and-bean-bags-choose-your-colors-over-100-color-combinations",
         "$129.99","/ set","regulation 4×2 · qty 1","min 1","2 boards · 1/2″ varnished cabinet-grade ply · carry case (bags separate)","In-house DTF (scuff-sand first)",
         "Lowest-price in-stock set from a reputable brand; the light varnished top takes a DTF transfer well after a quick scuff-sand.","assets/img/cornhole-alt1.jpg"),
     opt("alt","Quick-Ship Blank Top — 3/4″ Baltic Birch (No Clear Coat)","Dirty Bags Cornhole","https://dirtybagscornhole.com/products/quick-ship-cornhole-boards-blank-top-boards-no-clear-coat",
         "$249","/ set","regulation 2×4 · confirm restock","min 1","2 boards · 3/4″ Baltic birch · blank top, no clear coat — built for custom art","In-house DTF/UVDTF",
         "Purpose-built blank top for custom artwork (no clear coat to fight) — ideal for DTF. Was sold out at research; confirm restock.","assets/img/cornhole-alt2.webp"),
   ]),
 dict(id="strawhats", cat="outdoor", name="Branded Straw Hats", tag="Texas-made + wholesale blanks",
   note="Two ways to go: a showpiece (SunBody — real Houston-made palm) or a wholesale blank you band in-house. The value cluster is Park Wholesale's Mega Cap line — same vendor and price tier as the toyo you liked, in natural, tea-stained, caramel and chocolate. Buying blanks needs no wholesale account or 12-pc minimum (that only applies to their custom-logo decoration). Straw often shows 'On Backorder' in mid-summer, so capwholesalers.com and Mega Cap Inc (the maker) are verified stock fallbacks — see 'Learn more' on the Outback Toyo. Local experiential idea: a Rancher Hat Bar pop-up, or Gruene Hat Co (New Braunfels, ~25 min) brands hats on-site.",
   options=[
     opt("recommended","Palm Western Hat (real Guatemalan palm)","SunBody Hats (Houston, TX)","https://www.sunbody.com/Hats/?pt=1",
         "$46.65","/ hat","retail; wholesale on approved acct","min 1","Real palm leaf · cattleman / open-crown / Gus · UPF 50+ · sizes 5–8","In-house leather seal patch + custom band",
         "The single most on-brand piece — a genuine Texas (Houston) maker, authentic palm Western hats, UPF 50+. The showpiece above the wholesale blanks.","assets/img/hat-rec.webp"),
     opt("value","Mega Cap 8178 Outback Toyo Cowboy Hat (blank)","The Park Wholesale","https://theparkwholesale.com/collections/wholesale-cowboy-hats/products/mega-cap-8178-outback-toyo-cowboy-hat",
         "$13.40","/ hat","Blank · sold individually","min ~1","Toyo straw · outback western · vented crown · decorative band (swap your own) · Natural / Brown · one size","In-house seal patch / UVDTF + custom band",
         "The actual Outback Toyo — same family and price as the hat you liked — shown here in warm Brown with a vented crown. The most familiar pick of the set.","assets/img/hat-8178.jpg",
         badge="Closest to what you liked",
         learn="<span class='hd'>How to actually buy these</span>Park Wholesale's Mega Cap straw hats sell as plain <b>blanks</b> — no wholesale account, business license, or 12-piece minimum required. The 12-pc headwear minimum only applies if <i>they</i> decorate the hats; because you brand in-house you can order small quantities (the 8178 is sold individually; a solid-color dozen pack is also offered).<span class='hd'>Stock caveat</span>Straw routinely shows <b>&lsquo;On Backorder&rsquo;</b> through mid-summer (a notify-me button appears). It restocks — but if you need hats now, the same Mega Cap SKUs are carried by <a href='https://www.capwholesalers.com/straw-hats-c223' target='_blank' rel='noopener'>capwholesalers.com</a> (the 8034 natural was in stock there, ~12-pc min) and you can order straight from the maker, <a href='https://www.megacapinc.com/product/straw-hats/cowboy-straw-hats/western-tea-stained-straw' target='_blank' rel='noopener'>Mega Cap Inc</a> (trade login for pricing).<span class='hd'>Branding it</span>The crown front takes a <b>stamped-leather seal patch</b>, an embroidered patch, or UVDTF; the black-and-white seal reads cleanly on natural, caramel and tea-stained straw. Add or swap a custom woven/leather band to finish. Prototype the patch at qty&nbsp;1 via Crafters Lab (below) before a full run.<span class='hd'>Fit</span>Most are one-size (elastic sweatband). For real guest sizing, the <b>Otto 129-1326</b> below comes in M (58&nbsp;cm) and L (60&nbsp;cm)."),
     opt("value","Mega Cap 8034 Cowboy Straw Hat (Natural, 4″ brim)","The Park Wholesale","https://theparkwholesale.com/collections/wholesale-cowboy-hats/products/mega-cap-8034-cowboy-straw-hat",
         "$12.50","/ hat","Blank · no min at Park","min ~1","100% straw · natural · 4″ brim · braided rope chin cord · one size","In-house seal patch / UVDTF — max contrast on natural",
         "Closest match to the toyo you liked and the cleanest natural canvas. Confirmed in stock at capwholesalers.com when Park is backordered.","assets/img/hat-8034.jpg",
         badge="Cleanest natural"),
     opt("value","Mega Cap 8241 Western Toyo (Caramel / Chocolate)","The Park Wholesale","https://theparkwholesale.com/collections/wholesale-cowboy-hats/products/mega-cap-8241-western-toyo-cowboy-hat",
         "$13.25","/ hat","Blank · no wholesale account","min ~1","100% paper straw (toyo) · Caramel / Chocolate / Black · one size","In-house leather seal patch + custom band",
         "Same toyo in richer Caramel / Chocolate earthy tones — the most upscale-rustic of the toyos, and the B&W seal still reads clean on the warm crown.","assets/img/hat-8241.jpg",
         badge="Richest earthy tones"),
     opt("value","Mega Cap 8242 Western Tea-Stained Straw Hat","The Park Wholesale","https://theparkwholesale.com/collections/wholesale-cowboy-hats/products/mega-cap-8242-western-tea-stained-straw-hat",
         "$7.99","/ hat","Blank · sold individually","min ~1","100% straw · tea-stained (reads light / natural in the catalog photo) · beaded band · one size","Stamped-leather or embroidered seal patch",
         "The cheapest verified blank — a lightly tea-stained straw with a beaded band, simple to band and patch in-house.","assets/img/hat-8242.jpg",
         badge="Lowest cost"),
     opt("value","Mega Cap 8160 Outback Raffia Cowboy Hat","The Park Wholesale","https://theparkwholesale.com/collections/wholesale-cowboy-hats/products/mega-cap-8160-outback-raffia-cowboy-hat",
         "$15.99","/ hat","Blank · no wholesale account","min ~1","Raffia straw · leather chin cord · Natural / tea-stain Brown · one size","Stamped-leather seal patch + leather / woven band",
         "Coarser raffia weave and a real leather chin cord read the most rustic and authentic — the most premium-feeling blank of the set, still under $16.","assets/img/hat-8160.jpg",
         badge="Most rustic"),
     opt("value","Otto 129-1326 Straw Cowboy Hat (sized M / L)","The Park Wholesale","https://theparkwholesale.com/collections/wholesale-cowboy-hats/products/otto-129-1326-straw-cowboy-hat-with-adjustable-cort-129-1326",
         "$15.94","/ hat","Blank · band sold separately","M 58 / L 60 cm","100% natural straw · pre-curved 4″ brim · adjustable cord · two sizes","Built for a custom band + in-house seal patch",
         "A different brand for variety and the only one with real M / L sizing — a better guest fit, and explicitly band-ready (band sold separately).","assets/img/hat-otto.jpg",
         badge="Sized M / L"),
     opt("alt","Leather-Patch Straw Cowboy Hat (turnkey)","Crafters Lab","https://crafterslab.com/products/custom-leather-patch-otto-cap-straw-cowboy",
         "$49.99","/ hat","no real minimum","min 1","Natural straw, 4″ brim · M/L · custom leather patch done for you","Supplier engraves + sews your seal patch",
         "Lowest-friction branded hat — your seal on a veg-tan leather patch, qty 1, done for you. Use it to prototype the look before a wholesale run.","assets/img/hat-alt1.jpg"),
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
.learn{margin:0 0 12px}
.learn summary{cursor:pointer;font-size:12px;font-weight:800;letter-spacing:.3px;color:var(--rust);list-style:none;padding:8px 11px;background:#f6e7d6;border:1px solid #ecdcc0;border-radius:9px;display:flex;align-items:center;gap:6px}
.learn summary::-webkit-details-marker{display:none}
.learn summary::after{content:"▾";margin-left:auto;transition:transform .15s}
.learn[open] summary{border-radius:9px 9px 0 0}
.learn[open] summary::after{transform:rotate(180deg)}
.learn .ld{font-size:12px;line-height:1.5;color:#5a4836;padding:11px 12px;border:1px solid #ecdcc0;border-top:none;border-radius:0 0 9px 9px;background:#fffdf7}
.learn .ld b{color:var(--bark)}.learn .ld ul{margin:7px 0 0;padding-left:16px}.learn .ld li{margin:4px 0}
.learn .ld .hd{font-weight:800;color:var(--espresso);display:block;margin:9px 0 3px;font-size:11.5px;text-transform:uppercase;letter-spacing:.5px}
.btn{margin-top:auto;display:block;text-align:center;background:var(--espresso);color:#fff;padding:10px 12px;border-radius:9px;font-weight:700;font-size:13px}
.btn:hover{background:var(--rust);text-decoration:none}
.note{font-size:12.5px;color:#6a5848;background:#faf4e8;border:1px dashed var(--line);border-radius:10px;padding:10px 13px;margin:13px 0 0}.note b{color:var(--bark)}
footer{background:var(--espresso);color:#d9c7ac;padding:24px 0 32px;margin-top:30px;border-top:4px solid var(--brass)}footer .wrap{font-size:12.5px}footer b{color:#fff}footer a{color:var(--rustsoft)}
.subpage-link{display:inline-flex;align-items:center;gap:8px;margin:14px 0 2px;background:var(--rust);color:#fff;padding:11px 18px;border-radius:10px;font-weight:800;font-size:13.5px;box-shadow:var(--sh)}
.subpage-link:hover{background:var(--espresso);text-decoration:none}
.backlink{display:inline-block;margin:0 0 8px;color:#e9dcc6;font-size:13px;font-weight:700}
.backlink:hover{color:#fff}
.sec-lead{color:var(--muted);max-width:840px;margin:0 0 18px;font-size:14.5px;line-height:1.55}
.approaches{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:4px 0 26px}
.appcard{background:var(--parch);border:1px solid var(--line);border-radius:14px;padding:16px 18px;box-shadow:var(--sh)}
.appcard h4{margin:3px 0 6px;color:var(--espresso);font-size:16px}
.appcard .tagp{font-size:10.5px;font-weight:800;text-transform:uppercase;letter-spacing:.6px;color:var(--rust)}
.appcard p{font-size:13px;color:#5a4836;margin:0;line-height:1.5}
.appcard.best{border:2px solid var(--good)}
.heropick{display:grid;grid-template-columns:300px 1fr;gap:0;background:var(--parch);border:2px solid var(--good);border-radius:18px;overflow:hidden;box-shadow:var(--shlg);margin:0 0 28px}
.heropick .pic{background:#fff;display:flex;align-items:center;justify-content:center;padding:18px;border-right:1px solid var(--line)}
.heropick .pic img{max-width:100%;max-height:280px;object-fit:contain;mix-blend-mode:multiply}
.heropick .info{padding:20px 24px}
.heropick .crown{display:inline-block;background:var(--good);color:#fff;font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.6px;padding:4px 11px;border-radius:20px;margin-bottom:8px}
.heropick h3{margin:0 0 4px;font-size:21px;color:var(--espresso)}
.heropick .info p{font-size:13.5px;color:#5a4836;line-height:1.55;margin:8px 0 0}.heropick .info ul{margin:8px 0 0;padding-left:17px;font-size:13px}.heropick .info li{margin:4px 0}
.vtable{overflow-x:auto;border:1px solid var(--line);border-radius:14px;box-shadow:var(--sh);background:var(--parch);margin:0 0 26px}
.vtable table{border-collapse:collapse;width:100%;min-width:920px;font-size:12.5px}
.vtable th,.vtable td{padding:10px 12px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
.vtable thead th{background:#efe6d3;color:var(--espresso);font-family:Georgia,serif;position:sticky;top:0}
.vtable tbody tr:hover{background:#fbf6ec}.vtable tr.top td{background:#eef6ef;font-weight:600}
@media(max-width:920px){.grid{grid-template-columns:1fr}.stats{grid-template-columns:repeat(2,1fr)}.approaches{grid-template-columns:1fr}.heropick{grid-template-columns:1fr}}
@media print{.card:hover{transform:none}.btn{display:none}nav.cats{display:none}header.top{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
"""

ENGRAVE_SVG = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#7c7f4e" stroke-width="2.2"><path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/></svg>'

def esc(s): return _html.escape(str(s), quote=True)

def card_html(o):
    cls, _ = TIERS[o["tier"]]
    rec = " rec" if o["tier"] == "recommended" else ""
    learn = o.get("learn")
    learn_block = (f'<details class="learn"><summary>Learn more &mdash; how it works &amp; what to know</summary><div class="ld">{learn}</div></details>') if learn else ""
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
{learn_block}
<a class="btn" href="{esc(o['url'])}" target="_blank" rel="noopener">View &amp; buy &rarr;</a>
</div></article>"""

def item_html(it):
    parts = [f'<div class="item" id="item-{it["id"]}"><div class="item-h"><h3>{esc(it["name"])}</h3><span class="chip">{esc(it["tag"])}</span></div>']
    if it.get("reference"):
        parts.append(f'<div class="ref"><span class="tg">Your<br>Reference</span><span>{esc(it["reference"])}</span></div>')
    parts.append('<div class="grid">' + "".join(card_html(o) for o in it["options"]) + '</div>')
    if it.get("note"):
        parts.append(f'<div class="note">{esc(it["note"])}</div>')
    if it.get("subpage"):
        u, l = it["subpage"]
        parts.append(f'<a class="subpage-link" href="{esc(u)}">{esc(l)} &rarr;</a>')
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
<div class="stat"><div class="n">$0.09&ndash;$450</div><div class="l">Per-unit range</div></div>
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

BANDANA = {
 "lead_sub": "Every way to brand a bandana — ranked for a full-bleed cotton result, with our pick at the top.",
 "lead": "You have three routes. The cheapest/most traditional is a stock paisley with a blank center you fill with the seal (A); the most hands-on is buying blanks and branding them yourself (B); and the one you want — a genuinely bespoke product — is a completely custom, edge-to-edge design that turns the whole bandana into Poco Loco paisley + Western iconography (C). Below: the honest method trade-offs, our vetted pick, and a wide ranked vendor list.",
 "approaches": [
   {"tag":"Approach A","name":"Open-center medallion","body":"A stock traditional paisley with a blank <b>center medallion</b>; you or the vendor screen the seal into the open middle. Real cotton, classic, cheap, low-ish MOQ — but the paisley is generic and the logo is confined to the center.","best":False},
   {"tag":"Approach B","name":"Blank → brand in-house","body":"Buy blank earthy-cotton paisley or solid bandanas and brand them yourself (UVDTF / screen / embroidered corner). Total control, any quantity — but in-house transfer can't achieve true edge-to-edge all-over, and washes less durably than dyed-in print.","best":False},
   {"tag":"Approach C — your goal","name":"Full-custom, all-over","body":"Your complete design — custom paisley + the Poco Loco seal + iconography — printed <b>edge to edge</b>. The premium, fully-branded result. On <b>cotton</b> via all-over screen or digital print; the easy/cheap path is dye-sublimation but that's <b>polyester</b>; the authentic look is rotary screen on USA cotton (high MOQ).","best":True},
 ],
 "pick": {
   "name":"Full-bleed on cotton — DTLA Print (and The Bandanna Co. for a flagship run)",
   "supplier":"DTLA Print (Vernon, CA) · The Bandanna Company (USA mill, pictured)",
   "url":"https://www.dtlaprint.com/custom/bandanas/",
   "img":"assets/img/bandana-havahank.png",
   "body":"<p>For your full-bleed, all-over <b>cotton</b> goal at a realistic ~24–300 units, <b>DTLA Print</b> is the best practical pick: all-over <b>screen print on 100% cotton</b>, <b>hemmed on all four sides</b>, edge-to-edge, US-made (Vernon, CA), effective MOQ ~24. A classic paisley field + your 1–3 color seal as a centered medallion is exactly its sweet spot.</p><ul><li><b>Lowest MOQ US cotton full-bleed:</b> Printology (full-bleed screen on cotton, MOQ 12).</li><li><b>Full-color digital on USA cotton, verified price:</b> 4AllPromos ($11.76/ea at 100) or Planet Apparel (Austin, TX; organic option).</li><li><b>Authentic heirloom flagship:</b> The Bandanna Company / Hav-A-Hank (pictured) — genuine USA-mill <b>rotary all-over cotton paisley</b>, the real thing — but the all-over rotary look needs ~<b>3,000 pcs</b>.</li><li><b>Easy & cheap (poly):</b> Bandana Supply (local Sugar Land, TX), Pop! Promos — gorgeous full-bleed via dye-sublimation, but polyester, which reads athletic, not rustic.</li></ul><p>Pictured: The Bandanna Company's authentic rotary cotton paisley — the look to aim for. Sample 2–3 finalists before a full run.</p>",
 },
 "table_lead": "Approach: A = open-center · B = blank for in-house · C = full-custom all-over. Ranked for full-bleed cotton. Quote-only vendors don't publish unit prices (flagged). Confirm price/MOQ/hem at order.",
 "vendors": [
   {"name":"DTLA Print","loc":"Vernon, CA (US)","approach":"C / A / B","method":"All-over screen on cotton; DTG; embroidery","fabric":"100% cotton","moq":"~24","price":"quote ($1.85–8.46)","verdict":"Best practical full-bleed cotton; hemmed 4 sides","url":"https://www.dtlaprint.com/custom/bandanas/","top":True},
   {"name":"Printology","loc":"San Diego + Las Vegas (US)","approach":"C","method":"Full-bleed screen / DTG (cotton); dye-sub (poly)","fabric":"Cotton or poly","moq":"12","price":"quote","verdict":"Lowest-MOQ US full-bleed on cotton","url":"https://printology.io/products/custom-bandanas/","top":False},
   {"name":"4AllPromos (Digital Cotton)","loc":"USA","approach":"C","method":"Digital full-color (front)","fabric":"100% cotton","moq":"100","price":"$11.76","verdict":"Verified-price full-bleed on USA cotton","url":"https://www.4allpromos.com/product/usa-made-digitally-printed-bandannas-100-cotton-sustainable-22-x-22","top":False},
   {"name":"Planet Apparel","loc":"San Diego + Austin, TX","approach":"C","method":"Digital full-bleed / sublimation / screen","fabric":"USA cotton + organic","moq":"48","price":"quote ($45/color screen)","verdict":"Digital full-bleed on USA cotton; TX presence","url":"https://www.planetapparel.com/custom-bandanas/","top":False},
   {"name":"The Bandanna Co. / Hav-A-Hank","loc":"SC + NC (US mill)","approach":"C / A","method":"Rotary all-over (≤8 clr); screen (1–4 clr)","fabric":"100% cotton, USA-woven","moq":"50 screen / 3,000 rotary","price":"quote","verdict":"Authentic USA rotary all-over — the heirloom flagship","url":"https://thebandannacompany.com/custom-paisley/","top":False},
   {"name":"AMBRO Manufacturing","loc":"NJ/NY (US)","approach":"C / A / B","method":"Discharge/screen all-over; dye-sub (poly)","fabric":"100% cotton or poly","moq":"144","price":"quote","verdict":"US mill; offers 27×27 'wild rag' size","url":"https://www.ambromanufacturing.com/custom-all-over-print-bandanas/","top":False},
   {"name":"Hoo-rag / Wyldr","loc":"USA","approach":"C","method":"Dye-sub (1 side &lt;5k); screen (both &gt;5k)","fabric":"100% cotton","moq":"24","price":"$10","verdict":"Low-MOQ all-cotton full-bleed (24×24)","url":"https://www.wyldr.com/main-customs-page/","top":False},
   {"name":"Alchemy Merch","loc":"Overseas (China)","approach":"C","method":"Digital full-color (unlimited clr)","fabric":"100% cotton poplin","moq":"50","price":"~$7.60","verdict":"Unlimited-color digital on cotton; ~1 month","url":"https://alchemymerch.com/products/bandanas-100-cotton","top":False},
   {"name":"Bandana Supply Co","loc":"Sugar Land, TX","approach":"C / B","method":"Dye-sublimation, all-over","fabric":"Polyester","moq":"none","price":"~$4.80","verdict":"Local TX, no-min, fast — but poly, not cotton","url":"https://bandanasupply.com/products/custom-full-color-bandanas-as-low-as-4-8-per-piece","top":False},
   {"name":"Pop! Promos","loc":"Philly HQ / made China","approach":"C","method":"Dye-sublimation","fabric":"Microfiber poly","moq":"100","price":"$9.22","verdict":"Clean sublimation + pricing; square or triangle","url":"https://poppromos.com/product/full-color-bandana/","top":False},
   {"name":"4inBandana","loc":"Overseas (China)","approach":"C","method":"Sublimation + DTG, all-over","fabric":"Cotton / satin / poly","moq":"none","price":"~$5.65","verdict":"No-min cotton all-over; overseas, hem unconfirmed","url":"https://4inbandana.com/custom-bandanas","top":False},
   {"name":"Printful","loc":"US facilities","approach":"C","method":"Dye-sublimation","fabric":"Polyester","moq":"1","price":"~$10","verdict":"Zero-MOQ finished full-bleed; poly, vague sizes","url":"https://www.printful.com/custom-bandanas","top":False},
   {"name":"Spoonflower","loc":"USA","approach":"C (raw)","method":"Digital pigment on fabric","fabric":"100% cotton (by the yard)","moq":"none","price":"~$22/yd","verdict":"Cotton, zero-MOQ — but raw fabric, you cut & hem","url":"https://www.spoonflower.com/en/cotton-poplin","top":False},
   {"name":"OutfitYourLogo","approach":"A","loc":"US co.","method":"Screen into the open center","fabric":"100% cotton","moq":"100","price":"$4.97 (+$58/clr)","verdict":"Cheapest open-center medallion; not edge-to-edge","url":"https://www.outfityourlogo.com/detail.php?p=PAIS","top":False},
   {"name":"CustomInk","loc":"US-based","approach":"A / C(poly)","method":"Digital (poly) / screen / cotton corner SKU","fabric":"Poly (full-color) / cotton (corner)","moq":"~12","price":"quote","verdict":"Easy UX; full-color = poly, cotton = centered only","url":"https://www.customink.com/products/accessories/bandanas/full-color-classic-bandana/1944300","top":False},
   {"name":"Western Express","loc":"USA","approach":"A / B","method":"Stock paisley + your screen","fabric":"100% cotton","moq":"1","price":"$5.99","verdict":"Earthy cotton paisley blanks (brown/olive/beige)","url":"https://wexpress.com/bandanas-brown-paisley-usa-made/","top":False},
 ],
 "notes": "<span class='hd'>Cotton vs. polyester — the core decision</span>Dye-sublimation gives effortless edge-to-edge full color but <b>only on polyester</b> (reads athletic/synthetic — wrong for an upscale-rustic ranch). A true all-over <b>cotton</b> bandana means all-over <b>screen</b> (finite spot colors — perfect for paisley + a 1–3 color seal), <b>digital/pigment</b> (unlimited color, back prints lighter), or <b>reactive/rotary</b> (deepest, most premium, but high MOQ). For Poco Loco, stay cotton — a classic paisley + your black-and-white seal is ideal for screen.<span class='hd'>Art-setup gotchas for full-bleed</span><ul><li><b>Bleed:</b> extend the paisley ~0.25″ past the cut/hem line so no white slivers show after hemming.</li><li><b>Safe area:</b> a hem folds ~0.25–0.5″ under each side — keep the seal & text ≥1.5–2″ from the raw edge.</li><li><b>Layout:</b> build the paisley as a seamless tile; seal as a centered medallion with a decorative inner border (the classic bandana look).</li><li><b>Color:</b> specify Pantone Solid Coated; exact match is guaranteed only on white/natural grounds — design on a natural base, not a pre-dyed color.</li><li><b>Sides:</b> sublimation/reactive print through to the back; screen/digital usually print one side (natural-cotton back) — the most cost-effective premium layout.</li></ul><span class='hd'>Size & finishing</span><b>22×22″</b> is the standard neckerchief; <b>27×27″</b> is the 'wild rag' cowboys actually tie — more premium drape for a flagship piece (AMBRO offers 27×27). Specify a <b>double-folded, stitched hem on all four sides</b> (better than a raw serge) in a mid-to-heavy cotton.<span class='hd'>Defunct / not viable</span>bandana.com (now a jobs site), NYBandana (dead), Apliiq & Gelato (no bandana product), Real Thread (pet/dog bandana only).",
 "footer": "Recommended next steps: decide if the seal is 1–4 spot colors (screen/rotary on cotton) or full-color (digital on cotton); sample DTLA Print, Printology, and 4AllPromos; quote The Bandanna Company if you ever want a 3,000-pc heirloom rotary run. Prices/MOQs from live vendor pages, June 2026.",
}

def render_bandana_page(d):
    apps = "".join(
        f"<div class='appcard{' best' if a.get('best') else ''}'><span class='tagp'>{esc(a['tag'])}</span><h4>{esc(a['name'])}</h4><p>{a['body']}</p></div>"
        for a in d["approaches"])
    p = d["pick"]
    rows = ""
    for v in d["vendors"]:
        tc = " class='top'" if v.get("top") else ""
        rows += (f"<tr{tc}><td><b>{esc(v['name'])}</b><br><span style='color:#9c8a72;font-size:11px'>{esc(v.get('loc',''))}</span></td>"
                 f"<td>{esc(v['approach'])}</td><td>{esc(v['method'])}</td><td>{esc(v['fabric'])}</td>"
                 f"<td>{esc(v['moq'])}</td><td>{esc(v['price'])}</td><td>{esc(v['verdict'])}</td>"
                 f"<td><a href='{esc(v['url'])}' target='_blank' rel='noopener'>visit</a></td></tr>")
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Poco Loco Ranch — Bandana Vendor Breakdown</title><link rel="icon" href="assets/img/poco-loco-logo.png"><style>{CSS}</style></head><body>
<header class="top"><div class="wrap"><a class="backlink" href="index.html">&larr; Back to the OS&amp;E dashboard</a><div class="brandrow">
<div class="seal-chip"><img src="assets/img/poco-loco-logo.png" alt="Poco Loco Ranch"></div>
<div><h1>Bandanas — Complete Vendor Breakdown</h1><p class="sub">{esc(d['lead_sub'])}</p></div></div></div></header>
<div class="wrap">
<section class="cat"><div class="cat-h"><h2>The three ways to do it</h2></div><p class="sec-lead">{d['lead']}</p>
<div class="approaches">{apps}</div>
<div class="cat-h"><h2>Our pick</h2></div>
<div class="heropick"><div class="pic"><img src="{esc(p['img'])}" alt="{esc(p['name'])}"></div>
<div class="info"><span class="crown">★ Vetted best for full-bleed cotton</span><h3>{esc(p['name'])}</h3>
<div class="supplier">{esc(p['supplier'])}</div>{p['body']}
<a class="btn" style="max-width:260px;margin-top:14px" href="{esc(p['url'])}" target="_blank" rel="noopener">Visit DTLA Print &rarr;</a></div></div>
<div class="cat-h"><h2>Every vendor we vetted</h2></div><p class="sec-lead">{d['table_lead']}</p>
<div class="vtable"><table><thead><tr><th>Vendor</th><th>Approach</th><th>Method</th><th>Fabric</th><th>MOQ</th><th>~100 price</th><th>Verdict</th><th></th></tr></thead><tbody>{rows}</tbody></table></div>
<div class="cat-h"><h2>Methods, art &amp; finishing</h2></div><div class="note" style="font-size:13px">{d['notes']}</div>
</section></div>
<footer><div class="wrap"><p>{esc(d['footer'])}</p><p style="margin-top:8px;color:#9c8a72">Poco Loco Ranch &middot; Bandana sourcing deep-dive &middot; confirm live pricing at order.</p></div></footer>
</body></html>"""

if __name__ == "__main__":
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / "items.json").write_text(json.dumps(
        {"meta": META, "categories": [{"id":c,"name":n,"blurb":b} for c,n,b in CATEGORIES], "items": DATA}, indent=2))
    doc = render()
    (ROOT / "index.html").write_text(doc)
    (ROOT / "dashboard-standalone.html").write_text(inline_images(doc))
    (ROOT / "bandana.html").write_text(render_bandana_page(BANDANA))
    print("items:", len(DATA), "options:", sum(len(i['options']) for i in DATA))
    print("wrote index.html, dashboard-standalone.html, data/items.json")
