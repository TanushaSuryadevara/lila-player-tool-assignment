import pyarrow.parquet as pq
import pandas as pd
import os
import json

base = r"C:\Users\Tanusha\Downloads\player_data\player_data"
days = ["February_10","February_11","February_12","February_13","February_14"]

MAP_CONFIG = {
    "AmbroseValley": {"scale": 900, "origin_x": -370, "origin_z": -473},
    "GrandRift":     {"scale": 581, "origin_x": -290, "origin_z": -290},
    "Lockdown":      {"scale": 1000,"origin_x": -500, "origin_z": -500}
}

def to_pixel(x, z, map_id):
    cfg = MAP_CONFIG.get(map_id)
    if not cfg:
        return None, None
    u = (x - cfg["origin_x"]) / cfg["scale"]
    v = (z - cfg["origin_z"]) / cfg["scale"]
    px = u * 1024
    py = (1 - v) * 1024
    return round(px, 1), round(py, 1)

all_events = []

for day in days:
    folder = os.path.join(base, day)
    if not os.path.exists(folder):
        continue
    files = os.listdir(folder)
    print(f"Processing {day}: {len(files)} files")
    for fname in files:
        fpath = os.path.join(folder, fname)
        try:
            df = pq.read_table(fpath).to_pandas()
            df['event'] = df['event'].apply(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)
            parts = fname.split('_')
            is_bot = parts[0].isdigit()
            for _, row in df.iterrows():
                px, py = to_pixel(row['x'], row['z'], row['map_id'])
                if px is None:
                    continue
                all_events.append({
                    "uid": str(row['user_id']),
                    "mid": str(row['match_id']),
                    "map": row['map_id'],
                    "day": day,
                    "x": px,
                    "y": py,
                    "event": row['event'],
                    "ts": str(row['ts']),
                    "bot": is_bot
                })
        except Exception as e:
            continue

print(f"\nTotal events processed: {len(all_events)}")

output = r"C:\Users\Tanusha\Desktop\lila_tool\events.json"
with open(output, 'w') as f:
    json.dump(all_events, f)

print(f"Saved to events.json")
print("DONE!")

