import json
import os

# Define the path to the cleaned JSON file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "cleaned_combined_games.json")

def load_games():
    if not os.path.exists(OUTPUT_FILE):
        raise FileNotFoundError(f"Error: {OUTPUT_FILE} does not exist. Run the database manager first.")

    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def search_games(query=None, filters=None, sort_by="rank", limit=None, offset=0, category=None):
    games = load_games()
    results = []
    sent_amount = 0
    current_result = 0
    # This runs for every game in the JSON, (Might need to optimise but whatever)
    for game in games:
        name = game.get("Name", "").lower().strip()
        tags = [tag.lower().strip() for tag in game.get("Tags", [])]

        if query is None or query.lower().strip() in name or any(query.lower().strip() in tag for tag in tags):
            match = True
            if query:
                # If the search query is in the game name or the name is in the quiry
                if name in query.lower().strip() or query.lower().strip() in name:
                    match = True
                else:
                    match = False
            # If there are any filters
            if filters:
                # Apply playtime filters
                if "min_playtime" in filters:
                    match = match and int(game.get("MfgPlaytime", 60)) >= filters["min_playtime"]
                if "max_playtime" in filters:
                    match = match and int(game.get("MfgPlaytime", 60)) <= filters["max_playtime"]
                # Apply player count filter
                if "player_count" in filters:
                    match = match and int(game.get("MinPlayers", 0)) <= filters["player_count"] 
                    match = match and int(game.get("MaxPlayers", 100)) >= filters["player_count"]
            if category:
                for cat in category:
                    if game.get(f"Cat:{cat}") != "1":
                        match = False
            
            # Adds the game to results if it matches the query and filters
            if match:
                if limit is None and offset == 0:
                    results.append(game)
                elif sent_amount < limit:
                    if offset > 0:
                        if current_result < offset:
                            current_result += 1
                        else:
                            results.append(game)
                            sent_amount += 1
                    else:
                        results.append(game)
                        sent_amount += 1                                           
                
    # Sorting the results
    if sort_by == "rank":
        results.sort(key=lambda g: int(g.get("NumOwned", 0)), reverse=True)
        results.sort(key=lambda g: int(g.get("Rank:boardgame", 999999)), reverse=False)
    elif sort_by == "owners":
        results.sort(key=lambda g: int(g.get("NumOwned", 0)), reverse=True)
    elif sort_by == "id":
        results.sort(key=lambda g: int(g.get("BGGId", 999999)), reverse=False)

    # Return
    if results == []:
        print("No results found for the given query or filters.")
        return None
    return results

def get_game(bgg_id, returned_fields='Name'):
    games = load_games()
    for game in games:
        if game.get("BGGId") == bgg_id:
            returned = {}
            name = game.get("Name", "Unknown")
            rank = game.get("Rank:boardgame", "N/A")

            if 'name' in returned_fields.lower():
                returned["Name"] = name
            if 'rank' in returned_fields.lower():
                returned["Rank"] = rank
            return returned

# --- Testing the system --- 
if __name__ == "__main__":
    # Testing search
    print("Search Results:")
    search_results = search_games(query="monopoly", sort_by="owners")
    for game in search_results:
        print(game.get("Name"), "-", game.get("Rank:boardgame", "N/A"), "-", game.get("BGGId", "N/A"), "-", game.get("NumOwned")) 
    print(f"Total games found: {len(search_results)}")
        
    # Testing search with limit and offset (Used for pages of stuff)
    print("\nSearch Results with offset 10 and limit 10:")
    search_results = search_games(query="monopoly", sort_by="owners", limit=10, offset=10)
    for game in search_results:
        print(game.get("Name"), "-", game.get("Rank:boardgame", "N/A"), "-", game.get("BGGId", "N/A"), "-", game.get("NumOwned")) 
    print(f"Total games found: {len(search_results)}")
        
    # Testing search with filters, a game with 40 min max playtime and can have 8 players and is party and family
    print("\nSearch Results with filters:")
    search_results = search_games(filters={"player_count": 8, "max_playtime": 40}, sort_by="owners", category=["Family", "Party"])  
    for game in search_results:
        print(game.get("Name"), "-", game.get("Rank:boardgame", "N/A"), "-", game.get("BGGId", "N/A"), "-", game.get("NumOwned")) 
        
    # Testing page system
    print("\nSearch pages:")
    search_results = search_games(limit=20, offset=10)
    for game in search_results:
        print(game.get("Name"), "-", game.get("Rank:boardgame", "N/A"), "-", game.get("BGGId", "N/A"), "-", game.get("NumOwned")) 
    
    # Testing get game
    print("\nGet Game:")
    print(get_game("174430", returned_fields='NameRank'))