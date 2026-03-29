# Player Behavior Insights — LILA BLACK

## Insight 1 — The Northwest Corner is a Dead Zone

### What I noticed
When viewing Ambrose Valley with all events plotted,
the northwest corner of the map has almost zero 
activity across all 5 days of data. No kills, minimal
loot pickups, almost no player movement.

### The evidence
- Total events on AmbroseValley: 61,013
- Combat events: 2,287 — almost all concentrated 
  in the center-right of the map
- Northwest quadrant visible as dark/empty area 
  even with all event types enabled
- Pattern consistent across all 5 days — 
  not a one-day anomaly

### What this means for a Level Designer
Players are voting with their feet. The northwest 
corner offers them nothing worth going to — no 
compelling loot, no natural traffic routes, no 
strategic advantage. This is wasted map real estate.

### Actionable recommendation
- Add high-value loot spawns in the northwest corner
  to create a risk/reward reason to go there
- Consider adding a point of interest (building, 
  landmark) that creates natural traffic
- Metric to track: % of matches with at least one 
  player entering northwest quadrant
  (current estimate: under 15%)

---

## Insight 2 — Storm Deaths are Surprisingly Low

### What I noticed
With a storm mechanic that is supposed to force 
player movement and create urgency, only 17 storm 
deaths were recorded on Ambrose Valley across 
all 5 days and hundreds of matches.

### The evidence
- Total matches on AmbroseValley across 5 days: 
  estimated 500+ matches
- KilledByStorm events: only 17 total
- Ratio: less than 1 storm death per 30 matches
- By comparison: 2,287 combat events in same period
- Storm deaths are 0.03% of all non-movement events

### What this means for a Level Designer
Either players are successfully extracting before 
the storm reaches them (good — intended behavior) 
or the storm is moving too slowly to create real 
pressure (bad — intended tension is missing).
17 deaths across hundreds of matches suggests 
the storm may not be a meaningful threat on this map.

### Actionable recommendation
- Review storm speed and direction on AmbroseValley
- Compare storm death rate across all 3 maps —
  if GrandRift and Lockdown have higher rates,
  AmbroseValley storm needs rebalancing
- Consider whether storm path is too predictable,
  allowing players to always stay ahead of it
- Metric to track: storm death rate per match
  (target should be 10-15% of matches having 
  at least one storm death for meaningful tension)

---

## Insight 3 — Loot Distribution Does Not Match Combat Distribution

### What I noticed
Loot pickups (9,955 events) are spread across the 
entire map including edges and quiet areas. But 
combat (2,287 events) is heavily concentrated in 
the center. This mismatch means players are looting 
in one area then fighting in another — suggesting 
loot is not driving players toward conflict zones.

### The evidence
- Loot pickups: 9,955 spread across full map
- Combat events: 2,287 concentrated center-right
- Loot to combat ratio in center: much lower than 
  expected if loot was driving players there
- Edge areas show loot activity but near-zero combat
- Players appear to loot safely then rotate to 
  fight zones separately

### What this means for a Level Designer
When loot and combat zones don't overlap, players 
can loot safely without risk. This reduces tension 
and makes the early game feel too safe. The best 
extraction shooters force players to make risky 
decisions about whether to loot or fight.

### Actionable recommendation
- Move high-value loot spawns closer to natural 
  conflict zones in the center of the map
- Create loot-rich areas that also have poor cover —
  forcing players to be exposed while looting
- Add loot to the northwest dead zone to 
  simultaneously solve Insight 1
- Metric to track: average distance between 
  a player's last loot event and their death 
  location (shorter = better design tension)