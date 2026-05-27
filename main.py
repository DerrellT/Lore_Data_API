from fastapi import FastAPI
import json

def check_json_files():
    lore_data = None
    try :
        with open('data/lore_data.json') as f:
            lore_data = json.load(f)
            return lore_data
    except FileNotFoundError:
        print("Missing datat")
        return None


app = FastAPI() #server starts
lore_data = check_json_files() #loads JSON once
    
@app.get("/")
def home(): #function that runs when route is hit

    return {"message": "API is running"} #This becomes JSON in the browser.

@app.get("/characters")
def character():
    names_of_chars = lore_data["characters"] #access names of characters in json file and returns it
    return names_of_chars