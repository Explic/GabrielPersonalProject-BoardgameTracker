import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USERS_FILE = os.path.join(BASE_DIR, "data", "users.json")

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def signup(username, password):
    users = load_users()
    if username in users:
        return False, "Username already exists."
    users[username] = {
        "password": password,
        "wishlist": []
    }
    save_users(users)
    return True, "Account created successfully."

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
