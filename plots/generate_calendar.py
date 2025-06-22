import pandas as pd
import matplotlib.pyplot as plt
import calplot
from datetime import datetime
import os

# Check for log file
if not os.path.exists("log.md"):
    print("log.md not found.")
    exit()

# Initialize data holders
dates = []
mood_scores = []
current_date = None

# Define emoji to score mapping
emoji_to_score = {
    "😞": 1,
    "🙁": 2,
    "😐": 3,
    "🙂": 4,
    "😄": 5
}

# Parse log.md
with open("log.md", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith("## Log Entry:"):
            timestamp = line.replace("## Log Entry:", "").strip()
            try:
                current_date = datetime.strptime(timestamp, "%a %b %d %H:%M:%S %Y")
            except ValueError:
                print(f"⚠️ Skipping invalid timestamp: {timestamp}")
                current_date = None
        elif "Mood:" in line and current_date:
            mood_emoji = line.split("Mood:")[1].strip().split()[0]
            score = emoji_to_score.get(mood_emoji)
            if score:
                dates.append(current_date)
                mood_scores.append(score)
            else:
                print(f"⚠️ Unrecognized mood emoji: {mood_emoji}")
            current_date = None  # Reset to avoid reusing same date

# Check and process collected data
if dates and mood_scores and len(dates) == len(mood_scores):
    df = pd.DataFrame({"Date": dates, "Mood": mood_scores})
    df["Date"] = pd.to_datetime(df["Date"]).dt.date  # Strip time
    df = df.groupby("Date").mean()
    df.index = pd.to_datetime(df.index)  # Required for calplot

    # Create heatmap
    calplot.calplot(df["Mood"], cmap="YlGnBu", suptitle="📆 Mood Calendar Heatmap")

    # Save plot
    os.makedirs("plots", exist_ok=True)
    plt.savefig("plots/mood_calendar.png", bbox_inches="tight")
    plt.close()
    print("✅ Mood calendar saved to plots/mood_calendar.png")
else:
    print("⚠️ No valid mood logs found or mismatched dates and moods.")
