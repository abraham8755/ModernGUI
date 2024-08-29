# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacePrLMwp.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QScrollBar, QSizePolicy, QSpacerItem, QToolButton,
    QTreeView, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1155, 725)
        MainWindow.setStyleSheet(u"*{\n"
"	border : none;\n"
"	background-color: transparent;\n"
"	backgorund: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"#leftMenuSubContainer{\n"
"	background-color: #16191d;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10 px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer, #rightMenuSubContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"#frame_4, #frame_8, #popupNotificaitionContainer{\n"
"	background-color:  #16191d;\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"QScrollBar:horizontal, QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2c313c;\n"
"    height: 8px;  /* Daha ince yapmak i\u00e7in y\u00fcksekli\u011fi azalt\u0131yoruz */\n"
"    width: 8px;   /* Daha ince yapmak i\u00e7in geni\u015fli\u011fi azalt\u0131yoruz */\n"
"    margin: 0px 0px 0px 0px"
                        ";\n"
"    border-radius: 4px;  /* Daha ince scrollbarlar i\u00e7in k\u00f6\u015fe yuvarlatmalar\u0131n\u0131 da azalt\u0131yoruz */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal, QScrollBar::handle:vertical {\n"
"    background: rgba(255, 255, 255, 0.5);\n"
"    min-width: 20px;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover, QScrollBar::handle:vertical:hover {\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #d0d0d0;\n"
"}\n"
""
                        "QPushButton:pressed {\n"
"    background-color: #f0f0f0; /* Temel renk ile ayn\u0131 */\n"
"}\n"
"QToolButton {\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: #d0d0d0;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: #f0f0f0; /* Temel renk ile ayn\u0131 */\n"
"}\n"
"")
        self.actionsa = QAction(MainWindow)
        self.actionsa.setObjectName(u"actionsa")
        icon = QIcon()
        icon.addFile(u":/icons/icons/bell-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionsa.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        font = QFont()
        font.setPointSize(9)
        self.menuBtn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon1)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.homeBtn.setFont(font1)
        self.homeBtn.setStyleSheet(u"background-color: #1f232a;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon2)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.dataBtn = QPushButton(self.frame_2)
        self.dataBtn.setObjectName(u"dataBtn")
        self.dataBtn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dataBtn.setIcon(icon3)
        self.dataBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.dataBtn)

        self.fileBtn = QPushButton(self.frame_2)
        self.fileBtn.setObjectName(u"fileBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fileBtn.setIcon(icon4)
        self.fileBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.fileBtn)

        self.toolsBtn = QPushButton(self.frame_2)
        self.toolsBtn.setObjectName(u"toolsBtn")
        self.toolsBtn.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolsBtn.setIcon(icon5)
        self.toolsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.toolsBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        font2 = QFont()
        font2.setBold(True)
        self.settingsBtn.setFont(font2)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon6)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon7)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon8)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon9)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomQStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.centerMenuPages.setMinimumSize(QSize(200, 0))
        self.filePage = QWidget()
        self.filePage.setObjectName(u"filePage")
        self.verticalLayout_24 = QVBoxLayout(self.filePage)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_16 = QFrame(self.filePage)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.fileBtn_2 = QToolButton(self.frame_16)
        self.fileBtn_2.setObjectName(u"fileBtn_2")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fileBtn_2.setIcon(icon10)
        self.fileBtn_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_14.addWidget(self.fileBtn_2)

        self.folderBtn = QToolButton(self.frame_16)
        self.folderBtn.setObjectName(u"folderBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/folder-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.folderBtn.setIcon(icon11)
        self.folderBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_14.addWidget(self.folderBtn)

        self.saveBtn = QToolButton(self.frame_16)
        self.saveBtn.setObjectName(u"saveBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveBtn.setIcon(icon12)
        self.saveBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_14.addWidget(self.saveBtn)


        self.verticalLayout_24.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.filePage)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout_24.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.filePage)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.verticalLayout_24.addWidget(self.frame_18)

        self.centerMenuPages.addWidget(self.filePage)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.centerMenuPages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.centerMenuPages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.centerMenuPages.addWidget(self.page_3)

        self.verticalLayout_6.addWidget(self.centerMenuPages)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u":/images/images/lung2.jpg"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.label_6.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_6)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon13)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.frame_6)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon14)
        self.moreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.moreMenuBtn)

        self.profileMenuBtn = QPushButton(self.frame_6)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon15)
        self.profileMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.profileMenuBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon16)
        self.minimizeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon17)
        self.restoreBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon18)
        self.closeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.mainBodyContent.setMinimumSize(QSize(883, 556))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.mainContentsContainer)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_15)

        self.pagesPrevBtn = QPushButton(self.frame_14)
        self.pagesPrevBtn.setObjectName(u"pagesPrevBtn")
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pagesPrevBtn.setIcon(icon19)
        self.pagesPrevBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_15.addWidget(self.pagesPrevBtn)

        self.pagesNextBtn = QPushButton(self.frame_14)
        self.pagesNextBtn.setObjectName(u"pagesNextBtn")
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pagesNextBtn.setIcon(icon20)
        self.pagesNextBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_15.addWidget(self.pagesNextBtn)


        self.horizontalLayout_11.addWidget(self.frame_14)


        self.verticalLayout_15.addWidget(self.frame_11)

        self.mainPages = QCustomQStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_13 = QHBoxLayout(self.page_6)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.altFrame = QFrame(self.page_6)
        self.altFrame.setObjectName(u"altFrame")
        self.altFrame.setFrameShape(QFrame.StyledPanel)
        self.altFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.altFrame)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 7, 0)
        self.altLabel = QLabel(self.altFrame)
        self.altLabel.setObjectName(u"altLabel")

        self.verticalLayout_22.addWidget(self.altLabel)


        self.horizontalLayout_13.addWidget(self.altFrame)

        self.frame_10 = QFrame(self.page_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_10)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(7, 0, 0, 0)
        self.sagFrame = QFrame(self.frame_10)
        self.sagFrame.setObjectName(u"sagFrame")
        self.sagFrame.setFrameShape(QFrame.StyledPanel)
        self.sagFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.sagFrame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 10)
        self.sagLabel = QLabel(self.sagFrame)
        self.sagLabel.setObjectName(u"sagLabel")

        self.verticalLayout_13.addWidget(self.sagLabel)


        self.verticalLayout_16.addWidget(self.sagFrame)

        self.solFrame = QFrame(self.frame_10)
        self.solFrame.setObjectName(u"solFrame")
        self.solFrame.setFrameShape(QFrame.StyledPanel)
        self.solFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.solFrame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 10, 0, 0)
        self.solLabel = QLabel(self.solFrame)
        self.solLabel.setObjectName(u"solLabel")

        self.verticalLayout_14.addWidget(self.solLabel)


        self.verticalLayout_16.addWidget(self.solFrame)


        self.horizontalLayout_13.addWidget(self.frame_10)

        self.mainPages.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_17 = QVBoxLayout(self.page_7)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.altLabel_2 = QLabel(self.page_7)
        self.altLabel_2.setObjectName(u"altLabel_2")
        self.altLabel_2.setFont(font3)
        self.altLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.altLabel_2)

        self.mainPages.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_18 = QVBoxLayout(self.page_8)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.sagLabel_2 = QLabel(self.page_8)
        self.sagLabel_2.setObjectName(u"sagLabel_2")
        self.sagLabel_2.setFont(font3)
        self.sagLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.sagLabel_2)

        self.mainPages.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_25 = QVBoxLayout(self.page_9)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.solLabel_2 = QLabel(self.page_9)
        self.solLabel_2.setObjectName(u"solLabel_2")
        self.solLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.solLabel_2)

        self.mainPages.addWidget(self.page_9)

        self.verticalLayout_15.addWidget(self.mainPages)

        self.mainScrollContainer = QFrame(self.mainContentsContainer)
        self.mainScrollContainer.setObjectName(u"mainScrollContainer")
        self.mainScrollContainer.setFrameShape(QFrame.StyledPanel)
        self.mainScrollContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.mainScrollContainer)
        self.verticalLayout_23.setSpacing(6)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(9, 9, 9, 9)
        self.horizontalScrollBar = QScrollBar(self.mainScrollContainer)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setLayoutDirection(Qt.LeftToRight)
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.verticalLayout_23.addWidget(self.horizontalScrollBar)

        self.label_8 = QLabel(self.mainScrollContainer)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_8)


        self.verticalLayout_15.addWidget(self.mainScrollContainer)


        self.horizontalLayout_8.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuContainer.setMaximumSize(QSize(200, 538))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon9)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.rightMenuPages = QCustomQStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_12 = QHBoxLayout(self.page_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fileTreeView = QTreeView(self.page_4)
        self.fileTreeView.setObjectName(u"fileTreeView")

        self.horizontalLayout_12.addWidget(self.fileTreeView)

        self.rightMenuPages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout = QGridLayout(self.page_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.panBtn = QToolButton(self.page_5)
        self.panBtn.setObjectName(u"panBtn")
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/move.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.panBtn.setIcon(icon21)
        self.panBtn.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.panBtn, 2, 0, 1, 1)

        self.playBtn = QToolButton(self.page_5)
        self.playBtn.setObjectName(u"playBtn")
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons/play-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playBtn.setIcon(icon22)
        self.playBtn.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.playBtn, 1, 0, 1, 1)

        self.resetBtn = QToolButton(self.page_5)
        self.resetBtn.setObjectName(u"resetBtn")
        icon23 = QIcon()
        icon23.addFile(u":/icons/icons/refresh-ccw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resetBtn.setIcon(icon23)
        self.resetBtn.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.resetBtn, 0, 4, 1, 1)

        self.prevBtn = QToolButton(self.page_5)
        self.prevBtn.setObjectName(u"prevBtn")
        self.prevBtn.setIcon(icon19)
        self.prevBtn.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.prevBtn, 0, 0, 1, 1)

        self.zoomOutBtn = QToolButton(self.page_5)
        self.zoomOutBtn.setObjectName(u"zoomOutBtn")
        icon24 = QIcon()
        icon24.addFile(u":/icons/icons/zoom-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.zoomOutBtn.setIcon(icon24)
        self.zoomOutBtn.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.zoomOutBtn, 2, 4, 1, 1)

        self.pauseBtn = QToolButton(self.page_5)
        self.pauseBtn.setObjectName(u"pauseBtn")
        icon25 = QIcon()
        icon25.addFile(u":/icons/icons/pause-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pauseBtn.setIcon(icon25)
        self.pauseBtn.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pauseBtn, 1, 3, 1, 1)

        self.zoomInBtn = QToolButton(self.page_5)
        self.zoomInBtn.setObjectName(u"zoomInBtn")
        icon26 = QIcon()
        icon26.addFile(u":/icons/icons/zoom-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.zoomInBtn.setIcon(icon26)
        self.zoomInBtn.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.zoomInBtn, 2, 3, 1, 1)

        self.nextBtn = QToolButton(self.page_5)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setIcon(icon20)
        self.nextBtn.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.nextBtn, 0, 3, 1, 1)

        self.penBtn = QToolButton(self.page_5)
        self.penBtn.setObjectName(u"penBtn")
        icon27 = QIcon()
        icon27.addFile(u":/icons/icons/pen-tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.penBtn.setIcon(icon27)
        self.penBtn.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.penBtn, 1, 4, 1, 1)

        self.rightMenuPages.addWidget(self.page_5)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.popupNotificaitionContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificaitionContainer.setObjectName(u"popupNotificaitionContainer")
        self.verticalLayout_19 = QVBoxLayout(self.popupNotificaitionContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 9, 9, 9)
        self.popupNotificaitionSubContainer = QWidget(self.popupNotificaitionContainer)
        self.popupNotificaitionSubContainer.setObjectName(u"popupNotificaitionSubContainer")
        self.verticalLayout_20 = QVBoxLayout(self.popupNotificaitionSubContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_14 = QLabel(self.popupNotificaitionSubContainer)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)

        self.verticalLayout_20.addWidget(self.label_14)

        self.frame_9 = QFrame(self.popupNotificaitionSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.closeNotificationBtn = QPushButton(self.frame_9)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        icon28 = QIcon()
        icon28.addFile(u":/icons/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon28)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_20.addWidget(self.frame_9)


        self.verticalLayout_19.addWidget(self.popupNotificaitionSubContainer)


        self.verticalLayout_10.addWidget(self.popupNotificaitionContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(0)
        self.rightMenuPages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionsa.setText(QCoreApplication.translate("MainWindow", u"sa", None))
#if QT_CONFIG(tooltip)
        self.actionsa.setToolTip(QCoreApplication.translate("MainWindow", u"sa", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.dataBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
#endif // QT_CONFIG(tooltip)
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
        self.fileBtn.setText(QCoreApplication.translate("MainWindow", u"Folder", None))
#if QT_CONFIG(tooltip)
        self.toolsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Tools", None))
#endif // QT_CONFIG(tooltip)
        self.toolsBtn.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Infermation about the app", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Get more Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.fileBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Open File", None))
#endif // QT_CONFIG(tooltip)
        self.fileBtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.folderBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Opne Folder", None))
#endif // QT_CONFIG(tooltip)
        self.folderBtn.setText("")
#if QT_CONFIG(tooltip)
        self.saveBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.saveBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"AIMediSight", None))
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.pagesPrevBtn.setText("")
        self.pagesNextBtn.setText("")
        self.altLabel.setText("")
        self.sagLabel.setText("")
        self.solLabel.setText("")
        self.altLabel_2.setText("")
        self.sagLabel_2.setText("")
        self.solLabel_2.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Images:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.panBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Pan", None))
#endif // QT_CONFIG(tooltip)
        self.panBtn.setText("")
#if QT_CONFIG(tooltip)
        self.playBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Play", None))
#endif // QT_CONFIG(tooltip)
        self.playBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.resetBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Reset", None))
#endif // QT_CONFIG(tooltip)
        self.resetBtn.setText("")
#if QT_CONFIG(tooltip)
        self.prevBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Prev", None))
#endif // QT_CONFIG(tooltip)
        self.prevBtn.setText("")
#if QT_CONFIG(tooltip)
        self.zoomOutBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Zoom Out", None))
#endif // QT_CONFIG(tooltip)
        self.zoomOutBtn.setText("")
#if QT_CONFIG(tooltip)
        self.pauseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Pause", None))
#endif // QT_CONFIG(tooltip)
        self.pauseBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.zoomInBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Zoom In", None))
#endif // QT_CONFIG(tooltip)
        self.zoomInBtn.setText("")
#if QT_CONFIG(tooltip)
        self.nextBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Next", None))
#endif // QT_CONFIG(tooltip)
        self.nextBtn.setText("")
#if QT_CONFIG(tooltip)
        self.penBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Pen", None))
#endif // QT_CONFIG(tooltip)
        self.penBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_13.setText("")
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
    # retranslateUi

