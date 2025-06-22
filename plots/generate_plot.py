import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import os

# Read the log file
if not os.path.exists("log.md"):
    print("log.md not found.")
    exit()

dates = []
moods = []

with open("log.md", "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("## Log Entry:"):
            timestamp = line.replace("## Log Entry:", "").strip()
            try:
                dates.append(datetime.strptime(timestamp, "%a %b %d %H:%M:%S %Y"))
            except:
                dates.append(datetime.utcnow())
        elif "Mood:" in line:
            mood = line.split("Mood:")[1].split()[0].strip()
            mood_score = {"😞": 1, "🙁": 2, "😐": 3, "🙂": 4, "😄": 5}.get(mood, 3)
            moods.append(mood_score)

if dates and moods:
    df = pd.DataFrame({"Date": dates, "Mood": moods})
    df.sort_values("Date", inplace=True)

    plt.figure(figsize=(10, 4))
    plt.plot(df["Date"], df["Mood"], marker='o', linestyle='-', color='teal')
    plt.ylim(0, 6)
    plt.yticks([1, 2, 3, 4, 5], ["Very Low", "Low", "Neutral", "Good", "Great"])
    plt.xlabel("Date")
    plt.ylabel("Mood")
    plt.title("Mood Trend Over Time")
    plt.grid(True)
    os.makedirs("plots", exist_ok=True)
    plt.tight_layout()
    plt.savefig("plots/mood_trend.png")
    plt.close()
