# Architecture Document

## What I Built
A browser-based player journey visualization tool that 
lets Level Designers at Lila Games explore 89,104 player 
events across 3 maps and 5 days of production gameplay 
data from LILA BLACK.

## Tech Stack

| Layer | Tool | Why |
|-------|------|-----|
| Data processing | Python + PyArrow + Pandas | Best native support for Parquet format. Simple to run locally. |
| Frontend | Vanilla HTML + JavaScript | No framework needed. Fast to build, works in any browser. |
| Heatmap | heatmap.js | Lightweight library, works directly on canvas overlay. |
| Data format | JSON | Easy to load in browser, no backend server needed. |
| Hosting | Vercel | Free, one-click deploy from GitHub, instant shareable URL. |

## Data Flow
```
1. RAW DATA
   1,243 Parquet files across 5 day folders
   (February 10-14, 2026)
         ↓
2. PYTHON PIPELINE (explore.py)
   - Reads every file using PyArrow
   - Decodes event column from bytes to string
   - Detects human vs bot from filename pattern
     (UUID = human, numeric ID = bot)
   - Converts world coordinates (x,z) to 
     pixel positions on 1024x1024 minimap
   - Tags each event with map, day, match ID
         ↓
3. OUTPUT
   Single events.json file — 89,104 events
   Each event has: map, day, pixel x/y, 
   event type, timestamp, bot flag
         ↓
4. FRONTEND (index.html)
   - Loads events.json via fetch()
   - Displays minimap image as background
   - Plots events as colored dots on canvas
   - Filters by map, day, event type
   - Timeline slider scrubs through timestamps
   - Heatmap mode aggregates dot density
         ↓
5. LEVEL DESIGNER
   Opens URL in browser, explores patterns,
   makes informed map design decisions
```

## Coordinate Mapping

The README provided map-specific configuration:

| Map | Scale | Origin X | Origin Z |
|-----|-------|----------|----------|
| AmbroseValley | 900 | -370 | -473 |
| GrandRift | 581 | -290 | -290 |
| Lockdown | 1000 | -500 | -500 |

Conversion formula:
```
u = (x - origin_x) / scale
v = (z - origin_z) / scale
pixel_x = u * 1024
pixel_y = (1 - v) * 1024  ← Y flipped (image origin top-left)
```

Note: The y column in the data represents elevation 
and is ignored for 2D minimap plotting.

## Assumptions Made

- February 14 data is included but noted as partial day
- Bot detection uses filename pattern only
  (numeric user_id prefix = bot)
- Timestamps represent time within match context,
  not wall clock time
- All maps use 1024x1024 pixel minimap images

## Tradeoffs

| Decision | Gained | Given Up |
|----------|--------|----------|
| Static JSON file | Fast load, no backend needed | Data is not real-time |
| Vanilla JS | Simple, no dependencies | Less scalable UI |
| Pre-process all days | Complete picture | Large JSON file size |
| Canvas rendering | Fast dot plotting | No click-on-dot interaction |

## What I Would Do With More Time

1. Real-time pipeline — automate daily data refresh
   so designers always see fresh data without 
   manual processing

2. Match selector — with 796 unique matches, 
   designers need a searchable match list to 
   focus on specific sessions

3. Player tracking — follow one player across 
   multiple matches to identify power users 
   vs struggling players

4. Storm path overlay — request actual storm 
   boundary data from backend team and overlay 
   it on the map to contextualize storm deaths

5. Statistical significance — add minimum 
   threshold filters so designers don't 
   over-index on thin data patterns