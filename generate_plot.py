import re 
from datetime import datetime
import matplotlib.pyplot as plt 
import os

mood_map = {
    "😊": "Happy", "😌": "Calm", "😐": "Okay", "😴": "Tired", "😔": "Sad", "😄": "Excited"
}

dates = []
moods = []

# Parse log.md

with open("log.md", "r", encoding="utf-8") as f:
    content = f.read()

entries = content.split("## 🗓️ ")[1:]

for entry in entries:
    lines = entry.strip().splitlines()
    date = lines[0].strip()
    mood_line = next((line for line in lines if "Mood:" in line), "")
    emoji = re.findall(r'[^\w\s]', mood_line)
    if emoji:
        mood = mood_map.get(emoji[0], "Unknown")
        dates.append(datetime.strptime(date, "%Y-%m-%d"))
        moods.append(mood)
        
# skip if not enough data

if len(dates) < 2:
    exit()
    
# Plot
plt.figure(figsize=(10, 4))
plt.plot(dates, moods, marker='o', linestyle='-', color='teal')
plt.xticks(rotation=45)
plt.title("Mood Trend Over Time")
plt.ylabel("Mood")
plt.tight_layout()

#save 
os.makedirs("plots", exist_ok=True)
plt.savefig("plots/mood_trend.png")