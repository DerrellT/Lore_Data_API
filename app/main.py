from fastapi import FastAPI, HTTPException
import json

# ----------------------------
# DATA LOADING LAYER
# ----------------------------

def check_json_files():
    # Loads JSON data from file into Python memory
    # This is part of startup initialization
    try:
        with open('data/lore_data.json') as f:
            lore_data = json.load(f) 
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

app = FastAPI()  # creates the API server instance, what uvicorn runs

# Loads data ONCE when server starts into memory
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
    return lore_data

@app.get("/lore/{term}")
def get_lore(term): # This defines an API endpoint. When someone visits /lore/<term>. FastAPI passes <term> into this function.
    # Handles partial matching, returns a list and can look between both cahracters and regions

    result = search_lore(search_term, lore_data)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found") 
    return result

#high level
# Creates FastApi server
# loads json dataset once into memory
# shows endpoints for user to retrieve data from chars or regions
# seearch function returns type and its data

#system flow
# request comes in /lore/term
# FastAPI receives it
# route function runs
# search function filters JSON
# response returned


#zoomed in
# search function logic
# data loading
# why lowercase matching works