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
 dict(id="napkins", cat="bar", name="Linen-Feel Cocktail Napkins", tag="Disposable · printed",
   note="Like the Badrutt's napkin: a disposable linen-feel (airlaid) napkin with a printed logo. Limelight prints your seal at the lowest minimum (25); Caspari and Hoffmaster are premium natural blanks you can stamp in-house. Runner-ups: For Your Party (foil) and Champagne & Ink (100 min, ~$1.18 printed).",
   options=[
     opt("recommended","\"Linun\" Personalized Linen-Feel Cocktail Napkins","Limelight Paper","https://limelightpaper.com/products/linun-beverage-napkin",
         "≈ $0.34","/ napkin","$10 flat setup · min 25","min 25","Airlaid linen-feel · 5×5″ · one-time use · cream/natural","Supplier-printed (1-color or foil)",
         "Lowest MOQ (25) and a $10 flat setup — the closest match to the Badrutt's printed linen-feel napkin at boutique quantity.","assets/img/napkin-rec.jpg"),
     opt("premium","Linen Border Cocktail Napkins — Natural","Caspari","https://www.casparionline.com/products/linen-border-paper-cocktail-napkins-in-natural-20-per-package",
         "≈ $0.30","/ napkin","$5.95 / 20-pack","min 20","Triple-ply paper-linen · natural linen border · 5×5″","Blank: stamp seal in-house or use as-is",
         "The most premium-feeling blank in a true cream/natural tone at the lowest commitment — Caspari is the luxury name in paper-linen.","assets/img/napkin-alt1n.jpg"),
     opt("value","Linen-Like Natural Kraft Beverage Napkin","Hoffmaster","https://www.webstaurantstore.com/hoffmaster-046128-10-x-10-linen-like-natural-kraft-1-4-fold-beverage-napkin-case/788BNAP14NT.html",
         "≈ $0.09","/ napkin","$84.99 / case of 1,000","min 1,000","Natural kraft linen-feel airlaid · rustic tone","Blank: in-house stamp / UVDTF",
         "Ultra-low cost and the most rustic natural tone; a case of 1,000 for a property that stamps in-house.","assets/img/napkin-alt2.jpg"),
   ]),
 # ---------------- BEDROOM & COMFORT ----------------
 dict(id="blankets", cat="bedroom", name="Plain Low-Cost Blankets", tag="Woven cotton · no lint",
   note="Why woven, not fleece: flat-woven cotton (waffle / basketweave) has no raised nap or static, so it sheds pet hair and lint instead of grabbing it like polar fleece. All plain and embroiderable. More options: DII Herringbone (~$20, Amazon) and the Superior Diamond-weave throw.",
   options=[
     opt("recommended","Waffle Weave Cotton Throw, 50×60","VHC Brands","https://allysonsplace.com/products/vhc-brands-waffle-weave-white-throw-50x60-decorative-cotton-blanket-for-farmhouse-boho-decor",
         "$21.95","/ ea","$21.95–$25.95 by color","min 1","100% pre-washed cotton waffle weave · Natural/Olive/Grey/White · 50×60","In-house embroidery",
         "Flat woven cotton — sheds lint instead of grabbing it. Exact 50×60, true neutrals, under ~$25, single-unit.","assets/img/blanket-rec.jpg"),
     opt("value","Mikala 100% Cotton Waffle Throw, 50×60","Great Bay Home (Target)","https://www.target.com/p/cotton-super-soft-all-season-waffle-weave-knit-blanket-great-bay-home-throw-oatmeal/-/A-91107311",
         "≈ $22","/ ea","~$20–25 at Target","min 1","100% combed cotton waffle · Oatmeal/Taupe/Grey · 50×60","In-house embroidery",
         "Another woven-cotton waffle in true oatmeal/taupe, single-unit at Target — same anti-lint behavior.","assets/img/blanket-alt1.jpg"),
     opt("premium","Basketweave Thermal Cotton Throw, 50×60","Superior Brand","https://www.superiorbrand.com/products/basket-weave-all-season-100-cotton-thermal-woven-blanket",
         "$28.10","/ ea","sold individually","min 1","100% cotton flat basketweave thermal · Charcoal/Taupe/Khaki/Ivory · 50×60","In-house embroidery",
         "The tightest, flattest weave here = the best lint-shedder of all; just over $25 with confirmed neutral colors.","assets/img/blanket-alt2.webp"),
   ]),
 dict(id="sewing", cat="bedroom", name="Disposable Sewing Kit", tag="Hotel amenity · printed",
   note="A genuine disposable matchbook/folder kit that ALSO prints your logo on the website is rare. ProImprint (flat case) has the lowest cost + setup; ImprintItems prints a true paper matchbook cover (quote-only, ~$500 min). All print the seal for you — no in-house work needed.",
   options=[
     opt("recommended","Logo Sewing Kit — flat snap case","ProImprint","https://www.proimprint.com/Custom-Logo-Imprinted-Sewing-Kits",
         "$0.83","/ ea","min 250 + $34.99 setup","min 250","Thin flat case · threads, needles, pins, buttons · logo on front","Supplier-printed (website)",
         "Lowest per-unit ($0.83) and setup ($34.99) of the disposable-style kits, website-branded, clean amenity look.","assets/img/sewing-alt2.jpg"),
     opt("alt","Matchbook Folder Sewing Kit","ImprintItems","https://www.imprintitems.com/product/9755292",
         "quote","/ ea","~$500 min · $55 setup","min ~250","True paper matchbook folder — the authentic hotel format · cover printed","Supplier-printed cover (website)",
         "The truest disposable hotel matchbook, with your logo offset-printed across the cover. Pricing is quote-only.","assets/img/sewing-rec.jpg"),
     opt("alt","Sewing Kit #962","4imprint","https://www.4imprint.com/product/962/Sewing-Kit",
         "$1.12","/ ea","min 250 + $40 setup","min 250","Compact case · multi-thread, needles, pins, buttons","Supplier-printed (website)",
         "A turnkey website-branded kit from a trusted US promo house — clean and cheap at 250.","assets/img/sewing-alt1.jpg"),
   ]),
 # ---------------- WELCOME & DESK ----------------
 dict(id="pens", cat="welcome", name="Pens with Heft & Character", tag="≤ $5 · metal",
   reference="Your exemplar: a substantial cream-lacquer barrel with gold trim, twist-action — a real hotel pen, not promo SWAG.",
   note="Honest tradeoff: under $5 you can get heavy brass (the Executive — but black/gold, not cream) OR the cream/gold look (slim, lighter). A cream-lacquer + gold + HEAVY pen isn't stocked at this price — sample the brass Executive and the white/gold Slim before a 100-unit buy, or go ~$16 (Garland Hamilton) for an exact heavy cream/gold match.",
   options=[
     opt("recommended","Executive Metal Pen — solid brass barrel","4imprint","https://www.4imprint.com/product/8804-L/Executive-Metal-Pen-Laser-Engraved",
         "$4.25","/ pen","$425 / 100 (+$30 setup)","min 100","Solid BRASS barrel, lacquer finish, twist · gold-toned engraving","Supplier laser-engraved",
         "The only verified genuinely HEAVY pen in budget — real brass, classic executive feel, gold imprint. Black lacquer + gold seal is the most upscale combo (no cream offered).","assets/img/pen-rec.jpg"),
     opt("value","Slim Metal Pen with Gold Accents — White","Quality Logo Products","https://www.qualitylogoproducts.com/custom-pens/slim-metal-gold-pen.htm",
         "$1.70","/ pen","$170 / 100 · free setup","min 100","White metal barrel + gold trim, twist · the cream/gold look","Supplier-printed",
         "Closest to your exemplar's cream-and-gold palette and cheapest — but slim, so sample it to confirm the weight clears the 'not throwaway' bar.","assets/img/pen-alt1.jpg"),
     opt("alt","Metal Twist Pen — Champagne/Gold","4CustomPromo","https://www.4custompromo.com/custom-metal-twist-ballpoint-pen-with-big-pearl.html",
         "$1.97","/ pen","$197 / 100","min 100","Champagne/white + gold trim metal barrel, twist · laser-engravable","In-house or supplier laser-engrave",
         "Cream/champagne + gold with cleaner laser engraving and some metal weight; the pearl cap is a glam accent — order Champagne for the closest match.","assets/img/pen-alt2.jpg"),
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
 dict(id="bandana", cat="welcome", name="Custom Paisley Bandana", tag="Paisley + your logo",
   note="Two routes: (B) a traditional paisley with a blank CENTER MEDALLION your seal prints into — OutfitYourLogo, ~$555 for 100 incl. setup; or (A) FULL CUSTOM, your seal baked into the paisley — The Bandanna Company (Hav-A-Hank), screen min 50, quote pricing. Local option: Bandana Supply (Sugar Land, TX). Note: bandana.com / nationalbandana are defunct.",
   options=[
     opt("recommended","Open-Center Paisley Bandana, USA Made","OutfitYourLogo","https://www.outfityourlogo.com/detail.php?p=PAIS",
         "$4.97","/ ea","~$555 / 100 (incl. $58 setup)","min 100","22×22″ 100% cotton · classic paisley + 10×10 blank center · khaki/olive/navy/rust/red/black","Supplier screen-print into the center",
         "Exactly your 'paisley with a blank spot for the logo' idea — traditional paisley, USA-made cotton, every earthy color, with clean 100-unit pricing.","assets/img/bandana-rec.jpg"),
     opt("premium","Custom Paisley — logo baked into the design","The Bandanna Co. (Hav-A-Hank)","https://thebandannacompany.com/custom-paisley/",
         "quote","/ ea","screen min 50 · quote for 100","min 50","100% cotton · your seal printed INTO a full custom paisley · US heritage maker","Supplier full-custom screen-print",
         "The true full-design route — they bake your seal into the paisley itself. Achievable at ~100 via their 50-pc screen minimum; call for the 100-unit total.","assets/img/bandana-alt1.png"),
     opt("value","USA-Made Paisley Bandana, 22″","4AllPromos","https://www.4allpromos.com/product/usa-made-paisley-bandana-cotton-22-inch",
         "$5.85","/ ea","~$649 / 100 (incl. $63.63 setup)","min 100","22×22″ 100% cotton · stock paisley, logo in a corner/side strip","Supplier screen-print (corner)",
         "Fully-verified turnkey 100-unit pricing and free shipping; the seal prints in a corner strip rather than centered.","assets/img/bandana-alt2.jpg"),
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
   reference="Like your Badrutt's desk set: bordered correspondence cards with a small crest and matching envelopes, in cream/soft tones. (Embossing/foil on paper is a supplier job, not an in-house one.)",
   note="The fine-hotel upgrade: Crane & Co. 100% cotton bordered correspondence cards (gold or navy border on ecru), $32–$34 per box of 10 incl. envelopes, made in USA — order direct at crane.com (their photos are hotlink-protected, so not shown here). For heavy cotton to letterpress your crest yourself: Crane Lettra (~$13.64/50) or Original Crown Mill pure-cotton sets.",
   options=[
     opt("recommended","Bordered Correspondence Cards + Envelopes","Merrimade","https://www.merrimade.com/bordered-correspondence-cards.html",
         "$3.00","/ card","$75 / box of 25 (incl. 25 envelopes)","min 25","Bordered card · raised-ink your crest/text · white/ivory + red/navy/green border · 6.25×4.5″","Supplier raised-ink print of your crest",
         "Bordered hotel-style cards with your crest printed and matching envelopes included, at a low 25 minimum — the closest turnkey branded match to the Badrutt's set.","assets/img/stationery-rec.jpg"),
     opt("value","Embossed Border Correspondence Cards (#3120)","American Stationery","https://www.americanstationery.com/embossed-border-correspondence-cards-7254.html",
         "≈ $2.24","/ card","$55.95 / box of 25","min 25","Embossed raised border + personalization · white/ivory · envelopes included · 6.25×4.5″","Supplier emboss + print",
         "A true embossed border plus your printed crest at the lowest branded price — the most 'embossed' look of the three.","assets/img/stationery-alt1.jpg"),
     opt("alt","A7 Ecru Embossed Panel Cards (blank)","LCI Paper","https://lcipaper.com/a7-panel-card-lci-smooth-80lb-blank-cards-ecru/pd/E7PC-80.html",
         "≈ $0.30","/ card","$14.78 / 50 · envelopes ~$8.91/25","min 50","Blind-embossed panel border · ecru · 80lb · blank, laser/inkjet printable","In-house: print/stamp your crest",
         "The cheapest path — premium blind-embossed bordered blanks you run your own crest onto (or letterpress).","assets/img/stationery-alt2.jpg"),
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
 dict(id="umbrellaholder", cat="outdoor", name="Brass Umbrella Stand", tag="Brass tube",
   note="Material reality: new clean-cylinder 'brass' stands (Glaro and its commercial twins) are satin-brass FINISH on rust-proof aluminum, not solid brass — a genuine solid-brass smooth tube only exists vintage or custom-fabricated. For true solid brass, the vintage Chairish piece is the real thing (an open serpent-ring form, not a smooth tube).",
   options=[
     opt("recommended","Glaro 921 Satin Brass Cylinder Stand","Glaro / Trashcans Unlimited","https://trashcansunlimited.com/satin-brass-or-aluminum-umbrella-stand-921-by-glaro/",
         "$191.45","/ ea","made in USA · sold individually","min 1","Clean 23″H × 9″ cylinder · satin brass on spun aluminum · water tray","In-house laser-engrave / UVDTF the face",
         "The cleanest 'brass tube' silhouette available new — a plain polished cylinder, tarnish-proof so an engraved seal stays sharp, commercial-grade, under $200.","assets/img/umbrellaholder-rec.jpg"),
     opt("premium","Glaro 259 Combination Cylinder — Satin Brass","Glaro / Trashcans Unlimited","https://trashcansunlimited.com/aluminum-or-brass-combination-umbrella-stand-259-by-glaro/",
         "$289.45","/ ea","made in USA · sold individually","min 1","Larger 23″H × 15″ tube · ~20 lb · bigger branding face","In-house laser-engrave / UVDTF",
         "Same brand and clean-tube look but heavier (20 lb, won't tip) with a bigger face for the seal — for a high-traffic entry.","assets/img/umbrellaholder-alt1.jpg"),
     opt("alt","Early-20thC French SOLID Brass Holder (vintage)","Chairish","https://www.chairish.com/product/2920555/early-20th-century-french-brass-umbrella-holder",
         "$450","/ ea","one-of-one · for sale now","min 1","Genuine SOLID brass with natural patina · 24″H · Art Nouveau serpent rings","UVDTF on the base (open form)",
         "If you want truly solid brass, this is it — a real vintage piece. Trade-off: an open ring form (not a smooth tube), so engraving isn't practical.","assets/img/umbrellaholder-alt2.jpg"),
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

if __name__ == "__main__":
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / "items.json").write_text(json.dumps(
        {"meta": META, "categories": [{"id":c,"name":n,"blurb":b} for c,n,b in CATEGORIES], "items": DATA}, indent=2))
    doc = render()
    (ROOT / "index.html").write_text(doc)
    (ROOT / "dashboard-standalone.html").write_text(inline_images(doc))
    print("items:", len(DATA), "options:", sum(len(i['options']) for i in DATA))
    print("wrote index.html, dashboard-standalone.html, data/items.json")
