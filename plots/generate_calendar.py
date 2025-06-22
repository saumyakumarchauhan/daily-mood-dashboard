import pandas as pd
import calplot
import os
from datetime import datetime
import matplotlib.pyplot as plt

if not os.path.exists("log.md"):
    print("log.md not found.")
    exit()

dates, mood_scores = [], []

with open("log.md", "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("## Log Entry:"):
            timestamp = line.replace("## Log Entry:", "").strip()
            try:
                current_date = datetime.strptime(timestamp, "%a %b %d %H:%M:%S %Y").date()
            except:
                current_date = datetime.utcnow().date()
        elif "Mood:" in line:
            mood = line.split("Mood:")[1].split("|")[0].strip()
            mood_score = {"😞": 1, "🙁": 2, "😐": 3, "🙂": 4, "😄": 5}.get(mood, 3)
            dates.append(current_date)
            mood_scores.append(mood_score)

if dates and mood_scores:
    df = pd.DataFrame({"Date": dates, "Mood": mood_scores})
    df = df.groupby("Date").mean()

    calplot.calplot(df["Mood"], cmap="YlGnBu", figsize=(10, 4), suptitle="📆 Mood Calendar Heatmap")
    os.makedirs("plots", exist_ok=True)
    plt.savefig("plots/mood_calendar.png")
    plt.close()
