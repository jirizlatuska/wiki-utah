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

## 2026-05-20 — Added detailed trip schedule

**Source**: User-provided day-by-day schedule with campground names and segment durations.

**Pages created**:
- `wiki/schedule.md` — 24-night calendar (Jul 23 – Aug 16, 2026) with confirmed campgrounds, permit dates, four flagged gaps (nights 1/2, 3/4, 16/17, 20/21), timing note for Aug 13 Verde Canyon Railroad, and decision note on Monument Valley vs Muley Point for night 20/21

**Pages updated**:
- `wiki/itinerary.md` — added specific travel dates, flight times, reference to [[schedule]], confirmed permit dates
- `wiki/permits.md` — added confirmed permit dates (CBS July 30; White Rim Aug 10–11); updated booking strategy to reflect confirmed permits
- `wiki/index.md` — added [[schedule]] to core pages table

---

## 2026-05-21 — Added Newspaper Rock to Segment 5

**Pages created**: `wiki/newspaper-rock.md`
**Pages updated**: `wiki/schedule.md` (row 19/20), `wiki/index.md`, `wiki/kids.md` (added to Dinosaurs and ancient life section)

Newspaper Rock sits on UT-211 and falls naturally on the August 11 exit day from White Rim Road (Mineral Bottom → south). Free roadside stop, no permit.

---

**Key findings from parsing the schedule**:
- "Wild Horse State Park" (night Aug 9/10) is almost certainly Dead Horse Point State Park — needs user confirmation
- Night 16/17 (Aug 8/9) is a transit gap between Henry Mountains and Dead Horse Point area
- Aug 13 Verde Canyon Railroad (13:00 Clarkdale) makes Monument Valley (not Muley Point) the preferred camp for night 20/21
- Grand Canyon Desert View may fit better on Aug 14 morning than Aug 13

---

## 2026-05-20 — Created printable trip brochure

**File**: `brochure/brochure.html`

**Format**: A4 landscape, two-sided tri-fold (6 panels)
- Sheet 1 outside: cover illustration (canyon moonscape), inside-flap intro, route-at-a-glance back panel
- Sheet 2 inside: Legs 1–3 detail, Legs 4–6 detail, wildlife & family highlights panel

**Illustrations**: All CSS/SVG inline — no external image dependencies. Scenes include Bryce hoodoos at dusk, Apache Trail desert road, Natural Bridges night sky, and Henry Mountains bison.

**To print**: Open `brochure/brochure.html` in a browser → File → Print → A4 landscape, no margins. Print sheet 1, flip paper, print sheet 2, then fold in thirds.

---

## 2026-05-20 — Czech brochure and travel diary for child

**Files added**:
- `brochure/brochure-cz.html` — full Czech translation of the trip brochure; same 2-sheet tri-fold layout; language adapted for a 7-year-old; all SVG illustrations retained
- `brochure/diary.html` — Czech travel diary handout for the child; 6 A4 portrait pages:
  - Page 1: Cover with name field and self-portrait drawing space
  - Pages 2–4: Paired leg diary entries (Legs 1+2, 3+4, 5+6) with date, weather picker, drawing box, per-leg spotter checklist, sentence completions, and star rating
  - Page 5: Animal spotter table (12 species, fill-in where/what columns, score tally)
  - Page 6: Awards page — Best Place, Biggest WOW, Best Animal, Best Food, Biggest Surprise, Longest Ride — plus final reflection and overall trip star rating

---

## 2026-06-04 — Added Horseshoe Canyon / Great Gallery to Segment 3

**Pages created**: `wiki/horseshoe-canyon.md`
**Pages updated**:
- `wiki/schedule.md` — row 11/12 (Aug 3): added Horseshoe Canyon Great Gallery as morning stop before driving to Goblin Valley
- `wiki/index.md` — added `[[horseshoe-canyon]]` to Leg 3 table
- `wiki/kids.md` — added Horseshoe Canyon entry in "Dinosaurs and ancient life" section

Horseshoe Canyon is a detached unit of Canyonlands NP accessed from UT-24 north of Hanksville via W Lower San Rafael Road (County Road 1000). The Great Gallery contains Barrier Canyon Style pictographs (painted, not carved) up to 6–7 feet tall dating roughly 2,000–4,000 years. Hike: ~6.5 miles RT, ~750 ft descent. Start early to beat summer heat; allow 3–4 hours before driving on to Goblin Valley.

---

## 2026-06-04 — Added Green River Overlook (time permitting, Aug 8)

**Pages created**: `wiki/green-river-overlook.md`
**Pages updated**:
- `wiki/schedule.md` — row 16/17 (Aug 8): added Green River Overlook as time-permitting stop on transit from Henry Mountains to Dead Horse Point SP
- `wiki/itinerary.md` — added to Leg 5 table before White Rim Road entry
- `wiki/index.md` — added to Leg 5 table

Green River Overlook is in the Island in the Sky district of Canyonlands NP, on UT-313 en route to Dead Horse Point. Nearly no walking required; panoramic view down to the White Rim and Green River below.

---

## 2026-06-04 — Added Sunset Crater & Wupatki to Leg 1

**Pages created**: `wiki/sunset-crater.md`
**Pages updated**:
- `wiki/schedule.md` — row 2/3 (Jul 25): added as time-permitting stop between Meteor Crater and Coal Mine Canyon
- `wiki/itinerary.md` — added to Leg 1 table
- `wiki/index.md` — added to Leg 1 table
- `wiki/kids.md` — added entry in "Dinosaurs and ancient life" section

Sunset Crater Volcano NM and Wupatki NM share a 36-mile paved loop off US-89 north of Flagstaff — on the natural route from Winslow/Meteor Crater toward Cameron and Coal Mine Canyon. One entrance fee covers both. Flagged time permitting; adds ~45–60 min to July 25.

---

## 2026-07-05 — Ingested Časový rozvrh; first-night motel change; Orange Cliffs loop option

**Sources ingested**: `raw/Časový rozvrh` (was in repo since 2026-05-21 but never formally ingested)

**Pages created**:
- `wiki/casovy-rozvrh.md` — source summary + reconciliation with schedule (Wild Horse SP → Dead Horse Point interpretation, spelling normalizations)
- `wiki/orange-cliffs-loop.md` — optional Hanksville-area 4WD loop: BLM 15000 via Cedar Point and/or Poison Spring Canyon → camp around Land's End or Happy Canyon campsite (Orange Cliffs) → Flint Trail

**Pages updated**:
- `wiki/schedule.md` — night 0/1 (23/24 Jul): Gilbert Ray CG is CLOSED; replaced with motel in Tucson (presumably a Wyndham property near Costco, exact address TBD — needed for U.S. arrival paperwork; nearby BLM dispersed sites have no valid registration). Added Segment 4 alternative note for the Orange Cliffs loop. Sources now cite `raw/Časový rozvrh`.
- `wiki/itinerary.md` — Leg 1 first stop updated; Leg 4 alternative added
- `wiki/permits.md` — new conditional section: Orange Cliffs backcountry camping permit (only if loop is taken; needs verification)
- `wiki/hanksville.md` — link to the loop option
- `wiki/index.md` — added both new pages

**Open items**: confirm Tucson motel + street address; verify BLM 15000 road number, Dirty Devil ford conditions, Flint Trail status, and Orange Cliffs permit rules if the loop becomes a firm plan.

---

## 2026-07-05 — Babylon fire reroute (Aug 11–13)

**Source**: user update 2026-07-05 — Babylon fire burning south of the Needles district; area closed until end of July 2026, and reopening by Aug 12/13 cannot be assumed.

**Pages created**:
- `wiki/babylon-fire.md` — situation, impact table, reroute, and pre-trip checks

**Pages updated**:
- `wiki/schedule.md` — rows 19/20 and 20/21: dropped the Elk Ridge / Bears Ears crossing; Newspaper Rock "if open"; reroute US-191 → Monticello → Blanding → UT-95 → UT-261 → Muley Point, then as previously planned. Comb Wash CG now preferred for night 19/20 (Nizhoni CG possibly inside the closure). New planning note.
- `wiki/itinerary.md` — Leg 5: Horse Mountain row struck through as dropped; reroute note added
- `wiki/newspaper-rock.md` — fire caveat: check status before driving in on UT-211
- `wiki/natural-bridges-nm.md` — noted it is reached via the highway reroute, believed unaffected
- `wiki/index.md` — added babylon-fire to core pages

**Open items**: verify closure boundary and Newspaper Rock access closer to the trip (InciWeb / BLM Monticello); confirm Comb Wash vs Nizhoni for night 19/20.

---

## 2026-07-05 — Pocket fire (Sedona): Aug 13 train ride at risk

**Source**: user update 2026-07-05 — Pocket fire burning in the Sedona area, estimated to last months (until monsoon rains). Unknown whether the Verde Canyon Railroad is affected; hope is the railroad canyon is outside the smoke area. If affected, presumably skip Sedona.

**Pages created**:
- `wiki/pocket-fire.md` — situation, Aug 13 decision tree (train on → keep plan; train off → skip Sedona + train, Desert View slots into Aug 13), pre-trip checks

**Pages updated**:
- `wiki/schedule.md` — rows 21/22 and 22/23 flagged; Pocket fire caveat added to the August 13 timing note; new open item in summary
- `wiki/itinerary.md` — Leg 6: Sedona conditional, train flagged at risk
- `wiki/sedona.md` — visit now conditional on the fire
- `wiki/verde-canyon-railroad.md` — risk banner; geography note (Verde Canyon ≠ Oak Creek/Sedona canyon, ~20 mi west; plausibly outside smoke — needs verification); check status before trip
- `wiki/kids.md` — caveat on the train entry
- `wiki/index.md` — added pocket-fire to core pages

**Open items**: verify railroad operating status and smoke conditions shortly before Aug 13; decide Aug 13–14 fallback shape only once train status is known.
