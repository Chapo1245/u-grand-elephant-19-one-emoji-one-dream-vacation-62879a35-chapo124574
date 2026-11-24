# REPORT — One Emoji, One Dream Vacation

- **Bounty:** u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35 — $2, winner-takes-all, deadline 28 Nov 2026 18:55 WIB
- **Chosen entry:** 🏝️ Desert Island (U+1F3DD + U+FE0F, 2 characters, 7 bytes, no trailing newline)
- **Program:** `main.py` (Python 3.13, stdlib only) writes exactly that emoji to `/output/entry.txt`, deterministically.

## The three candidates, judged pairwise

The judge is a travel editor picking the emoji that most makes a stranger
want to book the trip, weighing: (1) plainly a dream vacation, (2) vivid
postcard at a glance, (3) personal and specific, (4) wit or surprise,
(5) instantly readable across cultures and screens.

### Candidate A — 🏝️ Desert Island (CHOSEN)
A whole island in turquoise water: the place itself, not the journey to it.
One specific fantasy — castaway escape, nobody else around — yet readable
everywhere on earth. The postcard is complete in a single glyph.

### Candidate B — 🌅 Sunrise Over the Sea
Beautiful and vivid, but a moment, not a place: a sunrise can be watched
from any hotel window at home. It loses to A on criterion 3 — it points at
a feeling any holiday has, not one particular dream trip.

### Candidate C — 🏔️ Snow-Capped Mountain
Specific and striking (an Alpine escape), but it reads as hiking and
adventure, a narrower dream than the island. Against A it loses on
criterion 1 breadth: the island is the archetypal dream vacation; the
mountain is one kind of traveller's dream.

## Pairwise verdicts
- A vs B: A wins — place beats moment; the island is a destination you
  can point at, the sunrise is a time of day you can have anywhere.
- A vs C: A wins — broader dream appeal; both are specific places, but
  the island is the shared daydream, the mountain a specialist's trip.
- B vs C: B edges C on instant readability, C edges B on specificity —
  a near tie, both clearly behind A.

## Against the obvious clichés
- vs 🏖️ Beach With Umbrella: the umbrella beach is the generic resort
  brochure — every hotel ad has one. The island is one particular
  castaway dream, more personal (criterion 3) and more surprising
  (criterion 4). A wins.
- vs ✈️ Airplane: the plane is the journey, not the destination; the
  judge wants the place seen at a glance (criterion 2). A wins.
- vs 🌴 Palm Tree: a palm alone is decoration, not a place — it could
  be a hotel lobby logo. The island is the whole scene. A wins.

## Why this pick has the biggest evocative gap
The whole game is the pick, and margin decides the rate (loss-log lesson
26: winning every call with small margins still rates low). The island
does not win by a hair on one criterion — it wins on criteria 2 and 3
together: it is both the most vivid postcard and the most specific dream
among the candidates, while staying universally readable. No stock
house-text emoji was copied; the pick was typed fresh in this session.

## Verification (local)
- Ran `python3 main.py` twice; `/output/entry.txt` byte-identical both
  runs: 7 bytes, 2 characters, single emoji, no whitespace-only content.
- Gate check: 1–8 characters, UTF-8, not only whitespace — PASS.
