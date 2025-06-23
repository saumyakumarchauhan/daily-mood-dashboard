import pandas as pd
import matplotlib.pyplot as plt
import calplot
from datetime import datetime
import os

# Ensure log.md exists
if not os.path.exists("log.md"):
    print("log.md not found.")
    exit()

# Define mappings
mood_map = {"😞": 1, "🙁": 2, "😐": 3, "🙂": 4, "😄": 5}
prod_map = {"Low": 1, "Medium": 2, "High": 3}

# Parse log.md
mood_entries = []
prod_entries = []

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
                prod = line.split("Productivity:")[1].split("|")[0].strip()
                mood_score = mood_map.get(mood, 3)
                prod_score = prod_map.get(prod, 2)
                mood_entries.append((current_date, mood_score))
                prod_entries.append((current_date, prod_score))
            except:
                continue

# Create plots directory
os.makedirs("plots", exist_ok=True)

# Generate Mood Heatmap
if mood_entries:
    df_mood = pd.DataFrame(mood_entries, columns=["Date", "Mood"])
    df_mood = df_mood.groupby("Date").mean()
    df_mood.index = pd.to_datetime(df_mood.index)

    calplot.calplot(
        df_mood["Mood"],
        cmap="YlGnBu",
        suptitle="📆 Mood Calendar Heatmap",
        colorbar=True
    )
    plt.savefig("plots/mood_calendar.png", bbox_inches="tight")
    plt.close()

# Generate Productivity Heatmap
if prod_entries:
    df_prod = pd.DataFrame(prod_entries, columns=["Date", "Productivity"])
    df_prod = df_prod.groupby("Date").mean()
    df_prod.index = pd.to_datetime(df_prod.index)

    calplot.calplot(
        df_prod["Productivity"],
        cmap="Oranges",
        suptitle="📈 Productivity Calendar Heatmap",
        colorbar=True
    )
    plt.savefig("plots/productivity_calendar.png", bbox_inches="tight")
    plt.close()

print("✅ Both heatmaps saved in 'plots/' folder.")
