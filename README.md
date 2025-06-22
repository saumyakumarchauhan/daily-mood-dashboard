# 🧘‍♂️ Daily Mood & Productivity Dashboard

A fully automated personal dashboard that tracks your **daily mood and productivity**, visualizes trends using Python, and publishes updates via **GitHub Pages**.

This project uses **GitHub Actions** to run daily, log your entries into `log.md`, generate a trend graph, and update a live HTML dashboard — all without your manual intervention.

---

## 🚀 Features

- ✅ **Daily automation** with GitHub Actions
- 📊 **Mood trend visualization** using Matplotlib
- 🌐 **GitHub Pages dashboard** (auto-updated)
- 📝 Simple markdown log (`log.md`)
- 🔒 Lightweight, open-source, and privacy-friendly

---

## 🗂 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── daily-log.yml        # GitHub Actions workflow
├── docs/
│   ├── dashboard.html           # HTML dashboard template
│   ├── index.html               # GitHub Pages entrypoint
│   ├── log.md                   # Copied daily log
│   └── mood_trend.png           # Copied chart
├── plots/
│   └── generate_plot.py         # Chart generation logic
├── log.md                       # Main mood log
├── README.md                    # This file
```

---

## 🧠 How It Works

1. **Workflow Trigger**  
   - Automatically runs every day at 9:30 AM IST  
   - Also manually runnable from the GitHub Actions tab

2. **Log Entry**  
   - Appends a new timestamped entry to `log.md`

3. **Plot Generation**  
   - Reads `log.md` and generates `mood_trend.png`

4. **Publishing**  
   - Copies files to the `docs/` folder
   - GitHub Pages auto-publishes it

---

## 🔧 Setup Instructions

1. **Fork or Clone This Repo**

```bash
git clone https://github.com/YOUR_USERNAME/daily-mood-dashboard.git
cd daily-mood-dashboard
```

2. **Push to GitHub**

```bash
git remote add origin https://github.com/YOUR_USERNAME/daily-mood-dashboard.git
git branch -M main
git push -u origin main
```

3. **Enable GitHub Pages**
   - Go to your repo → **Settings** → **Pages**
   - Source: `main` branch, `/docs` folder
   - Click **Save**

4. **Run Manually Once**
   - Go to **Actions** tab → Click on `Daily Mood and Productivity Logger` → Run workflow

---

## 🌐 Live Dashboard

> 🔗 [Click here to view the dashboard](https://your-username.github.io/daily-mood-dashboard/)

_(replace with your actual username and repo name)_

---

## 📈 Future Ideas

- Prompt for mood using GitHub issues
- Add `sleep`, `stress`, or `focus` metrics
- Export logs to Google Sheets or Notion

---

## 📜 License

This project is licensed under the MIT License.  
© 2025 **Saumyakumar Chauhan**, B.Tech in CSE from IIIT Kota and B.S. in Data Science from IIT Madras.
