import json
import os

# Define the path to the cleaned JSON file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "cleaned_combined_games.json")

def load_games():
    """Load the cleaned JSON file containing board game data."""
    if not os.path.exists(OUTPUT_FILE):
        raise FileNotFoundError(f"Error: {OUTPUT_FILE} does not exist. Run the database manager first.")

    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def search_games(query=None, filters=None, sort_by="rank"):
    """Search for games by name or tags, with optional filters and sorting."""
    games = load_games()
    results = []

    for game in games:
        name = game.get("Name", "").lower().strip()
        tags = [tag.lower().strip() for tag in game.get("Tags", [])]

        if query is None or query.lower().strip() in name or any(query.lower().strip() in tag for tag in tags):
            if filters:
                match = all(game.get(key) == value for key, value in filters.items())

                # Apply playtime filters
                if "min_playtime" in filters:
                    match = match and int(game.get("Playtime", 0)) >= filters["min_playtime"]
                if "max_playtime" in filters:
                    match = match and int(game.get("Playtime", 999999)) <= filters["max_playtime"]

                if match:
                    results.append(game)
            else:
                results.append(game)

    if sort_by == "rank":
        results.sort(key=lambda g: int(g.get("Rank:boardgame", 999999)), reverse=False)
    elif sort_by == "owners":
        results.sort(key=lambda g: int(g.get("NumOwned", 0)), reverse=True)

    return results

if __name__ == "__main__":
    # Example usage
    print("Search Results:")
    search_results = search_games(query="monopoly", sort_by="owners")
    for game in search_results:
        print(game.get("Name"), "-", game.get("Rank:boardgame", "N/A"), "-", game.get("BGGId", "N/A"), "-", game.get("NumOwned")) 
    print(f"Total games found: {len(search_results)}")