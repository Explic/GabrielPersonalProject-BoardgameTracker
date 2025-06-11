from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QWidget)

class Ui_HomeWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(509, 410)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_9 = QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_2)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 290))
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.DatabaseTitle = QLabel(self.widget_2)
        self.DatabaseTitle.setObjectName(u"DatabaseTitle")

        self.horizontalLayout_3.addWidget(self.DatabaseTitle)

        self.SearchButton = QPushButton(self.widget_2)
        self.SearchButton.setObjectName(u"SearchButton")
        self.SearchButton.setMaximumSize(QSize(51, 16777215))

        self.horizontalLayout_3.addWidget(self.SearchButton)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.BoardgameLists = QTabWidget(self.widget_2)
        self.BoardgameLists.setObjectName(u"BoardgameLists")
        self.PopularGamesTab = QWidget()
        self.PopularGamesTab.setObjectName(u"PopularGamesTab")
        self.gridLayout = QGridLayout(self.PopularGamesTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.BoardgameList = QListWidget(self.PopularGamesTab)
        self.BoardgameList.setObjectName(u"BoardgameList")
        self.BoardgameList.setFrameShape(QFrame.StyledPanel)
        self.BoardgameList.setFrameShadow(QFrame.Sunken)
        self.BoardgameList.setMidLineWidth(0)
        self.BoardgameList.setTabKeyNavigation(False)
        self.BoardgameList.setProperty("isWrapping", False)
        self.BoardgameList.setLayoutMode(QListView.SinglePass)
        self.BoardgameList.setViewMode(QListView.ListMode)
        self.BoardgameList.setUniformItemSizes(False)
        self.BoardgameList.setWordWrap(False)
        self.BoardgameList.setSelectionRectVisible(True)
        self.BoardgameList.setSortingEnabled(False)

        self.gridLayout.addWidget(self.BoardgameList, 0, 0, 1, 1)

        self.BoardgameLists.addTab(self.PopularGamesTab, "")
        self.TopRatedGamesTab = QWidget()
        self.TopRatedGamesTab.setObjectName(u"TopRatedGamesTab")
        self.gridLayout_2 = QGridLayout(self.TopRatedGamesTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.BoardgameList_2 = QListWidget(self.TopRatedGamesTab)
        self.BoardgameList_2.setObjectName(u"BoardgameList_2")
        self.BoardgameList_2.setFrameShape(QFrame.StyledPanel)
        self.BoardgameList_2.setFrameShadow(QFrame.Sunken)
        self.BoardgameList_2.setMidLineWidth(0)
        self.BoardgameList_2.setTabKeyNavigation(False)
        self.BoardgameList_2.setProperty("isWrapping", False)
        self.BoardgameList_2.setLayoutMode(QListView.SinglePass)
        self.BoardgameList_2.setViewMode(QListView.ListMode)
        self.BoardgameList_2.setUniformItemSizes(False)
        self.BoardgameList_2.setWordWrap(False)
        self.BoardgameList_2.setSelectionRectVisible(True)
        self.BoardgameList_2.setSortingEnabled(False)

        self.gridLayout_2.addWidget(self.BoardgameList_2, 0, 0, 1, 1)

        self.BoardgameLists.addTab(self.TopRatedGamesTab, "")

        self.gridLayout_3.addWidget(self.BoardgameLists, 2, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.widget_2, 1, 1, 1, 2)

        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.RecommendedGameName = QLabel(self.widget)
        self.RecommendedGameName.setObjectName(u"RecommendedGameName")

        self.gridLayout_4.addWidget(self.RecommendedGameName, 1, 0, 1, 1)

        self.RecommendedGameTags = QLabel(self.widget)
        self.RecommendedGameTags.setObjectName(u"RecommendedGameTags")

        self.gridLayout_4.addWidget(self.RecommendedGameTags, 4, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.GameImage = QLabel(self.widget)
        self.GameImage.setObjectName(u"GameImage")
        self.GameImage.setMinimumSize(QSize(221, 157))
        self.GameImage.setMaximumSize(QSize(221, 157))
        self.GameImage.setPixmap(QPixmap(u"assets/placeholder.png"))
        self.GameImage.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.GameImage)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 31))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.RecommendedView = QPushButton(self.frame)
        self.RecommendedView.setObjectName(u"RecommendedView")
        self.RecommendedView.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_5.addWidget(self.RecommendedView)

        self.RecommendedButton = QPushButton(self.frame)
        self.RecommendedButton.setObjectName(u"RecommendedButton")
        self.RecommendedButton.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_5.addWidget(self.RecommendedButton)


        self.gridLayout_7.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.widget, 1, 0, 1, 1)

        self.SettingsButton = QPushButton(self.frame_2)
        self.SettingsButton.setObjectName(u"SettingsButton")
        self.SettingsButton.setMaximumSize(QSize(75, 24))

        self.gridLayout_8.addWidget(self.SettingsButton, 2, 0, 1, 1)

        self.WelcomeText = QLabel(self.frame_2)
        self.WelcomeText.setObjectName(u"WelcomeText")

        self.gridLayout_8.addWidget(self.WelcomeText, 0, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.LogoutButton = QPushButton(self.frame_2)
        self.LogoutButton.setObjectName(u"LogoutButton")
        self.LogoutButton.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.LogoutButton)

        self.ExitButton = QPushButton(self.frame_2)
        self.ExitButton.setObjectName(u"ExitButton")
        self.ExitButton.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.ExitButton)


        self.gridLayout_8.addLayout(self.horizontalLayout, 2, 2, 1, 1)

        self.WishlistButton = QPushButton(self.frame_2)
        self.WishlistButton.setObjectName(u"WishlistButton")

        self.gridLayout_8.addWidget(self.WishlistButton, 0, 2, 1, 1)


        self.gridLayout_9.addWidget(self.frame_2, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.BoardgameLists.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.DatabaseTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Boardgames Database</span></p></body></html>", None))
        self.SearchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.BoardgameLists.setTabText(self.BoardgameLists.indexOf(self.PopularGamesTab), QCoreApplication.translate("MainWindow", u"Popular", None))
        self.BoardgameLists.setTabText(self.BoardgameLists.indexOf(self.TopRatedGamesTab), QCoreApplication.translate("MainWindow", u"Top Rated", None))
        self.RecommendedGameName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">GAMENAME</span></p></body></html>", None))
        self.RecommendedGameTags.setText(QCoreApplication.translate("MainWindow", u"TAGS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Next Game to Play:</p></body></html>", None))
        self.GameImage.setText("")
        self.RecommendedView.setText(QCoreApplication.translate("MainWindow", u"View Game", None))
        self.RecommendedButton.setText(QCoreApplication.translate("MainWindow", u"Recommendations", None))
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.WelcomeText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Welcome [USERNAME]!</span></p></body></html>", None))
        self.LogoutButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.ExitButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.WishlistButton.setText(QCoreApplication.translate("MainWindow", u"My Wishlist", None))
    # retranslateUi

