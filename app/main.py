from fastapi import FastAPI
import json

# ----------------------------
# DATA LOADING LAYER
# ----------------------------

def check_json_files():
    # Loads JSON data from file into Python memory
    # This is part of "startup initialization" logic (not request logic)
    lore_data = None
    try:
        with open('data/lore_data.json') as f:
            lore_data = json.load(f)  # converts JSON → Python dict
            return lore_data
    except FileNotFoundError:
        # If file path is wrong or missing, API cannot function properly
        print("Missing data file")
        return None


# ----------------------------
# APP INITIALIZATION
# ----------------------------

app = FastAPI()  # creates the API server instance (this is what uvicorn runs)

# Loads data ONCE when server starts (important backend concept: startup state)
lore_data = check_json_files()


# ----------------------------
# ROUTES (ENDPOINTS)
# ----------------------------

@app.get("/")
def home():
    # Health check endpoint
    # Used to confirm API is running correctly
    return {"message": "API is running"}


@app.get("/characters")
def character():
    # Endpoint: returns all characters from loaded dataset
    # We are NOT searching or filtering yet — just exposing data
    names_of_chars = lore_data["characters"]
    return names_of_chars