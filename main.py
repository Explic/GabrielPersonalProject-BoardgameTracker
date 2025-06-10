import sys
from ui.loginpage import Ui_LoginWindow
from ui.homepage import Ui_HomeWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from src.backend.user_manager import login, signup

# Global variables
MainWindow = None
logged_in_user = None

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