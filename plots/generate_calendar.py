import pandas as pd
import matplotlib.pyplot as plt
import calplot
from datetime import datetime, timezone
import os

# Read log.md
if not os.path.exists("log.md"):
    print("log.md not found.")
    exit()

entries = []
mood_map = {"😞": 1, "🙁": 2, "😐": 3, "🙂": 4, "😄": 5}

with open("log.md", "r", encoding="utf-8") as f:
    current_date = None
    for line in f:
        if line.startswith("## Log Entry:"):
            timestamp = line.replace("## Log Entry:", "").strip()
            try:
                dt = datetime.strptime(timestamp, "%a %b %d %H:%M:%S %Z %Y")
                current_date = dt.date()
            except:
                current_date = None
        elif "- Mood:" in line and current_date:
            try:
                mood = line.split("Mood:")[1].split("|")[0].strip()
                score = mood_map.get(mood, 3)
                entries.append((current_date, score))
            except:
                continue

# Build and group DataFrame
if entries:
    df = pd.DataFrame(entries, columns=["Date", "Mood"])
    df = df.groupby("Date").mean()
    df.index = pd.to_datetime(df.index)

    # Generate heatmap
    calplot.calplot(df["Mood"], cmap="YlGnBu", suptitle="📆 Mood Calendar Heatmap")
    os.makedirs("plots", exist_ok=True)
    plt.savefig("plots/mood_calendar.png", bbox_inches="tight")
    plt.close()
    print("✅ mood_calendar.png generated successfully.")
else:
    print("⚠️ No mood entries found.")
