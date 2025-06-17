from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QWidget)

class Ui_RecommendWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(619, 738)
        MainWindow.setMinimumSize(QSize(619, 738))
        MainWindow.setMaximumSize(QSize(619, 738))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 211, 31))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 70, 361, 121))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelImage_1 = QLabel(self.frame_2)
        self.labelImage_1.setObjectName(u"labelImage_1")
        self.labelImage_1.setMinimumSize(QSize(102, 75))
        self.labelImage_1.setMaximumSize(QSize(102, 75))
        self.labelImage_1.setScaledContents(True)

        self.gridLayout.addWidget(self.labelImage_1, 1, 1, 1, 1)

        self.labelRank_1 = QLabel(self.frame_2)
        self.labelRank_1.setObjectName(u"labelRank_1")
        self.labelRank_1.setMinimumSize(QSize(103, 75))
        self.labelRank_1.setMaximumSize(QSize(103, 75))

        self.gridLayout.addWidget(self.labelRank_1, 1, 3, 1, 1)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 2, 1, 1)

        self.labelTags_1 = QLabel(self.frame_2)
        self.labelTags_1.setObjectName(u"labelTags_1")
        self.labelTags_1.setMinimumSize(QSize(102, 75))
        self.labelTags_1.setMaximumSize(QSize(102, 75))
        self.labelTags_1.setWordWrap(True)

        self.gridLayout.addWidget(self.labelTags_1, 1, 5, 1, 1)

        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 1, 4, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelName_1 = QLabel(self.frame_2)
        self.labelName_1.setObjectName(u"labelName_1")
        self.labelName_1.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout.addWidget(self.labelName_1)

        self.button_1 = QPushButton(self.frame_2)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setMinimumSize(QSize(51, 24))
        self.button_1.setMaximumSize(QSize(51, 24))

        self.horizontalLayout.addWidget(self.button_1)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 310, 361, 121))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.labelTags_3 = QLabel(self.frame_4)
        self.labelTags_3.setObjectName(u"labelTags_3")
        self.labelTags_3.setMinimumSize(QSize(102, 75))
        self.labelTags_3.setMaximumSize(QSize(102, 75))
        self.labelTags_3.setWordWrap(True)

        self.gridLayout_5.addWidget(self.labelTags_3, 1, 5, 1, 1)

        self.line_8 = QFrame(self.frame_4)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_8, 1, 4, 1, 1)

        self.labelImage_3 = QLabel(self.frame_4)
        self.labelImage_3.setObjectName(u"labelImage_3")
        self.labelImage_3.setMinimumSize(QSize(102, 75))
        self.labelImage_3.setMaximumSize(QSize(102, 75))
        self.labelImage_3.setScaledContents(True)

        self.gridLayout_5.addWidget(self.labelImage_3, 1, 1, 1, 1)

        self.line_7 = QFrame(self.frame_4)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_7, 1, 2, 1, 1)

        self.labelRank_3 = QLabel(self.frame_4)
        self.labelRank_3.setObjectName(u"labelRank_3")
        self.labelRank_3.setMinimumSize(QSize(103, 75))
        self.labelRank_3.setMaximumSize(QSize(103, 75))

        self.gridLayout_5.addWidget(self.labelRank_3, 1, 3, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.labelName_3 = QLabel(self.frame_4)
        self.labelName_3.setObjectName(u"labelName_3")
        self.labelName_3.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_9.addWidget(self.labelName_3)

        self.button_3 = QPushButton(self.frame_4)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setMinimumSize(QSize(51, 24))
        self.button_3.setMaximumSize(QSize(51, 24))

        self.horizontalLayout_9.addWidget(self.button_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 430, 361, 121))
        self.frame_5.setMinimumSize(QSize(361, 121))
        self.frame_5.setMaximumSize(QSize(361, 121))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_6)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.line_10 = QFrame(self.frame_6)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_10, 1, 2, 1, 1)

        self.labelTags_4 = QLabel(self.frame_6)
        self.labelTags_4.setObjectName(u"labelTags_4")
        self.labelTags_4.setMinimumSize(QSize(102, 75))
        self.labelTags_4.setMaximumSize(QSize(102, 75))
        self.labelTags_4.setWordWrap(True)

        self.gridLayout_7.addWidget(self.labelTags_4, 1, 5, 1, 1)

        self.labelRank_4 = QLabel(self.frame_6)
        self.labelRank_4.setObjectName(u"labelRank_4")
        self.labelRank_4.setMinimumSize(QSize(103, 75))
        self.labelRank_4.setMaximumSize(QSize(103, 75))

        self.gridLayout_7.addWidget(self.labelRank_4, 1, 3, 1, 1)

        self.labelImage_4 = QLabel(self.frame_6)
        self.labelImage_4.setObjectName(u"labelImage_4")
        self.labelImage_4.setMinimumSize(QSize(102, 75))
        self.labelImage_4.setMaximumSize(QSize(102, 75))
        self.labelImage_4.setScaledContents(True)

        self.gridLayout_7.addWidget(self.labelImage_4, 1, 1, 1, 1)

        self.line_11 = QFrame(self.frame_6)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_11, 1, 4, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_7, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.labelName_4 = QLabel(self.frame_6)
        self.labelName_4.setObjectName(u"labelName_4")
        self.labelName_4.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_10.addWidget(self.labelName_4)

        self.button_4 = QPushButton(self.frame_6)
        self.button_4.setObjectName(u"button_4")
        self.button_4.setMinimumSize(QSize(51, 24))
        self.button_4.setMaximumSize(QSize(51, 24))

        self.horizontalLayout_10.addWidget(self.button_4)


        self.gridLayout_6.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 550, 361, 121))
        self.frame_7.setMinimumSize(QSize(361, 121))
        self.frame_7.setMaximumSize(QSize(361, 121))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_8)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.line_14 = QFrame(self.frame_8)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_14, 1, 4, 1, 1)

        self.labelRank_5 = QLabel(self.frame_8)
        self.labelRank_5.setObjectName(u"labelRank_5")
        self.labelRank_5.setMinimumSize(QSize(103, 75))
        self.labelRank_5.setMaximumSize(QSize(103, 75))

        self.gridLayout_9.addWidget(self.labelRank_5, 1, 3, 1, 1)

        self.line_13 = QFrame(self.frame_8)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_13, 1, 2, 1, 1)

        self.labelImage_5 = QLabel(self.frame_8)
        self.labelImage_5.setObjectName(u"labelImage_5")
        self.labelImage_5.setMinimumSize(QSize(102, 75))
        self.labelImage_5.setMaximumSize(QSize(102, 75))
        self.labelImage_5.setScaledContents(True)

        self.gridLayout_9.addWidget(self.labelImage_5, 1, 1, 1, 1)

        self.labelTags_5 = QLabel(self.frame_8)
        self.labelTags_5.setObjectName(u"labelTags_5")
        self.labelTags_5.setMinimumSize(QSize(102, 75))
        self.labelTags_5.setMaximumSize(QSize(102, 75))
        self.labelTags_5.setWordWrap(True)

        self.gridLayout_9.addWidget(self.labelTags_5, 1, 5, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 1, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.labelName_5 = QLabel(self.frame_8)
        self.labelName_5.setObjectName(u"labelName_5")
        self.labelName_5.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_11.addWidget(self.labelName_5)

        self.button_5 = QPushButton(self.frame_8)
        self.button_5.setObjectName(u"button_5")
        self.button_5.setMinimumSize(QSize(51, 24))
        self.button_5.setMaximumSize(QSize(51, 24))

        self.horizontalLayout_11.addWidget(self.button_5)


        self.gridLayout_8.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 190, 361, 121))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_10)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.labelRank_6 = QLabel(self.frame_10)
        self.labelRank_6.setObjectName(u"labelRank_6")
        self.labelRank_6.setMinimumSize(QSize(103, 75))
        self.labelRank_6.setMaximumSize(QSize(103, 75))

        self.gridLayout_11.addWidget(self.labelRank_6, 1, 3, 1, 1)

        self.labelTags_6 = QLabel(self.frame_10)
        self.labelTags_6.setObjectName(u"labelTags_6")
        self.labelTags_6.setMinimumSize(QSize(102, 75))
        self.labelTags_6.setMaximumSize(QSize(102, 75))
        self.labelTags_6.setWordWrap(True)

        self.gridLayout_11.addWidget(self.labelTags_6, 1, 5, 1, 1)

        self.line_16 = QFrame(self.frame_10)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.VLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_16, 1, 2, 1, 1)

        self.line_17 = QFrame(self.frame_10)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.VLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_17, 1, 4, 1, 1)

        self.labelImage_6 = QLabel(self.frame_10)
        self.labelImage_6.setObjectName(u"labelImage_6")
        self.labelImage_6.setMinimumSize(QSize(102, 75))
        self.labelImage_6.setMaximumSize(QSize(102, 75))
        self.labelImage_6.setScaledContents(True)

        self.gridLayout_11.addWidget(self.labelImage_6, 1, 1, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_11, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelName_6 = QLabel(self.frame_10)
        self.labelName_6.setObjectName(u"labelName_6")
        self.labelName_6.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_3.addWidget(self.labelName_6)

        self.button_2 = QPushButton(self.frame_10)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setMinimumSize(QSize(51, 24))
        self.button_2.setMaximumSize(QSize(51, 24))

        self.horizontalLayout_3.addWidget(self.button_2)


        self.gridLayout_10.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.frame_10)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(370, 70, 241, 601))
        self.widget.setMaximumSize(QSize(241, 601))
        self.gridLayout_12 = QGridLayout(self.widget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.listRecommended = QListWidget(self.widget)
        self.listRecommended.setObjectName(u"listRecommended")
        self.listRecommended.setMinimumSize(QSize(223, 583))

        self.gridLayout_12.addWidget(self.listRecommended, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 51, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 50, 221, 21))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(19, 680, 581, 31))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(71, 24))
        self.pushButton.setMaximumSize(QSize(71, 24))

        self.horizontalLayout_8.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Recommended For You:</span></p></body></html>", None))
        self.labelImage_1.setText(QCoreApplication.translate("MainWindow", u"GameImage1", None))
        self.labelRank_1.setText(QCoreApplication.translate("MainWindow", u"GameRank1", None))
        self.labelTags_1.setText(QCoreApplication.translate("MainWindow", u"GameTags1", None))
        self.labelName_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">GameName1</span></p></body></html>", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.labelTags_3.setText(QCoreApplication.translate("MainWindow", u"GameTags3", None))
        self.labelImage_3.setText(QCoreApplication.translate("MainWindow", u"GameImage3", None))
        self.labelRank_3.setText(QCoreApplication.translate("MainWindow", u"GameRank3", None))
        self.labelName_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">GameName3</span></p></body></html>", None))
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.labelTags_4.setText(QCoreApplication.translate("MainWindow", u"GameTags4", None))
        self.labelRank_4.setText(QCoreApplication.translate("MainWindow", u"GameRank4", None))
        self.labelImage_4.setText(QCoreApplication.translate("MainWindow", u"GameImage4", None))
        self.labelName_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">GameName4</span></p></body></html>", None))
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.labelRank_5.setText(QCoreApplication.translate("MainWindow", u"GameRank5", None))
        self.labelImage_5.setText(QCoreApplication.translate("MainWindow", u"GameImage5", None))
        self.labelTags_5.setText(QCoreApplication.translate("MainWindow", u"GameTags5", None))
        self.labelName_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">GameName5</span></p></body></html>", None))
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.labelRank_6.setText(QCoreApplication.translate("MainWindow", u"GameRank2", None))
        self.labelTags_6.setText(QCoreApplication.translate("MainWindow", u"GameTags2", None))
        self.labelImage_6.setText(QCoreApplication.translate("MainWindow", u"GameImage2", None))
        self.labelName_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">GameName2</span></p></body></html>", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Top 5:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">More Recommended Games:</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

