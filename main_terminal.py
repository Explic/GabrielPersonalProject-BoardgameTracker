from src.backend import *
import cutie
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu(title, options):
    print(title)
    x = cutie.select(options)
    clear()
    return x

def showcase_user_management():
    print("User Management Showcase")
    options = ["Signup", "Login", "Manage Wishlist", "Back"]
    while True:
        choice = menu("User Management", options)
        if choice == 0:  # Signup
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(signup(username, password))
        elif choice == 1:  # Login
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(login(username, password))
        elif choice == 2:  # Manage Wishlist
            username = input("Enter username: ")
            wishlist_options = ["Add to Wishlist", "Remove from Wishlist", "View Wishlist", "Back"]
            while True:
                wishlist_choice = menu("Wishlist Management", wishlist_options)
                if wishlist_choice == 0:  # Add to Wishlist
                    game_id = input("Enter game ID to add: ")
                    print(add_to_wishlist(username, game_id))
                elif wishlist_choice == 1:  # Remove from Wishlist
                    game_id = input("Enter game ID to remove: ")
                    print(remove_from_wishlist(username, game_id))
                elif wishlist_choice == 2:  # View Wishlist
                    print(get_wishlist(username))
                elif wishlist_choice == 3:  # Back
                    break
        elif choice == 3:  # Back
            break

def showcase_recommendations():
    print("Recommendations Showcase")
    while True:
        bgg_ids = input("Enter BGG IDs (comma-separated): ").split(',')
        recommendations = recommend_games(bgg_ids)
        print("Recommended Games:")
        if recommendations == None:
            print("Error: ID not found")
        else:
            for game in recommendations:
                print(game.get("Name"))
        if not cutie.prompt_yes_or_no("Do you want to try again?"):
            break

def showcase_search():
    print("Search Showcase\nSelect search options (Use spacebar to select, enter to confirm):")
    options = ["Use Search Query", "Filter Playtime", "Filter Playercount", "Choose Categories"]
    selected_indices = cutie.select_multiple(options)
    print(selected_indices)
    clear()
    while True:
        filters = {}
        if 0 in selected_indices:
            query = input("Enter your search: ")
        else:
            query = None
        if 1 in selected_indices:
            filters["min_playtime"] = int(input("Enter minimum playtime: "))
            filters["max_playtime"] = int(input("Enter maximum playtime: "))
        if 2 in selected_indices:  
            filters["player_count"] = int(input("Enter player count: "))
        if 3 in selected_indices:
            categories = []
            print("Select Categories (Use space to confirm):")
            options = ["Thematic", "Strategy", "War", "Family", "CGS", "Abstract", "Party", "Childrens"]
            selected = cutie.select_multiple(options)
            if 0 in selected:
                 categories.append("Thematic")
            if 1 in selected:
                 categories.append("Strategy")
            if 2 in selected:
                 categories.append("War")
            if 3 in selected:
                 categories.append("Family")
            if 4 in selected:
                 categories.append("CGS")
            if 5 in selected:
                 categories.append("Abstract")
            if 6 in selected:
                 categories.append("Party")
            if 7 in selected:
                 categories.append("Childrens")
            clear()
            print(f"Selected: {categories}")
        else:
            categories = None

        results = search_games(query=query, filters=filters, category=categories)
        print("Search Results:")
        for game in results:
            print(game.get("Name") + " - ID:" + game.get("BGGId"))
        if not cutie.prompt_yes_or_no("Do you want to try again?"):
            break
        


def main():  
    print("Starting Boardgame Manager")
    options = ["User Management", "Recommendations", "Search", "Exit"]
    while True:
        choice = menu("Main Menu", options)
        if choice == 0:
            showcase_user_management()
        elif choice == 1:
            showcase_recommendations()
        elif choice == 2:
            showcase_search()
        elif choice == 3:
            print("Exiting Backend Showcase")
            break
            
if __name__ == "__main__":
    main()