# 📸 Instagram View Tracker

A Python automation tool that tracks Instagram Reel statistics and automatically updates a Google Sheets dashboard.

---

## ✨ Features

- 📊 Count total reels on each Instagram account
- 👀 Calculate total reel views
- 📈 Update Google Sheets automatically
- 🚀 Fast Playwright automation
- 🔐 Uses your logged-in Chrome profile
- ✅ Skip inactive or suspended accounts
- 📋 Clean terminal progress output

---

## 🛠️ Tech Stack

- Python 3.14
- Playwright
- Google Sheets API
- gspread
- pandas
- python-dotenv

---

## 📂 Project Structure

```
instagram-view-tracker/
│
├── browser.py
├── config.py
├── instagram.py
├── sheets.py
├── main.py
├── requirements.txt
├── credentials.json
├── .gitignore
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/zeeshan-aidev/instagram-view-tracker.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browser

```bash
python -m playwright install chromium
```

Run

```bash
python main.py
```

---

## 📸 Workflow

```
Google Sheets
        │
        ▼
Read Active Accounts
        │
        ▼
Open Instagram
        │
        ▼
Count Reels
        │
        ▼
Calculate Total Views
        │
        ▼
Update Google Sheet
```

---

## 🗺️ Roadmap

- [x] Google Sheets Integration
- [x] Instagram Login
- [x] Reel Counter
- [ ] Automatic Daily Updates
- [ ] Retry Failed Accounts
- [ ] Better Error Logging
- [ ] GUI Version
- [ ] Multi-Account Support

---

## 👨‍💻 Author

**Zeeshan Ali**

Python Developer • Automation Enthusiast

GitHub:
https://github.com/zeeshan-aidev
