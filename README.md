# Lore Data API

A beginner backend API built with FastAPI that serves structured lore data stored in a local JSON file.

---

## Project Purpose

This project was built to learn core backend development concepts using Python and FastAPI, including:

- Building REST API endpoints
- Loading and serving JSON data
- Understanding request/response flow
- Learning server architecture and routing
- Practicing clean separation between data and API logic

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- JSON (local data storage)

---

## Features (Current Stage)

- Basic FastAPI server setup
- Root endpoint to confirm API is running
- `/characters` endpoint that returns all character data from JSON
- JSON file loaded once at server startup

---

## 📁 Project Structure
Lore Data API/
│
├── main.py              # FastAPI application
├── data/
│   └── lore_data.json   # Local dataset
└── venv/                # Virtual environment (not pushed to GitHub)

---

## ▶️ How to Run

1. Activate virtual environment:
source venv/bin/activate
2. Install dependencies:
pip install fastapi uvicorn
3. Start server:
python3 -m uvicorn main:app –reload
4. Open in browser:
http://127.0.0.1:8000
http://127.0.0.1:8000/characters
http://127.0.0.1:8000/docs

---

## 🧠 What I Learned

- How APIs handle requests and responses
- Difference between CLI apps and web APIs
- How to structure backend code
- How data flows from file → server → client
- Basics of REST API design

---

## 📌 Future Improvements

- Add character lookup by name
- Add region endpoints
- Add search functionality
- Improve API structure (modular files)
- Add error handling improvements

---

## ⚠️ Notes

This is a learning project focused on backend fundamentals, not production deployment.

---