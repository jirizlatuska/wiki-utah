# Wiki Log

Append-only record of all operations.

---

## 2026-05-19 — Initial wiki creation

**Sources ingested**: All six KMZ route files in `raw/`

- `Directions from Phoenix Sky Harbor...to Navajo Moenave Dinosaur Tracks.kmz` (Leg 1)
- `Directions from Moenave Dinosaur Tracks...to Stateline Campground.kmz` (Leg 2)
- `Directions from Stateline Campground...to Goblin Valley.kmz` (Leg 3)
- `Directions from Goblin Valley State Park...to Mt. Pennell Lookout.kmz` (Leg 4)
- `Directions from BLM 0095, Hanksville...to Muley Point East.kmz` (Leg 5)
- `Directions from Muley Point...to Phoenix Sky Harbor.kmz` (Leg 6)
- `ae7599a3-Directions_from_Muley_Point...PHX.kmz` (duplicate of Leg 6)

**Pages created** (37 total):

Core:
- `wiki/index.md` — table of contents
- `wiki/log.md` — this file
- `wiki/itinerary.md` — full 6-leg itinerary with all waypoints
- `wiki/permits.md` — White Pocket, Coyote Buttes South, White Rim Road

Leg 1 destinations:
- `wiki/apache-trail.md`
- `wiki/mogollon-rim.md`
- `wiki/meteor-crater.md`
- `wiki/coal-mine-canyon.md`
- `wiki/moenave-dinosaur-tracks.md`

Leg 2 destinations:
- `wiki/navajo-bridge.md`
- `wiki/white-pocket.md`
- `wiki/kanab.md`
- `wiki/coral-pink-sand-dunes.md`
- `wiki/bryce-canyon.md`
- `wiki/kodachrome-basin.md`
- `wiki/cottonwood-canyon-road.md`

Leg 3 destinations:
- `wiki/coyote-buttes-south.md`
- `wiki/alstrom-point.md`
- `wiki/smokey-mountain-road.md`
- `wiki/escalante.md`
- `wiki/muley-twist-canyon.md`
- `wiki/hanksville.md`
- `wiki/goblin-valley.md`

Leg 4 destinations:
- `wiki/moonscape-overlook.md`
- `wiki/cathedral-valley.md`
- `wiki/bentonite-hills.md`
- `wiki/henry-mountains.md`

Leg 5 destinations:
- `wiki/white-rim-road.md`
- `wiki/natural-bridges-nm.md`
- `wiki/muley-point.md`

Leg 6 destinations:
- `wiki/valley-of-the-gods.md`
- `wiki/monument-valley.md`
- `wiki/grand-canyon-desert-view.md`
- `wiki/sedona.md`
- `wiki/verde-canyon-railroad.md`
- `wiki/organ-pipe-cactus-nm.md`
- `wiki/kitt-peak.md`

**Notes**: KMZ files contain route/waypoint data only. Factual claims about locations are drawn from general knowledge and marked "(needs verification)" throughout. Trip-specific dates are not yet set.

---

## 2026-05-20 — Added child-friendly activity information

**Reason**: Traveling with a 7-year-old; requested coverage of dinosaur tracks, live animals, and age-appropriate activities.

**Pages created**:
- `wiki/kids.md` — aggregator page covering dinosaurs, wildlife, best stops ranked for kids, suitable hikes, train ride, and difficulty notes

**Pages updated** (added "For kids" section to each):
- `wiki/moenave-dinosaur-tracks.md`
- `wiki/goblin-valley.md`
- `wiki/henry-mountains.md`
- `wiki/navajo-bridge.md`
- `wiki/bryce-canyon.md`
- `wiki/verde-canyon-railroad.md`
- `wiki/coral-pink-sand-dunes.md`
- `wiki/natural-bridges-nm.md`

**Index updated**: Added `[[kids]]` to core pages table.

---

## 2026-05-20 — Created printable trip brochure

**File**: `brochure/brochure.html`

**Format**: A4 landscape, two-sided tri-fold (6 panels)
- Sheet 1 outside: cover illustration (canyon moonscape), inside-flap intro, route-at-a-glance back panel
- Sheet 2 inside: Legs 1–3 detail, Legs 4–6 detail, wildlife & family highlights panel

**Illustrations**: All CSS/SVG inline — no external image dependencies. Scenes include Bryce hoodoos at dusk, Apache Trail desert road, Natural Bridges night sky, and Henry Mountains bison.

**To print**: Open `brochure/brochure.html` in a browser → File → Print → A4 landscape, no margins. Print sheet 1, flip paper, print sheet 2, then fold in thirds.
