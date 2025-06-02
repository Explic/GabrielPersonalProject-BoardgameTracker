import json
import os

# Define the path to the cleaned JSON file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "cleaned_combined_games.json")

def print_top_10_ranked_games():
    """Load the cleaned JSON file and print the top 10 ranked board games."""
    if not os.path.exists(OUTPUT_FILE):
        print(f"Error: {OUTPUT_FILE} does not exist. Run the database manager first.")
        return

    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        games = json.load(f)

    # Print the top 10 ranked games
    print("Top 10 Ranked Board Games:")
    for i, game in enumerate(games[:10], start=1):
        rank = game.get("Rank:boardgame", "N/A")
        name = game.get("Name", "Unknown")
        print(f"{i}. {name} (Rank: {rank})")

if __name__ == "__main__":
    print_top_10_ranked_games()
