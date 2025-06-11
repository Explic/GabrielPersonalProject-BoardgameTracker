from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QWidget)

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QWidget)

class Ui_GameWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(546, 343)
        MainWindow.setMaximumSize(QSize(828, 425))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 6, 0)
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(254, 238))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 5, 1, 1, 1)

        self.titleCatagory = QLabel(self.tab)
        self.titleCatagory.setObjectName(u"titleCatagory")

        self.gridLayout_3.addWidget(self.titleCatagory, 6, 0, 1, 1)

        self.titleRank = QLabel(self.tab)
        self.titleRank.setObjectName(u"titleRank")

        self.gridLayout_3.addWidget(self.titleRank, 0, 0, 1, 1)

        self.labelRank = QLabel(self.tab)
        self.labelRank.setObjectName(u"labelRank")

        self.gridLayout_3.addWidget(self.labelRank, 0, 2, 1, 1)

        self.line_3 = QFrame(self.tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 6, 1, 1, 1)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 4, 1, 1, 1)

        self.line_4 = QFrame(self.tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_4, 3, 1, 1, 1)

        self.labelYear = QLabel(self.tab)
        self.labelYear.setObjectName(u"labelYear")

        self.gridLayout_3.addWidget(self.labelYear, 1, 2, 1, 1)

        self.titleRating = QLabel(self.tab)
        self.titleRating.setObjectName(u"titleRating")

        self.gridLayout_3.addWidget(self.titleRating, 5, 0, 1, 1)

        self.titleYear = QLabel(self.tab)
        self.titleYear.setObjectName(u"titleYear")

        self.gridLayout_3.addWidget(self.titleYear, 1, 0, 1, 1)

        self.titlePlayer = QLabel(self.tab)
        self.titlePlayer.setObjectName(u"titlePlayer")

        self.gridLayout_3.addWidget(self.titlePlayer, 2, 0, 1, 1)

        self.line_7 = QFrame(self.tab)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_7, 0, 1, 1, 1)

        self.line_6 = QFrame(self.tab)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_6, 1, 1, 1, 1)

        self.line_5 = QFrame(self.tab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setWindowModality(Qt.NonModal)
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 2, 1, 1, 1)

        self.titlePlaytime = QLabel(self.tab)
        self.titlePlaytime.setObjectName(u"titlePlaytime")

        self.gridLayout_3.addWidget(self.titlePlaytime, 3, 0, 1, 1)

        self.titleOwner = QLabel(self.tab)
        self.titleOwner.setObjectName(u"titleOwner")

        self.gridLayout_3.addWidget(self.titleOwner, 4, 0, 1, 1)

        self.labelPlayercount = QLabel(self.tab)
        self.labelPlayercount.setObjectName(u"labelPlayercount")

        self.gridLayout_3.addWidget(self.labelPlayercount, 2, 2, 1, 1)

        self.labelPlaytime = QLabel(self.tab)
        self.labelPlaytime.setObjectName(u"labelPlaytime")

        self.gridLayout_3.addWidget(self.labelPlaytime, 3, 2, 1, 1)

        self.labelOwners = QLabel(self.tab)
        self.labelOwners.setObjectName(u"labelOwners")

        self.gridLayout_3.addWidget(self.labelOwners, 4, 2, 1, 1)

        self.labelRating = QLabel(self.tab)
        self.labelRating.setObjectName(u"labelRating")

        self.gridLayout_3.addWidget(self.labelRating, 5, 2, 1, 1)

        self.labelCatagory = QLabel(self.tab)
        self.labelCatagory.setObjectName(u"labelCatagory")

        self.gridLayout_3.addWidget(self.labelCatagory, 6, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(130, 1, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 7, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_6 = QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.titleTags = QLabel(self.tab_2)
        self.titleTags.setObjectName(u"titleTags")

        self.gridLayout_6.addWidget(self.titleTags, 4, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.titleID = QLabel(self.tab_2)
        self.titleID.setObjectName(u"titleID")

        self.gridLayout_5.addWidget(self.titleID, 0, 0, 1, 1)

        self.line_8 = QFrame(self.tab_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_8, 0, 1, 1, 1)

        self.labelID = QLabel(self.tab_2)
        self.labelID.setObjectName(u"labelID")

        self.gridLayout_5.addWidget(self.labelID, 0, 2, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 2, 0, 1, 1)

        self.line_9 = QFrame(self.tab_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_9, 3, 0, 1, 1)

        self.TagsList = QListWidget(self.tab_2)
        self.TagsList.setObjectName(u"TagsList")
        self.TagsList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.TagsList.setProperty("showDropIndicator", True)
        self.TagsList.setAlternatingRowColors(True)
        self.TagsList.setSelectionMode(QAbstractItemView.NoSelection)
        self.TagsList.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.TagsList.setProperty("isWrapping", False)

        self.gridLayout_6.addWidget(self.TagsList, 5, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_7 = QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.listSimilar = QListWidget(self.tab_3)
        self.listSimilar.setObjectName(u"listSimilar")
        self.listSimilar.setAlternatingRowColors(True)

        self.gridLayout_7.addWidget(self.listSimilar, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.widget, 1, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(250, 238))
        self.frame.setMaximumSize(QSize(250, 238))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 9, 0)
        self.labelArtist = QLabel(self.frame)
        self.labelArtist.setObjectName(u"labelArtist")

        self.gridLayout_2.addWidget(self.labelArtist, 1, 0, 1, 1)

        self.GameImage = QLabel(self.frame)
        self.GameImage.setObjectName(u"GameImage")
        self.GameImage.setMinimumSize(QSize(230, 189))
        self.GameImage.setPixmap(QPixmap(u"assets/placeholder.png"))
        self.GameImage.setScaledContents(True)

        self.gridLayout_2.addWidget(self.GameImage, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame, 1, 2, 1, 1)

        self.wishlistButton = QPushButton(self.centralwidget)
        self.wishlistButton.setObjectName(u"wishlistButton")
        self.wishlistButton.setMinimumSize(QSize(75, 24))
        self.wishlistButton.setMaximumSize(QSize(111, 24))

        self.gridLayout_8.addWidget(self.wishlistButton, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)

        self.GameName = QLabel(self.centralwidget)
        self.GameName.setObjectName(u"GameName")

        self.gridLayout_8.addWidget(self.GameName, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setMaximumSize(QSize(75, 24))

        self.horizontalLayout.addWidget(self.backButton)


        self.gridLayout_8.addLayout(self.horizontalLayout, 2, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(statustip)
        self.titleCatagory.setStatusTip(QCoreApplication.translate("MainWindow", u"The genre/type of the game, such as Strategy or Family", None))
#endif // QT_CONFIG(statustip)
        self.titleCatagory.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Catagory:</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.titleRank.setStatusTip(QCoreApplication.translate("MainWindow", u"Board Game Geek rank (Higher is better)", None))
#endif // QT_CONFIG(statustip)
        self.titleRank.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">BGG Rank:</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.labelRank.setStatusTip(QCoreApplication.translate("MainWindow", u"Board Game Geek rank (Higher is better)", None))
#endif // QT_CONFIG(statustip)
        self.labelRank.setText(QCoreApplication.translate("MainWindow", u"Rank Placeholder", None))
#if QT_CONFIG(statustip)
        self.labelYear.setStatusTip(QCoreApplication.translate("MainWindow", u"Year the board game was first published", None))
#endif // QT_CONFIG(statustip)
        self.labelYear.setText(QCoreApplication.translate("MainWindow", u"Year Placeholder", None))
#if QT_CONFIG(statustip)
        self.titleRating.setStatusTip(QCoreApplication.translate("MainWindow", u"The average rating given by users on BoardGameGeek", None))
#endif // QT_CONFIG(statustip)
        self.titleRating.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">User Rating:</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.titleYear.setStatusTip(QCoreApplication.translate("MainWindow", u"Year the board game was first published", None))
#endif // QT_CONFIG(statustip)
        self.titleYear.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Year Published:</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.titlePlayer.setStatusTip(QCoreApplication.translate("MainWindow", u"The minimum and maximum number of players recommended for this game", None))
#endif // QT_CONFIG(statustip)
        self.titlePlayer.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Playercount:</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.titlePlaytime.setStatusTip(QCoreApplication.translate("MainWindow", u"The estimated time required to play the game, in minutes", None))
#endif // QT_CONFIG(statustip)
        self.titlePlaytime.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Playtime:</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.titleOwner.setStatusTip(QCoreApplication.translate("MainWindow", u"The number of users who own this game on BoardGameGeek", None))
#endif // QT_CONFIG(statustip)
        self.titleOwner.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Owners:</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.labelPlayercount.setStatusTip(QCoreApplication.translate("MainWindow", u"The minimum and maximum number of players recommended for this game", None))
#endif // QT_CONFIG(statustip)
        self.labelPlayercount.setText(QCoreApplication.translate("MainWindow", u"PC Placeholder", None))
#if QT_CONFIG(statustip)
        self.labelPlaytime.setStatusTip(QCoreApplication.translate("MainWindow", u"The estimated time required to play the game, in minutes", None))
#endif // QT_CONFIG(statustip)
        self.labelPlaytime.setText(QCoreApplication.translate("MainWindow", u"PT Placeholder", None))
#if QT_CONFIG(statustip)
        self.labelOwners.setStatusTip(QCoreApplication.translate("MainWindow", u"The number of users who own this game on BoardGameGeek", None))
#endif // QT_CONFIG(statustip)
        self.labelOwners.setText(QCoreApplication.translate("MainWindow", u"Own Placeholder", None))
#if QT_CONFIG(statustip)
        self.labelRating.setStatusTip(QCoreApplication.translate("MainWindow", u"The average rating given by users on BoardGameGeek", None))
#endif // QT_CONFIG(statustip)
        self.labelRating.setText(QCoreApplication.translate("MainWindow", u"Rating Placeholder", None))
#if QT_CONFIG(statustip)
        self.labelCatagory.setStatusTip(QCoreApplication.translate("MainWindow", u"The genre/type of the game, such as Strategy or Family", None))
#endif // QT_CONFIG(statustip)
        self.labelCatagory.setText(QCoreApplication.translate("MainWindow", u"Cat Placeholder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Info", None))
#if QT_CONFIG(statustip)
        self.titleTags.setStatusTip(QCoreApplication.translate("MainWindow", u"Tags associated with the game, such as mechanics and themes", None))
#endif // QT_CONFIG(statustip)
        self.titleTags.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Game Tags:</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.titleID.setStatusTip(QCoreApplication.translate("MainWindow", u"The unique identifier for this game on BoardGameGeek", None))
#endif // QT_CONFIG(statustip)
        self.titleID.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">BGG GAME ID:</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.labelID.setStatusTip(QCoreApplication.translate("MainWindow", u"The unique identifier for this game on BoardGameGeek", None))
#endif // QT_CONFIG(statustip)
        self.labelID.setText(QCoreApplication.translate("MainWindow", u"ID PLACEHOLDER", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Advanced Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Similar Games", None))
#if QT_CONFIG(statustip)
        self.labelArtist.setStatusTip(QCoreApplication.translate("MainWindow", u"Artist Credits", None))
#endif // QT_CONFIG(statustip)
        self.labelArtist.setText(QCoreApplication.translate("MainWindow", u"Artist: Unknown", None))
#if QT_CONFIG(statustip)
        self.GameImage.setStatusTip(QCoreApplication.translate("MainWindow", u"Game Image", None))
#endif // QT_CONFIG(statustip)
        self.GameImage.setText("")
        self.wishlistButton.setText(QCoreApplication.translate("MainWindow", u"Add to list", None))
#if QT_CONFIG(statustip)
        self.GameName.setStatusTip(QCoreApplication.translate("MainWindow", u"Board Game Name", None))
#endif // QT_CONFIG(statustip)
        self.GameName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">GAMENAME</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.backButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Back to homescreen", None))
#endif // QT_CONFIG(statustip)
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi
