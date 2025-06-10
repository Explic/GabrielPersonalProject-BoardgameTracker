import sys
from ui.loginpage import Ui_LoginWindow
from ui.homepage import Ui_HomeWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from src.backend.user_manager import login, signup

class LoginPage:
    def __init__(self, main_window):
        self.log = Ui_LoginWindow()
        self.log.setupUi(main_window)
        self.log.SignupButton.clicked.connect(self.click_button_signup)
        self.log.LoginButton.clicked.connect(self.click_button_login)
    
    def login_notify(self, message):
        self.log.NotifyLabel.setText(message)
        
    def click_button_signup(self):
        inputusername = self.log.UsernameInput.text()
        inputpassword = self.log.PasswordInput.text()
        outcome = signup(inputusername, inputpassword)
        print(outcome)
        if outcome == (True, 'Account created successfully.'):
            self.login_notify("Account Created, Please Log In")
        elif outcome == (False, 'Username already exists.'):
            self.login_notify("Username already exists")
        elif outcome == (False, 'Password must be at least 7 characters long.'):
            self.login_notify("Password must be at least 7 characters long")
        elif outcome == (False, 'Username cannot be empty.'):
            self.login_notify("Username cannot be empty")
        elif outcome == (False, 'Password cannot be empty.'):
            self.login_notify("Password cannot be empty")
    
    def click_button_login(self):
        inputusername = self.log.UsernameInput.text()
        inputpassword = self.log.PasswordInput.text()
        outcome = login(inputusername, inputpassword)
        if outcome == (False, "Username not found."):
            self.login_notify("Username not found")
        elif outcome == (False, "Username does not exist"):
            self.login_notify("Username does not exist")
        elif outcome == (False, 'Incorrect password.'):
            self.login_notify("Incorrect password")
        elif outcome == (True, "Login successful."):
            print("Logged in as: " + inputusername)
            #GO TO HOMEPAGE
            self.log.centralwidget.hide()  # Hide the login page
            HomePage(self.log.centralwidget.parent())  # Initialize the HomePage
            
            
class HomePage:
    def __init__(self, main_window):
        print("boothomepage")
        self.home = Ui_HomeWindow()
        self.home.setupUi(main_window)
        self.home.RecommendedButton.clicked.connect(self.click_recommendedButton)
        self.home.RecommendedView.clicked.connect(self.click_recommendedView)
        self.home.SearchButton.clicked.connect(self.click_searchButton)
        self.home.SettingsButton.clicked.connect(self.click_settingsButton)
        self.home.LogoutButton.clicked.connect(self.click_logoutButton)
        self.home.ExitButton.clicked.connect(self.click_exitButton)
        self.home.WishlistButton.clicked.connect(self.click_wishlistButton)
        
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    login_page = LoginPage(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec())