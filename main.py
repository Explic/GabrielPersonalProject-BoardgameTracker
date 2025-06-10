import sys
from ui.loginpage import Ui_LoginWindow
from ui.homepage import Ui_HomeWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from src.backend.user_manager import login, signup, get_wishlist
from src.backend.recommend_system import recommend_games
import requests
from PySide6.QtGui import QPixmap
from src.backend.search_system import search_games

# Global variables
MainWindow = None
logged_in_user = None

def load_image(image_url, suggested_id):
    # Define image_path at the start
    image_path = f"ui/assets/cachedimages/{suggested_id}.png"
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(image_path, 'wb') as file:
                file.write(response.content)
        else:
            print(f"Failed to download image: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image: {e}")
        image_path = "ui/assets/placeholder.png"  # Fallback to placeholder
    return image_path

def setup_login_page():
    global MainWindow
    login_ui = Ui_LoginWindow()
    login_ui.setupUi(MainWindow)

    def login_notify(message):
        login_ui.NotifyLabel.setText(message)

    def click_button_signup():
        inputusername = login_ui.UsernameInput.text()
        inputpassword = login_ui.PasswordInput.text()
        outcome = signup(inputusername, inputpassword)
        print(outcome)
        if outcome == (True, 'Account created successfully.'):
            login_notify("Account Created, Please Log In")
        elif outcome == (False, 'Username already exists.'):
            login_notify("Username already exists")
        elif outcome == (False, 'Password must be at least 7 characters long.'):
            login_notify("Password must be at least 7 characters long")
        elif outcome == (False, 'Username cannot be empty.'):
            login_notify("Username cannot be empty")
        elif outcome == (False, 'Password cannot be empty.'):
            login_notify("Password cannot be empty")

    def click_button_login():
        global logged_in_user
        inputusername = login_ui.UsernameInput.text()
        inputpassword = login_ui.PasswordInput.text()
        outcome = login(inputusername, inputpassword)
        if outcome == (False, "Username not found."):
            login_notify("Username not found")
        elif outcome == (False, "Username does not exist"):
            login_notify("Username does not exist")
        elif outcome == (False, 'Incorrect password.'):
            login_notify("Incorrect password")
        elif outcome == (True, "Login successful."):
            print("Logged in as: " + inputusername)
            logged_in_user = inputusername
            setup_homepage()

    login_ui.SignupButton.clicked.connect(click_button_signup)
    login_ui.LoginButton.clicked.connect(click_button_login)

def setup_homepage():
    global MainWindow, logged_in_user
    MainWindow.setCentralWidget(None)  # Clear the previous UI
    home_ui = Ui_HomeWindow()
    home_ui.setupUi(MainWindow)
    home_ui.WelcomeText.setText(u"<html><head/><body><p><span style=\" font-size:18pt;\">Welcome "+logged_in_user+"!</span></p></body></html>")
    
    # Suggested homepage game widget
    if get_wishlist(logged_in_user) == None:
        suggested = recommend_games(["174430"], 1)
    else:
        suggested = recommend_games(get_wishlist(logged_in_user), 1)
        print(get_wishlist(logged_in_user))
        print(suggested)
    suggested_id = suggested[0]['BGGId']
    home_ui.RecommendedGameName.setText(u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">"+suggested[0]['Name']+"</span></p></body></html>")
    # Extract tags where the value is 1
    tags = [key.replace("Cat:", "") for key, value in suggested[0].items() if key.startswith("Cat:") and value == '1']
    tags_text = ", ".join(tags) if tags else "No tags available"
    home_ui.RecommendedGameTags.setText(tags_text)
    image_url = suggested[0]['ImagePath']
    image_path = load_image(image_url, suggested_id)
    home_ui.GameImage.setPixmap(QPixmap(image_path))
    
    # Top 10 games homescreen
    popular_games = search_games(sort_by="owners", limit=10)
    for game in popular_games:
        item = QListWidgetItem(game["Name"])
        home_ui.BoardgameList.addItem(item)
    rank_games = search_games(sort_by="rank", limit=10)
    for game in rank_games:
        item = QListWidgetItem(game["Name"])
        home_ui.BoardgameList_2.addItem(item)
    
    # when button clicked
    def click_recommended_button():
        print("Recommended Button clicked")

    def click_recommended_view():
        print("Recommended View clicked")

    def click_search_button():
        print("Search Button clicked")

    def click_settings_button():
        print("Settings Button clicked")

    def click_logout_button():
        print("Logout Button clicked")
        setup_login_page()  # Return to login page

    def click_exit_button():
        print("Exit Button clicked")
        sys.exit()

    def click_wishlist_button():
        print("Wishlist Button clicked")
        if get_wishlist(logged_in_user) == None:
            home_ui.WishlistButton.setText("No Wishlisted Games")
        else:
            print("Wishlist menu")

    # Connect buttons to func
    home_ui.RecommendedButton.clicked.connect(click_recommended_button)
    home_ui.RecommendedView.clicked.connect(click_recommended_view)
    home_ui.SearchButton.clicked.connect(click_search_button)
    home_ui.SettingsButton.clicked.connect(click_settings_button)
    home_ui.LogoutButton.clicked.connect(click_logout_button)
    home_ui.ExitButton.clicked.connect(click_exit_button)
    home_ui.WishlistButton.clicked.connect(click_wishlist_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    setup_login_page()
    MainWindow.show()
    sys.exit(app.exec())