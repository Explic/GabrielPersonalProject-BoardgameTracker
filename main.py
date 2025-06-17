import sys
from ui.loginpage import Ui_LoginWindow
from ui.homepage import Ui_HomeWindow
from ui.gameviewpage import Ui_GameWindow
from ui.recommendpage import Ui_RecommendWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QAbstractScrollArea
from src.backend.user_manager import login, signup, get_wishlist, add_to_wishlist, remove_from_wishlist
from src.backend.recommend_system import recommend_games
import requests
from PySide6.QtGui import QPixmap
from src.backend.search_system import search_games, get_game
from PySide6.QtCore import Qt

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

def setup_settings_view():
    global MainWindow, logged_in_user
    MainWindow.setCentralWidget(None)

def setup_recommended_view():
    global MainWindow, logged_in_user
    MainWindow.setCentralWidget(None)
    rc_ui = Ui_RecommendWindow()
    rc_ui.setupUi(MainWindow)
    recommendations = recommend_games(get_wishlist(logged_in_user), 50)
    print(recommendations)
    # Idk how to make this more efficent
    name1, name2, name3, name4, name5 = [game['Name'] for game in recommendations[:5]]
    image1, image2, image3, image4, image5 = [game['ImagePath'] for game in recommendations[:5]]
    rank1, rank2 , rank3, rank4, rank5 = [game['Rank:boardgame'] for game in recommendations[:5]]
    id1, id2 , id3, id4, id5 = [game['BGGId'] for game in recommendations[:5]]
    tag1 = [key.replace("Cat:", "") for key, value in recommendations[0].items() if key.startswith("Cat:") and value == '1']
    tag2 = [key.replace("Cat:", "") for key, value in recommendations[1].items() if key.startswith("Cat:") and value == '1']
    tag3 = [key.replace("Cat:", "") for key, value in recommendations[2].items() if key.startswith("Cat:") and value == '1']
    tag4 = [key.replace("Cat:", "") for key, value in recommendations[3].items() if key.startswith("Cat:") and value == '1']
    tag5 = [key.replace("Cat:", "") for key, value in recommendations[4].items() if key.startswith("Cat:") and value == '1']
    # There has to be a better way of doing this haha
    rc_ui.labelName_1.setText(u"<html><head/><body><p><span style=\" font-weight:700;\">"+name1+"</span></p></body></html>")
    rc_ui.labelImage_1.setPixmap(QPixmap(load_image(image1, id1)))
    rc_ui.labelRank_1.setText("Rank: "+rank1)
    rc_ui.labelTags_1.setText(", ".join(tag1))
    
    rc_ui.labelName_6.setText(u"<html><head/><body><p><span style=\" font-weight:700;\">"+name2+"</span></p></body></html>")
    rc_ui.labelImage_6.setPixmap(QPixmap(load_image(image2, id2)))
    rc_ui.labelRank_6.setText("Rank: "+rank2)
    rc_ui.labelTags_6.setText(", ".join(tag2))

    rc_ui.labelName_3.setText(u"<html><head/><body><p><span style=\" font-weight:700;\">"+name3+"</span></p></body></html>")
    rc_ui.labelImage_3.setPixmap(QPixmap(load_image(image3, id3)))
    rc_ui.labelRank_3.setText("Rank: "+rank3)
    rc_ui.labelTags_3.setText(", ".join(tag3))

    rc_ui.labelName_4.setText(u"<html><head/><body><p><span style=\" font-weight:700;\">"+name4+"</span></p></body></html>")
    rc_ui.labelImage_4.setPixmap(QPixmap(load_image(image4, id4)))
    rc_ui.labelRank_4.setText("Rank: "+rank4)
    rc_ui.labelTags_4.setText(", ".join(tag4))

    rc_ui.labelName_5.setText(u"<html><head/><body><p><span style=\" font-weight:700;\">"+name5+"</span></p></body></html>")
    rc_ui.labelImage_5.setPixmap(QPixmap(load_image(image5, id5)))
    rc_ui.labelRank_5.setText("Rank: "+rank5)
    rc_ui.labelTags_5.setText(", ".join(tag5))
    
    # List
    for game in recommendations[5:]:
        item = QListWidgetItem(game["Name"])
        rc_ui.listRecommended.addItem(item)
    
    def game_clicked(id):
        print("game_clicked")
        setup_game_view(id)
        
    def back_clicked():
        print("back_clicked")
        setup_homepage()   
        
    def click_list():
        print(f"game clicked: {item.text()}")
        game_details = search_games(query=item.text(), limit=1)
        if game_details:
            game_id = game_details[0]["BGGId"]
            print(game_id)
            setup_game_view(game_id)
    
    # Buttons
    rc_ui.button_1.clicked.connect(lambda: game_clicked(id1))
    rc_ui.button_2.clicked.connect(lambda: game_clicked(id2))
    rc_ui.button_3.clicked.connect(lambda: game_clicked(id3))
    rc_ui.button_4.clicked.connect(lambda: game_clicked(id4))
    rc_ui.button_5.clicked.connect(lambda: game_clicked(id5))
    rc_ui.pushButton.clicked.connect(back_clicked)
    rc_ui.listRecommended.clicked.connect(click_list)
    
def setup_game_view(game_id):
    global MainWindow, logged_in_user
    MainWindow.setCentralWidget(None)
    gv_ui = Ui_GameWindow()
    gv_ui.setupUi(MainWindow)
    gameinfo = get_game(game_id, "Name, Rank, Year, Playercount, Playtime, Owners, Rating, Image, Artist, Tags")
    catagory = [key.replace("Cat:", "") for key, value in get_game(game_id, "full").items() if key.startswith("Cat:") and value == '1']
    catagory_text = ", ".join(catagory) if catagory else "No Catagories Found"
    imagedir = load_image(gameinfo["Image"], game_id)
    
    # Updating Text / Images
    gv_ui.GameImage.setPixmap(QPixmap("ui/assets/placeholder.png"))
    if game_id in get_wishlist(logged_in_user):
        gv_ui.wishlistButton.setText("Remove from list")
    else:
        gv_ui.wishlistButton.setText("Add to list")
    gv_ui.GameName.setText(u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">"+gameinfo["Name"]+"</span></p></body></html>")
    gv_ui.labelRank.setText(gameinfo["Rank"])
    gv_ui.labelYear.setText(gameinfo["Year"])
    if gameinfo["MinPlayer"] == gameinfo["MaxPlayer"]:
        try:
            if int(gameinfo["MinPlayer"]) == 1:
                gv_ui.labelPlayercount.setText("Singleplayer")
            else:
                gv_ui.labelPlayercount.setText(gameinfo["MinPlayer"]+" Players")
        except:
            gv_ui.labelPlayercount.setText(gameinfo["MinPlayer"])
    else:
        gv_ui.labelPlayercount.setText(gameinfo["MinPlayer"]+"-"+gameinfo["MaxPlayer"]+" Players")
    gv_ui.labelPlaytime.setText(gameinfo["Playtime"]+" minutes")
    gv_ui.labelOwners.setText(gameinfo["Owners"])
    gv_ui.labelRating.setText(f"{gameinfo['Rating']}/10")
    gv_ui.labelCatagory.setText(catagory_text)
    if gameinfo["Artists"] == '':
        artists = "Unknown"
    else:
        artists = gameinfo["Artists"]
    gv_ui.labelArtist.setText("Artists: " + artists)
    gv_ui.labelArtist.setWordWrap(True)
    gv_ui.labelArtist.setStatusTip("Artists: " + artists)
    gv_ui.labelID.setText(game_id)
    gv_ui.GameImage.setPixmap(QPixmap(imagedir))
    for tag in gameinfo["Tags"]:
        item = QListWidgetItem(tag)
        gv_ui.TagsList.addItem(item)
    suggestions = recommend_games([game_id], 20)
    for game in suggestions:
        item = QListWidgetItem(game["Name"])
        gv_ui.listSimilar.addItem(item)
    
    
    # Button presses
    def click_wishlist_button():
        if game_id in get_wishlist(logged_in_user):
            print("Removing From wishlist")
            gv_ui.wishlistButton.setText("Add to list")
            remove_from_wishlist(logged_in_user, game_id)
        else:
            add_to_wishlist(logged_in_user, game_id)
            print("Adding To Wishlist")
            gv_ui.wishlistButton.setText("Remove from list")
            add_to_wishlist(logged_in_user, game_id)
            
    def click_back_button():
        print("Returning To Home")
        setup_homepage()
    
    def click_suggested(index):
        item_text = index.data()
        print(f"Suggested game clicked: {item_text}")
        # Example: Fetch game details based on the clicked game's name
        game_details = search_games(query=item_text, limit=1)
        if game_details:
            game_id = game_details[0]["BGGId"]
            print(game_id)
            setup_game_view(game_id)
            
    
    # Clickable setup
    gv_ui.wishlistButton.clicked.connect(click_wishlist_button)
    gv_ui.backButton.clicked.connect(click_back_button)
    gv_ui.listSimilar.clicked.connect(click_suggested)
    

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
    if get_wishlist(logged_in_user) == []:
        suggested = recommend_games(["291457"], 1)
        print(suggested)
        suggested_id = suggested[0]['BGGId']
        nowishlist = True
    else:
        suggested = recommend_games(get_wishlist(logged_in_user), 1)
        print(get_wishlist(logged_in_user))
        print(suggested)
        suggested_id = suggested[0]['BGGId']
        nowishlist = False
    home_ui.RecommendedGameName.setText(u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">"+suggested[0]['Name']+"</span></p></body></html>")
    # Extract tags where the value is 1
    tags = [key.replace("Cat:", "") for key, value in suggested[0].items() if key.startswith("Cat:") and value == '1']
    tags_text = ", ".join(tags) if tags else "No tags available"
    home_ui.RecommendedGameTags.setText(tags_text)
    image_url = suggested[0]['ImagePath']
    image_path = load_image(image_url, suggested_id)
    home_ui.GameImage.setPixmap(QPixmap(image_path))
    home_ui.WishlistButton.setText("My List")
    if nowishlist == True:
        home_ui.RecommendedGameName.setText("Gloomhaven\nNOTE: No games in list\nList games for suggestions")
    home_ui.BoardgameList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    home_ui.BoardgameList_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    
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
        if get_wishlist(logged_in_user) == None:
            home_ui.RecommendedButton.setText("Need listed games")
        else:
            print("Recommended view")
            setup_recommended_view()
            
            
    def click_recommended_view():
        print("Recommended View clicked")
        print(suggested_id)
        setup_game_view(suggested_id)

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
            home_ui.WishlistButton.setText("List is empty!")
        else:
            print("Wishlist menu")

    def on_top_game_clicked(item):
        print(f"Top-rated game clicked: {item.text()}")
        # Example: Fetch game details based on the clicked game's name
        game_details = search_games(query=item.text(), limit=1)
        if game_details:
            game_id = game_details[0]["BGGId"]
            print(game_id)
            setup_game_view(game_id)
            

    # Buttons for list
    home_ui.BoardgameList_2.itemClicked.connect(on_top_game_clicked)
    home_ui.BoardgameList.itemClicked.connect(on_top_game_clicked)

    # Connect buttons to functions
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