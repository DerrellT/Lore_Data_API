# Lore Data API

Backend API built with FastAPI that serves structured lore data from a local JSON dataset, with support for data retrieval and search-based queries.

---

## Project Purpose

This project was built to develop foundational backend engineering skills using Python and FastAPI, including:

- Designing REST API endpoints
- Handling JSON-based data pipelines
- Understanding request/response lifecycle
- Structuring backend applications
- Implementing basic search logic over structured data

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- JSON (local data layer)

---

## Features (Current Stage)

- FastAPI server with modular structure
- Health check endpoint (/)
- Full dataset endpoint (/characters)
- Search endpoint with partial matching logic
- JSON data loaded once at server startup for efficiency

---

## API Endpoints

- GET / → API health check
- GET /lore → returns all character data
- GET /lore/{term} → returns matching characters and regions using partial search

---

## Project Structure
Lore Data API/
│
├── main.py              # FastAPI application
├── data/
│   └── lore_data.json   # Local dataset
└── venv/                # Virtual environment (not pushed to GitHub)

---

## How to Run

1. Activate virtual environment:
source venv/bin/activate
2. Install dependencies:
pip install fastapi uvicorn
3. Start server:
python3 -m uvicorn main:app –reload
4. Open in browser:
http://127.0.0.1:8000
http://127.0.0.1:8000/lore
http://127.0.0.1:8000/docs

---

## What I Learned

- REST API design fundamentals
- Difference between CLI and web-based architectures
- How request/response cycles work in FastAPI
- JSON data handling in backend systems
- Basic search logic and filtering over structured data

---

## Future Improvements

- Add exact-match character lookup endpoint
- Improve error handling with HTTP status codes
- Refactor into modular backend structure
- Expand dataset relationships (characters ↔ regions)
---

## Notes

This project focuses on backend fundamentals and API design principles rather than production deployment or full-stack architecture.

---