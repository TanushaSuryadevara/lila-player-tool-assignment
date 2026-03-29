# LILA BLACK — Player Journey Visualization Tool

A browser-based tool for Level Designers to explore 
player behavior across LILA BLACK's 3 maps using 
5 days of production gameplay data.

## Live Tool
https://lila-player-tool-assignment.vercel.app

## GitHub Repository
https://github.com/TanushaSuryadevara/lila-player-tool-assignment

## What It Does
- Plots 89,104 player events on game minimaps
- Distinguishes human players from bots visually
- Shows kills, deaths, loot, storm deaths as 
  distinct colored markers
- Filter by map, day, and event type
- Timeline playback to watch matches unfold
- Heatmap overlay showing kill zones and traffic

## How to Run Locally

### Requirements
- Python 3.11+
- pip install pandas pyarrow

### Steps
1. Clone the repository
2. Download player_data folder and place in same 
   directory as explore.py
3. Run the data pipeline:
   python explore.py
4. Start local server:
   python -m http.server 8000
5. Open browser at:
   http://localhost:8000

## Project Structure
```
lila_tool/
├── index.html          (frontend tool)
├── explore.py          (data pipeline)
├── events.json         (processed data)
├── ARCHITECTURE.md     (technical decisions)
├── INSIGHTS.md         (3 game insights)
├── AmbroseValley_Minimap.png
├── GrandRift_Minimap.png
└── Lockdown_Minimap.jpg
```

## Tech Stack
- Python + PyArrow + Pandas (data processing)
- Vanilla HTML + JavaScript (frontend)
- heatmap.js (heatmap overlay)
- Vercel (hosting)

## Data
- 5 days of production data (Feb 10-14, 2026)
- 1,243 parquet files
- 89,104 total events
- 3 maps: AmbroseValley, GrandRift, Lockdown
- 339 unique players, 796 unique matches
