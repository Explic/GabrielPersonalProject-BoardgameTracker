import csv
import json
import os
from tqdm import tqdm

# === File Paths ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "cleaned_combined_games.json")


# === CSV Loader ===
def load_csv_to_dict(filename, key_field):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        print(f"Warning: {filename} not found. Skipping.")
        return {}
    data = {}
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[row[key_field]] = row
    return data


# === Binary Tag Extractor ===
def extract_active_tags(row, label_prefix):
    return [f"{label_prefix}:{key}" for key, value in row.items() if value == "1" and key != "BGGId"]


# === Merger and Cleaner ===
def merge_and_clean_datasets():
    games = load_csv_to_dict("GAMES.csv", "BGGId")
    mechanics = load_csv_to_dict("MECHANICS.csv", "BGGId")
    themes = load_csv_to_dict("THEMES.csv", "BGGId")
    subcategories = load_csv_to_dict("SUBCATEGORIES.csv", "BGGId")
    artists = load_csv_to_dict("ARTISTS_REDUCED.csv", "BGGId")

    combined = []

    print("Merging and cleaning datasets...")
    for bgg_id in tqdm(games, desc="Processing Games", unit="game"):
        game_data = games[bgg_id].copy()

        # Merge tags
        tags = []
        if bgg_id in mechanics:
            tags += extract_active_tags(mechanics[bgg_id], "Mechanic")
        if bgg_id in themes:
            tags += extract_active_tags(themes[bgg_id], "Theme")
        if bgg_id in subcategories:
            tags += extract_active_tags(subcategories[bgg_id], "Subcategory")
        game_data["Tags"] = tags

        # Merge artists
        game_data["Artists"] = []
        if bgg_id in artists:
            game_data["Artists"] = [
                name for name, val in artists[bgg_id].items()
                if val == "1" and name not in ("BGGId", "Low-Exp Artist")
            ]

        combined.append(game_data)

    return combined


# === Sorter by Rank then ID ===
def sort_combined_data(games):
    def sort_key(game):
        try:
            rank = int(game.get("Rank:boardgame", ""))
            if rank <= 0 or rank >= 999999:
                raise ValueError
            return (0, rank)  # Ranked games come first
        except (ValueError, TypeError):
            return (1, int(game.get("BGGId", "99999999")))  # Unranked sorted by ID
    return sorted(games, key=sort_key)


# === Save Final Cleaned File ===
def save_cleaned_dataset():
    os.makedirs(DATA_DIR, exist_ok=True)
    combined = merge_and_clean_datasets()
    sorted_combined = sort_combined_data(combined)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted_combined, f, indent=2)
    print(f"\nSaved {len(sorted_combined)} sorted games to: {OUTPUT_FILE}")


# === CLI Entry Point ===
if __name__ == "__main__":
    save_cleaned_dataset()
    print("Database manager executed successfully.")
