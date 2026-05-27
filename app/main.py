from fastapi import FastAPI
import json

# ----------------------------
# DATA LOADING LAYER
# ----------------------------

def check_json_files():
    # Loads JSON data from file into Python memory
    # This is part of "startup initialization" logic (not request logic)
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


@app.get("/characters/")
def get_all_characters():
    # Endpoint: returns all characters from loaded dataset
    return lore_data["characters"]

@app.get("/characters/{name}")
def get_character(name):
    # This defines an API endpoint.
    # When someone visits /characters/<name>,
    # FastAPI passes <name> into this function.


    search_name = name.lower()
    # Convert user input to lowercase.

    for character in lore_data["characters"]:

        character_name = character["name"].lower()
        # Convert the stored character name to lowercase

        if search_name in character_name:
            # Check if user input appears inside the character name,and partial matching
            return character

    return {"error": "Character not found"} # If loop finishes with no match return an error message instead of returning nothing.
