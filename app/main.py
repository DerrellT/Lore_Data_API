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

def search_lore(search_term, lore_data):
    results = [] # created list to be added onto
    for character in lore_data["characters"]:
        if search_term in character["name"].lower():
            results.append({ 
                "type": "Character", #now it can filter by "type"
                "data": character}) #goes through and adds all partial matches to a resutl list
    for region in lore_data["regions"]:
        if search_term in region["name"].lower():
            results.append({
                "type": "Region",
                "data": region})
    return results #collects the list that has been made
     

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
    if not lore_data:
        return {"error": "File issue needs to be resolved"}
    return {"message": "API is running"}


@app.get("/lore/")
def get_all_lore():
    # Endpoint: returns all characters from loaded dataset
    return lore_data

@app.get("/lore/{term}")
def get_lore(term):
    # This defines an API endpoint.
    # When someone visits /characters/<name>,
    # FastAPI passes <name> into this function.

    search_term = term.lower()
    # Convert user input to lowercase.
    result = search_lore(search_term, lore_data)
    if not result:
        return {"error": "No matches found"} # If loop finishes with no match return an error message instead of returning nothing.
 
    return result


