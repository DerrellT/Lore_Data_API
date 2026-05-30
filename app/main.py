from fastapi import FastAPI, HTTPException
import json

# ----------------------------
# DATA LOADING LAYER
# ----------------------------

def check_json_files():
    """Loads JSON data from file into Python memory"""
    try:
        with open('data/lore_data.json') as f:
            lore_data = json.load(f) 
            return lore_data
    except FileNotFoundError:
        # If file path is wrong or missing, API cannot function properly
        print("Missing data file")
        return None

def search_lore(search_term, lore_data):
    """Search characters and regions using partial name matching."""
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



# Searches for a single character using an exact name match.
# Returns the character dictionary if found.
# Returns None if no character matches.
def search_character(search_char_by_name, lore_data):
    """Find a character using an exact name match."""
    for character in lore_data["characters"]:
        if character["name"].lower() == search_char_by_name: #looking for an exact match
            return character



# ----------------------------
# APP INITIALIZATION
# ----------------------------

app = FastAPI()  # creates the API server instance, what uvicorn runs

# Loads data ONCE when server starts into memory
lore_data = check_json_files()


# ----------------------------
# ROUTES (ENDPOINTS)
# ----------------------------

@app.get("/")
def home():
    """Return API status and verify data loaded correctly."""
    if not lore_data:
        return {"error": "File issue needs to be resolved"}
    return {"message": "API is running"}


@app.get("/lore/")
def get_all_lore():
    """Returns all data in the json dataset"""
    return lore_data

@app.get("/lore/{term}")
def get_lore(term): # This defines an API endpoint. When someone visits /lore/<term>. FastAPI passes <term> into this function.
    """Partial matching with multi search"""
    # Handles partial matching, returns a list and can look between both cahracters and regions
    search_term = term.lower()

    result = search_lore(search_term, lore_data)
    if not result:
        raise HTTPException(status_code=404, detail="Lore not found") 
    return result



#The route takes the value after /character/, converts it to lowercase for case-insensitive matching, passes it into search_character(), and returns the matching character if found. If no match is found, it raises a 404 error.
@app.get("/character/{name}")
def get_character(name):
    """Return a character by exact name match."""
    search_char_by_name = name.lower()
    result = search_character(search_char_by_name, lore_data) 
    if not result:
        raise HTTPException(status_code=404, detail="Character not found") 
    return result
