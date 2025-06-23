import pandas as pd
import matplotlib.pyplot as plt
import calplot
from datetime import datetime, timezone
import os

# Read log.md
if not os.path.exists("log.md"):
    print("log.md not found.")
    exit()

dates = []
mood_scores = []

with open("log.md", "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("## Log Entry:"):
            timestamp = line.replace("## Log Entry:", "").strip()
            try:
                dt = datetime.strptime(timestamp, "%a %b %d %H:%M:%S UTC %Y")
            except:
                print(f"❌ Failed to parse date: {timestamp}")
                continue

            dates.append(dt)
        elif "Mood:" in line:
            mood = line.split("Mood:")[1].split()[0].strip()
            score = {"😞": 1, "🙁": 2, "😐": 3, "🙂": 4, "😄": 5}.get(mood, 3)
            mood_scores.append(score)

# Create DataFrame and group by day
if dates and mood_scores:
    df = pd.DataFrame({"Date": dates, "Mood": mood_scores})
    df["Date"] = pd.to_datetime(df["Date"]).dt.date  # Strip time part
    df = df.groupby("Date").mean()
    df.index = pd.to_datetime(df.index)  # Convert to DatetimeIndex

    # Generate and save heatmap
    calplot.calplot(df["Mood"], cmap="YlGnBu", suptitle="📆 Mood Calendar Heatmap")
    os.makedirs("plots", exist_ok=True)
    plt.savefig("plots/mood_calendar.png", bbox_inches="tight")
    plt.close()
