import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USERS_FILE = os.path.join(BASE_DIR, "data", "users.json")

# ---- User Management ----
# Loads the user json
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

# Saves the user json
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Signup
def signup(username, password):
    users = load_users()
    # Checking for valid user / pass
    if username in users:
        return False, "Username already exists."
    if username is None or username == "":
        return False, "Username cannot be empty."
    if password is None or password == "":
        return False, "Password cannot be empty."
    if len(password) < 7:
        return False, "Password must be at least 7 characters long."
    users[username] = {
        "password": password,
        "wishlist": []
    }
    save_users(users)
    return True, "Account created successfully."

# Login
def login(username, password):
    users = load_users()
    if username not in users:
        return False, "Username not found."
    if users[username]["password"] != password:
        return False, "Incorrect password."
    return True, "Login successful."

def signout(username):
    users = load_users()
    if username not in users:
        return False, "Username not found."
    return True, "Logged out successfully."

# ---- Wishlist Management ----
def get_wishlist(username):
    users = load_users()
    if username not in users:
        return None, "Username not found."
    return users[username]["wishlist"], "Wishlist retrieved successfully."

def add_to_wishlist(username, game_id):
    users = load_users()
    if username not in users:
        return False, "Username not found."
    if game_id in users[username]["wishlist"]:
        return False, "Game already in wishlist."
    if game_id is None or game_id == "":
        return False, "Invalid game ID."
    users[username]["wishlist"].append(game_id)
    save_users(users)
    return True, "Game added to wishlist successfully."

def remove_from_wishlist(username, game_id):
    users = load_users()
    if username not in users:
        return False, "Username not found."
    if game_id not in users[username]["wishlist"]:
        return False, "Game not found in wishlist."
    users[username]["wishlist"].remove(game_id)
    save_users(users)
    return True, "Game removed from wishlist successfully."

def remove_user(username):
    users = load_users()
    if username not in users:
        return False, "Username not found."
    del users[username]
    save_users(users)
    return True, "User removed successfully."

# --- Testing user manager ---
if __name__ == "__main__":
    print("Testing User Management System:")
    print(signup("testuser", "password123")) # Should succeed
    print(login("testuser", "password123")) # Should succeed
    print(add_to_wishlist("testuser", "12345")) # Should succeed
    print(get_wishlist("testuser")) # Should contain "12345"
    print(remove_from_wishlist("testuser", "12345")) # Should succeed
    print(get_wishlist("testuser")) # Should be empty now
    print(signout("testuser")) # Should succeed
    print(login("testuser", "wrongpassword"))  # Should fail
    print(login("nouser", "password123"))  # Should fail
    print(signup("testuser", "short"))  # Should fail due to short password
    print(remove_user("testuser"))  # Should succeed
    print(get_wishlist("testuser"))  # Should fail since user is removed
    print(remove_user("nouser"))  # Should fail since user does not exist
    print("User Management System tests completed.")