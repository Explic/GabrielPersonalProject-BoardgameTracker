import json
import os
from collections import Counter

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

def recommend_games(input_bgg_ids, num_recommendations=20):
    """Recommend games similar to the input list of BGGIds."""
    all_games = load_games()
    input_games = [game for game in all_games if game.get("BGGId") in input_bgg_ids]

    if not input_games:
        print("No matching games found for the provided BGGIds.")
        return

    recommendations = []

    for game in all_games:
        score = 0

        for input_game in input_games:
            # Compare tags
            input_tags = set(input_game.get("Tags", []))
            game_tags = set(game.get("Tags", []))
            score += len(input_tags & game_tags)

            # Add 2 points for each matching theme
            input_themes = {tag for tag in input_tags if tag.startswith("Theme:")}
            game_themes = {tag for tag in game_tags if tag.startswith("Theme:")}
            score += len(input_themes & game_themes) * 2  # Give more weight to themes

            # Add a point for similar playtime
            input_playtime = int(input_game.get("ComMaxPlaytime", 0))
            game_playtime = int(game.get("ComMaxPlaytime", 0))
            if abs(input_playtime - game_playtime) <= 30:  # Allow a 30-minute difference
                score += 1

            # Compare difficulty
            input_difficulty = float(input_game.get("GameWeight", 0))
            game_difficulty = float(game.get("GameWeight", 0))
            if abs(input_difficulty - game_difficulty) <= 0.5:  # Allow a 0.5 difference
                score += 1
                
            #Giving popular games an advantage
            if int(game.get("NumOwned", 0)) > 1000:
                score += 0.5
            
            # Games with a high bgg rank are more likely to be recommended
            if int(game.get("Rank:boardgame", 999999)) < 100:
                score += 0.5
            
            # Add 2 points for each matching category (Cat) tag
            input_cats = {i for i, value in input_game.items() if i.startswith("Cat:") and value == "1"}
            game_cats = {i for i, value in game.items() if i.startswith("Cat:") and value == "1"}
            score += len(input_cats & game_cats) * 2
        
        # Makes it so that the game itself is not recommended
        if game.get("BGGId") in input_bgg_ids:
            score = 0

        if score > 0:
            recommendations.append((score, game))

    # Sort recommendations by score (highest first) and return the top results
    recommendations.sort(reverse=True, key=lambda x: x[0])
    return [game for _, game in recommendations[:num_recommendations]]

if __name__ == "__main__":
    # Example usage / testing
    example_bgg_ids = ["174430", "161936"]  # Gloomhaven + pand

    recommendations = recommend_games(example_bgg_ids)
    print("Recommended Games for Gloomhaven:")
    for game in recommendations:
        print(game.get("Name"))
        
    example_bgg_ids = ["161936"]  # Pandemic Legacy: Season 1
    recommendations = recommend_games(example_bgg_ids)
    print("\n\nRecommended Games for Pandemic:")
    for game in recommendations:
        print(game.get("Name"))

