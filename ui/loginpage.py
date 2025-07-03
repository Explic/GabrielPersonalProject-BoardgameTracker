# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testloginwruCni.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"BoardgameManager-Login")
        MainWindow.resize(219, 272)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 4, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.UsernameLabel = QLabel(self.centralwidget)
        self.UsernameLabel.setObjectName(u"UsernameLabel")

        self.verticalLayout.addWidget(self.UsernameLabel)

        self.UsernameInput = QLineEdit(self.centralwidget)
        self.UsernameInput.setObjectName(u"UsernameInput")
        self.UsernameInput.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.UsernameInput)

        self.verticalSpacer = QSpacerItem(10, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.PasswordLabel = QLabel(self.centralwidget)
        self.PasswordLabel.setObjectName(u"PasswordLabel")

        self.verticalLayout.addWidget(self.PasswordLabel)

        self.PasswordInput = QLineEdit(self.centralwidget)
        self.PasswordInput.setObjectName(u"PasswordInput")
        self.PasswordInput.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.PasswordInput)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.SignupButton = QPushButton(self.centralwidget)
        self.SignupButton.setObjectName(u"SignupButton")

        self.gridLayout.addWidget(self.SignupButton, 0, 0, 1, 1)

        self.LoginButton = QPushButton(self.centralwidget)
        self.LoginButton.setObjectName(u"LoginButton")

        self.gridLayout.addWidget(self.LoginButton, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.NotifyLabel = QLabel(self.centralwidget)
        self.NotifyLabel.setObjectName(u"NotifyLabel")
        self.NotifyLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.NotifyLabel, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Board-Game Tracker</span></p></body></html>", None))
        self.UsernameLabel.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.UsernameInput.setText("")
        self.UsernameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Username", None))
        self.PasswordLabel.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.PasswordInput.setInputMask("")
        self.PasswordInput.setText("")
        self.PasswordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Password", None))
        self.SignupButton.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.NotifyLabel.setText(QCoreApplication.translate("MainWindow", u"Notify", None))
    # retranslateUi

    def on_signup_button_clicked(self):
        self.NotifyLabel.setText("sign up button clicked")
    # on_signup_button_clicked
    
    def on_login_button_clicked(self):
        username = self.UsernameInput.text()
        password = self.PasswordInput.text()
        self.NotifyLabel.setText(f"username: {username} password: {password}")
    # on_login_button_clicked
    
    def login_notify(self, message):
        self.NotifyLabel.setText(message)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(MainWindow)
    ui.SignupButton.clicked.connect(ui.on_signup_button_clicked)
    ui.LoginButton.clicked.connect(ui.on_login_button_clicked)
    MainWindow.show()
    sys.exit(app.exec())

