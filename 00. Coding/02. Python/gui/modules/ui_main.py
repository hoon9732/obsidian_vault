# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1209, 900)
        MainWindow.setMinimumSize(QSize(1080, 600))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"HANWHA DARK THEME(DEFAULT)\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(43, 37, 33, 180);\n"
"	border: 1px solid rgb(58, 49, 44);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 198, 121);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color"
                        ": rgb(52, 44, 40);\n"
"	border: 1px solid rgb(58, 49, 44);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(43, 37, 33);\n"
"}\n"
"/*\n"
"#topLogo {\n"
"	background-color: rgb(43, 37, 33);\n"
"	background-image: url(:/images/images/images/Hanwha_logo_small.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}*/\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(249, 189, 147); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(52, 44, 40);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-co"
                        "lor: rgb(249, 189, 147);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(52, 44, 40);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(249, 189, 147);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(58, 49, 44);\n"
"}\n"
"/*\n"
"#stackedWidget .QPushButton{\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border: 10px;\n"
"	border-left: 20px solid rgb(88, 71, 64);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(48, 41, 37);\n"
"	text-align: center;\n"
"	padding: 44px;\n"
"	color: rgb(149, 126, 113);\n"
"}\n"
"*/\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    "
                        "background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(48, 41, 37);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(149, 126, 113);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(52, 44, 40);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(249, 189, 147);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(58, 49, 44);\n"
"}\n"
"#extraLeftBox_2{	\n"
"	background-color: rgb(58, 49, 44);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(249, 189, 147)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
""
                        "/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(249, 196, 161); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(238, 180, 141); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(52, 44, 40);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(52, 44, 40);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(249, 189, 147);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////"
                        "////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(43, 37, 33);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(58, 49, 44);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(57, 49, 44); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(30, 26, 23); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(58, 49, 44); }\n"
"#themeSettingsTopDetail { background-color: rgb(249, 189, 147); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(58, 49, 44); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(149, 126, 113); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	ba"
                        "ckground-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(52, 44, 40);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(249, 189, 147);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	/* border-radius: 5px; */\n"
"	gridline-color: rgb(58, 49, 44);\n"
"	border-bottom: 1px solid rgb(60, 49, 44);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(60, 49, 44);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(60, 49, 44);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(249, 189, 147);\n"
"}\n"
"QHeaderView::section{\n"
""
                        "	background-color: rgb(43, 37, 33);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(58, 49, 44);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(60, 49, 44);\n"
"    border-right: 1px solid rgb(60, 49, 44);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(43, 37, 33);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(43, 37, 33);\n"
"	background-color: rgb(43, 37, 33);\n"
"	padding: 3px;\n"
"	/* border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px; */\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(60, 49, 44);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTabWidget */\n"
"QTabWidget::pane {	\n"
"	background: rgb(58, 49, 44);\n"
"	top: 0px;\n"
"}\n"
"QTabBar::tab {\n"
"	top: -2px;\n"
"	left: 2px;\n"
"	background-color: rgb(43, 37, 33);\n"
"	border: 1px solid rgb(60, 49, 44);\n"
"	padding: 14px;\n"
"}\n"
"QTabBar::tab:selected {\n"
""
                        "	background: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(43, 37, 33);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(43, 37, 33);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 198, 121);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(88, 71, 64);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(124, 101, 91);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(35, 29, 27);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 198, 121);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
""
                        "QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(88, 71, 64);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(124, 101, 91);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(72, 59, 52);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(249, 189, 147);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(77, 63, 55);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(77, 63, 55);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-"
                        "radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(72, 59, 52);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(249, 189, 147);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(77, 63, 55);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(77, 63, 55);\n"
"     height: 20px;\n"
"	border-top-left-radius"
                        ": 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 2px solid rgb(72, 59, 52);\n"
"	width: 12px;\n"
"	height: 12px;\n"
"	border-radius: 10px;\n"
"    background: rgb(60, 49, 44);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(81, 66, 58);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(72, 59, 52);\n"
"	border: 3px solid rgb(72, 59, 52);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
""
                        "RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(72, 59, 52);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(60, 49, 44);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(81, 66, 58);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 106, 94);\n"
"	border: 3px solid rgb(72, 59, 52);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(35, 29, 27);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(43, 37, 33);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(88, 71, 64);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(54, 44, 39, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radi"
                        "us: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 198, 121);	\n"
"	background-color: rgb(43, 37, 33);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(54, 44, 39);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(72, 59, 52);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(76, 62, 55);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(249, 189, 147);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(255, 195, 155);\n"
"}\n"
""
                        "QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 198, 121);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(72, 59, 52);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(76, 62, 55);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(249, 189, 147);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(255, 195, 155);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 198, 121);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 198, 121);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 17"
                        "0, 255);\n"
"	background-color: rgb(60, 49, 44);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(249, 189, 147);\n"
"	background-color: rgb(71, 58, 52);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(72, 59, 52);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(72, 59, 52);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(80, 65, 57);\n"
"	border: 2px solid rgb(86, 70, 61);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(49, 40, 35);\n"
"	border: 2px solid rgb(61, 50, 43);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.leftMenuFrame.setLineWidth(0)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 42))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 42))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.toggleLeftBox = QPushButton(self.topMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-screen-desktop.png);")

        self.verticalLayout_8.addWidget(self.toggleLeftBox)

        self.btn_testing = QPushButton(self.topMenu)
        self.btn_testing.setObjectName(u"btn_testing")
        sizePolicy.setHeightForWidth(self.btn_testing.sizePolicy().hasHeightForWidth())
        self.btn_testing.setSizePolicy(sizePolicy)
        self.btn_testing.setMinimumSize(QSize(0, 45))
        self.btn_testing.setFont(font)
        self.btn_testing.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_testing.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_testing.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-check-circle.png);")

        self.verticalLayout_8.addWidget(self.btn_testing)

        self.btn_open_gl = QPushButton(self.topMenu)
        self.btn_open_gl.setObjectName(u"btn_open_gl")
        sizePolicy.setHeightForWidth(self.btn_open_gl.sizePolicy().hasHeightForWidth())
        self.btn_open_gl.setSizePolicy(sizePolicy)
        self.btn_open_gl.setMinimumSize(QSize(0, 45))
        self.btn_open_gl.setFont(font)
        self.btn_open_gl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_open_gl.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_open_gl.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-3d.png);")

        self.verticalLayout_8.addWidget(self.btn_open_gl)

        self.btn_report = QPushButton(self.topMenu)
        self.btn_report.setObjectName(u"btn_report")
        sizePolicy.setHeightForWidth(self.btn_report.sizePolicy().hasHeightForWidth())
        self.btn_report.setSizePolicy(sizePolicy)
        self.btn_report.setMinimumSize(QSize(0, 45))
        self.btn_report.setFont(font)
        self.btn_report.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_report.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_report.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png);")

        self.verticalLayout_8.addWidget(self.btn_report)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.bottomMenu)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setMinimumSize(QSize(0, 42))
        self.btn_settings.setFont(font)
        self.btn_settings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_settings.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_settings.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-settings.png);")

        self.verticalLayout_9.addWidget(self.btn_settings)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout1 = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout1.setSpacing(0)
        self.extraColumLayout1.setObjectName(u"extraColumLayout1")
        self.extraColumLayout1.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 45))
        self.extraTopBg.setMaximumSize(QSize(16777215, 42))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon1 = QFrame(self.extraTopBg)
        self.extraIcon1.setObjectName(u"extraIcon1")
        self.extraIcon1.setMinimumSize(QSize(20, 0))
        self.extraIcon1.setMaximumSize(QSize(20, 20))
        self.extraIcon1.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon1.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon1, 0, 0, 1, 1)

        self.extraLabel1 = QLabel(self.extraTopBg)
        self.extraLabel1.setObjectName(u"extraLabel1")
        self.extraLabel1.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel1, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_51.addLayout(self.extraTopLayout)


        self.extraColumLayout1.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_browse = QPushButton(self.extraTopMenu)
        self.btn_browse.setObjectName(u"btn_browse")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_browse.sizePolicy().hasHeightForWidth())
        self.btn_browse.setSizePolicy(sizePolicy1)
        self.btn_browse.setMinimumSize(QSize(120, 45))
        self.btn_browse.setFont(font)
        self.btn_browse.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_browse.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_browse.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-folder-open.png);")

        self.verticalLayout_11.addWidget(self.btn_browse)

        self.btn_start = QPushButton(self.extraTopMenu)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy1.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy1)
        self.btn_start.setMinimumSize(QSize(120, 45))
        self.btn_start.setFont(font)
        self.btn_start.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_start.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_start.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-media-play.png);")

        self.verticalLayout_11.addWidget(self.btn_start)

        self.btn_graph = QPushButton(self.extraTopMenu)
        self.btn_graph.setObjectName(u"btn_graph")
        sizePolicy1.setHeightForWidth(self.btn_graph.sizePolicy().hasHeightForWidth())
        self.btn_graph.setSizePolicy(sizePolicy1)
        self.btn_graph.setMinimumSize(QSize(120, 45))
        self.btn_graph.setFont(font)
        self.btn_graph.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_graph.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_graph.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-line.png);")

        self.verticalLayout_11.addWidget(self.btn_graph)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout1.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setEnabled(True)
        self.contentTopBg.setMinimumSize(QSize(0, 42))
        self.contentTopBg.setMaximumSize(QSize(16777215, 42))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftBox)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 0))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 42))
        self.topLogoInfo.setStyleSheet(u"")
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(10, 5, 200, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(10, 25, 200, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleRightInfo = QLabel(self.topLogoInfo)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setGeometry(QRect(0, 0, 950, 42))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 42))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.topLogoInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(120, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settingsTopBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"images/icons/cil-chat-bubble.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(100, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: rgb(88,71, 64);")
        self.stackedWidget.setLineWidth(0)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setEnabled(True)
        self.home.setStyleSheet(u"/*\n"
"background-image: url(:/images/images/images/Hanwha_white.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;\n"
"border: -1px\n"
"\n"
"background-position: center center;\n"
"background-attachment: fixed;\n"
"background: rgb(60, 49, 44);\n"
"*/")
        self.missile_1 = QPushButton(self.home)
        self.missile_1.setObjectName(u"missile_1")
        self.missile_1.setGeometry(QRect(40, 420, 520, 360))
        self.missile_1.setStyleSheet(u"QPushButton{\n"
"	border-radius: 12px;\n"
"	color: rgb(230, 230, 230);\n"
"	font-size: 32px;\n"
"\n"
"	border-left: 3px solid rgb(230, 230, 230);\n"
"	border-right: 1px solid rgb(230, 230, 230);\n"
"	border-top: 3px solid rgb(230, 230, 230);\n"
"	border-bottom: 1px solid rgb(230, 230, 230);\n"
"	border-image: url(:/images/images/images/missile_1.png) 0 0 0 0 stretch stretch;\n"
" }\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(60, 49, 44);\n"
"	border-left: 0px solid rgb(230, 230, 230);\n"
"	border-right: 0px solid rgb(230, 230, 230);\n"
"	border-top: 0px solid rgb(230, 230, 230);\n"
"	border-bottom: 0px solid rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(43, 37, 33);\n"
"	border-left: 0px solid rgb(230, 230, 230);\n"
"	border-right: 0px solid rgb(230, 230, 230);\n"
"	border-top: 0px solid rgb(230, 230, 230);\n"
"	border-bottom: 0px solid rgb(230, 230, 230);\n"
"}\n"
"")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(320, 20, 500, 400))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setToolTipDuration(-1)
        self.frame.setStyleSheet(u"border-image: url(:/images/images/images/Hanwha_white.png) 0 0 0 0 stretch stretch;\n"
"border: 10px\n"
"/*\n"
"background-position: center center;\n"
"background-attachment: fixed;\n"
"background: rgb(60, 49, 44);\n"
"*/")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.missile_2 = QPushButton(self.home)
        self.missile_2.setObjectName(u"missile_2")
        self.missile_2.setGeometry(QRect(600, 420, 520, 360))
        self.missile_2.setStyleSheet(u"QPushButton{\n"
"	border-radius: 12px;\n"
"	color: rgb(230, 230, 230);\n"
"	font-size: 32px;\n"
"\n"
"	border-left: 3px solid rgb(230, 230, 230);\n"
"	border-right: 1px solid rgb(230, 230, 230);\n"
"	border-top: 3px solid rgb(230, 230, 230);\n"
"	border-bottom: 1px solid rgb(230, 230, 230);\n"
"	border-image: url(:/images/images/images/missile_2.png) 0 0 0 0 stretch stretch;\n"
" }\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(60, 49, 44);\n"
"	border-left: 0px solid rgb(230, 230, 230);\n"
"	border-right: 0px solid rgb(230, 230, 230);\n"
"	border-top: 0px solid rgb(230, 230, 230);\n"
"	border-bottom: 0px solid rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(43, 37, 33);\n"
"	border-left: 0px solid rgb(230, 230, 230);\n"
"	border-right: 0px solid rgb(230, 230, 230);\n"
"	border-top: 0px solid rgb(230, 230, 230);\n"
"	border-bottom: 0px solid rgb(230, 230, 230);\n"
"}\n"
"")
        self.label = QLabel(self.home)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 780, 520, 40))
        self.label.setStyleSheet(u"QLabel{\n"
"	font-size: 32px;\n"
"	font-weight: bold;\n"
"}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(600, 780, 520, 40))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	font-size: 32px;\n"
"	font-weight: bold;\n"
"}")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.home)
        self.frame.raise_()
        self.missile_1.raise_()
        self.missile_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.open_gl = QWidget()
        self.open_gl.setObjectName(u"open_gl")
        self.tabWidget_3 = QTabWidget(self.open_gl)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(0, 0, 1018, 831))
        self.tab_19 = QWidget()
        self.tab_19.setObjectName(u"tab_19")
        self.sensorTable_19 = QTableWidget(self.tab_19)
        if (self.sensorTable_19.columnCount() < 5):
            self.sensorTable_19.setColumnCount(5)
        if (self.sensorTable_19.rowCount() < 10):
            self.sensorTable_19.setRowCount(10)
        self.sensorTable_19.setObjectName(u"sensorTable_19")
        self.sensorTable_19.setGeometry(QRect(0, 140, 960, 400))
        sizePolicy4.setHeightForWidth(self.sensorTable_19.sizePolicy().hasHeightForWidth())
        self.sensorTable_19.setSizePolicy(sizePolicy4)
        self.sensorTable_19.setMinimumSize(QSize(0, 0))
        self.sensorTable_19.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_19.setSizeIncrement(QSize(0, 0))
        self.sensorTable_19.setLineWidth(1)
        self.sensorTable_19.setAlternatingRowColors(True)
        self.sensorTable_19.setRowCount(10)
        self.sensorTable_19.setColumnCount(5)
        self.sensorTable_19.horizontalHeader().setVisible(True)
        self.sensorTable_19.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_19.horizontalHeader().setDefaultSectionSize(180)
        self.sensorTable_19.verticalHeader().setVisible(False)
        self.sensorTable_19.verticalHeader().setStretchLastSection(False)
        self.btn_testlaunch = QPushButton(self.tab_19)
        self.btn_testlaunch.setObjectName(u"btn_testlaunch")
        self.btn_testlaunch.setGeometry(QRect(330, 10, 300, 120))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.btn_testlaunch.setFont(font4)
        self.btn_testlaunch.setStyleSheet(u"background-color: #63BF5E;\n"
"border: -1px;\n"
"font-size: 40px;")
        self.btn_siteview = QPushButton(self.tab_19)
        self.btn_siteview.setObjectName(u"btn_siteview")
        self.btn_siteview.setGeometry(QRect(10, 10, 300, 120))
        self.btn_siteview.setFont(font4)
        self.btn_siteview.setStyleSheet(u"background-color: #BF9567;\n"
"font-size: 40px;")
        self.btn_abortlaunch = QPushButton(self.tab_19)
        self.btn_abortlaunch.setObjectName(u"btn_abortlaunch")
        self.btn_abortlaunch.setGeometry(QRect(650, 10, 300, 120))
        self.btn_abortlaunch.setFont(font4)
        self.btn_abortlaunch.setStyleSheet(u"background-color: #BF503A;\n"
"font-size: 40px;")
        self.tabWidget_3.addTab(self.tab_19, "")
        self.tab_20 = QWidget()
        self.tab_20.setObjectName(u"tab_20")
        self.sensorTable_20 = QTableWidget(self.tab_20)
        if (self.sensorTable_20.columnCount() < 5):
            self.sensorTable_20.setColumnCount(5)
        if (self.sensorTable_20.rowCount() < 10):
            self.sensorTable_20.setRowCount(10)
        self.sensorTable_20.setObjectName(u"sensorTable_20")
        self.sensorTable_20.setGeometry(QRect(0, 0, 960, 480))
        sizePolicy4.setHeightForWidth(self.sensorTable_20.sizePolicy().hasHeightForWidth())
        self.sensorTable_20.setSizePolicy(sizePolicy4)
        self.sensorTable_20.setMinimumSize(QSize(0, 0))
        self.sensorTable_20.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_20.setSizeIncrement(QSize(0, 0))
        self.sensorTable_20.setLineWidth(1)
        self.sensorTable_20.setAlternatingRowColors(True)
        self.sensorTable_20.setRowCount(10)
        self.sensorTable_20.setColumnCount(5)
        self.sensorTable_20.horizontalHeader().setVisible(True)
        self.sensorTable_20.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_20.horizontalHeader().setDefaultSectionSize(180)
        self.sensorTable_20.verticalHeader().setVisible(False)
        self.sensorTable_20.verticalHeader().setStretchLastSection(False)
        self.tabWidget_3.addTab(self.tab_20, "")
        self.stackedWidget.addWidget(self.open_gl)
        self.testing = QWidget()
        self.testing.setObjectName(u"testing")
        self.tabWidget_2 = QTabWidget(self.testing)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 998, 695))
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.sensorTable_10 = QTableWidget(self.tab_10)
        if (self.sensorTable_10.columnCount() < 6):
            self.sensorTable_10.setColumnCount(6)
        if (self.sensorTable_10.rowCount() < 40):
            self.sensorTable_10.setRowCount(40)
        self.sensorTable_10.setObjectName(u"sensorTable_10")
        self.sensorTable_10.setGeometry(QRect(0, 0, 960, 1080))
        sizePolicy4.setHeightForWidth(self.sensorTable_10.sizePolicy().hasHeightForWidth())
        self.sensorTable_10.setSizePolicy(sizePolicy4)
        self.sensorTable_10.setMinimumSize(QSize(0, 0))
        self.sensorTable_10.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_10.setSizeIncrement(QSize(0, 0))
        self.sensorTable_10.setLineWidth(1)
        self.sensorTable_10.setAlternatingRowColors(True)
        self.sensorTable_10.setRowCount(40)
        self.sensorTable_10.setColumnCount(6)
        self.sensorTable_10.horizontalHeader().setVisible(True)
        self.sensorTable_10.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_10.horizontalHeader().setDefaultSectionSize(150)
        self.sensorTable_10.verticalHeader().setVisible(False)
        self.sensorTable_10.verticalHeader().setStretchLastSection(False)
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.sensorTable_11 = QTableWidget(self.tab_11)
        if (self.sensorTable_11.columnCount() < 6):
            self.sensorTable_11.setColumnCount(6)
        if (self.sensorTable_11.rowCount() < 40):
            self.sensorTable_11.setRowCount(40)
        self.sensorTable_11.setObjectName(u"sensorTable_11")
        self.sensorTable_11.setGeometry(QRect(0, 0, 960, 1080))
        sizePolicy4.setHeightForWidth(self.sensorTable_11.sizePolicy().hasHeightForWidth())
        self.sensorTable_11.setSizePolicy(sizePolicy4)
        self.sensorTable_11.setMinimumSize(QSize(0, 0))
        self.sensorTable_11.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_11.setSizeIncrement(QSize(0, 0))
        self.sensorTable_11.setLineWidth(1)
        self.sensorTable_11.setAlternatingRowColors(True)
        self.sensorTable_11.setRowCount(40)
        self.sensorTable_11.setColumnCount(6)
        self.sensorTable_11.horizontalHeader().setVisible(True)
        self.sensorTable_11.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_11.horizontalHeader().setDefaultSectionSize(150)
        self.sensorTable_11.verticalHeader().setVisible(False)
        self.sensorTable_11.verticalHeader().setStretchLastSection(False)
        self.tabWidget_2.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.sensorTable_12 = QTableWidget(self.tab_12)
        if (self.sensorTable_12.columnCount() < 6):
            self.sensorTable_12.setColumnCount(6)
        if (self.sensorTable_12.rowCount() < 40):
            self.sensorTable_12.setRowCount(40)
        self.sensorTable_12.setObjectName(u"sensorTable_12")
        self.sensorTable_12.setGeometry(QRect(0, 0, 960, 1080))
        sizePolicy4.setHeightForWidth(self.sensorTable_12.sizePolicy().hasHeightForWidth())
        self.sensorTable_12.setSizePolicy(sizePolicy4)
        self.sensorTable_12.setMinimumSize(QSize(0, 0))
        self.sensorTable_12.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_12.setSizeIncrement(QSize(0, 0))
        self.sensorTable_12.setLineWidth(1)
        self.sensorTable_12.setAlternatingRowColors(True)
        self.sensorTable_12.setRowCount(40)
        self.sensorTable_12.setColumnCount(6)
        self.sensorTable_12.horizontalHeader().setVisible(True)
        self.sensorTable_12.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_12.horizontalHeader().setDefaultSectionSize(150)
        self.sensorTable_12.verticalHeader().setVisible(False)
        self.sensorTable_12.verticalHeader().setStretchLastSection(False)
        self.tabWidget_2.addTab(self.tab_12, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.sensorTable_13 = QTableWidget(self.tab_13)
        if (self.sensorTable_13.columnCount() < 6):
            self.sensorTable_13.setColumnCount(6)
        if (self.sensorTable_13.rowCount() < 40):
            self.sensorTable_13.setRowCount(40)
        self.sensorTable_13.setObjectName(u"sensorTable_13")
        self.sensorTable_13.setGeometry(QRect(0, 0, 960, 1080))
        sizePolicy4.setHeightForWidth(self.sensorTable_13.sizePolicy().hasHeightForWidth())
        self.sensorTable_13.setSizePolicy(sizePolicy4)
        self.sensorTable_13.setMinimumSize(QSize(0, 0))
        self.sensorTable_13.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_13.setSizeIncrement(QSize(0, 0))
        self.sensorTable_13.setLineWidth(1)
        self.sensorTable_13.setAlternatingRowColors(True)
        self.sensorTable_13.setRowCount(40)
        self.sensorTable_13.setColumnCount(6)
        self.sensorTable_13.horizontalHeader().setVisible(True)
        self.sensorTable_13.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_13.horizontalHeader().setDefaultSectionSize(150)
        self.sensorTable_13.verticalHeader().setVisible(False)
        self.sensorTable_13.verticalHeader().setStretchLastSection(False)
        self.tabWidget_2.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.sensorTable_14 = QTableWidget(self.tab_14)
        if (self.sensorTable_14.columnCount() < 6):
            self.sensorTable_14.setColumnCount(6)
        if (self.sensorTable_14.rowCount() < 40):
            self.sensorTable_14.setRowCount(40)
        self.sensorTable_14.setObjectName(u"sensorTable_14")
        self.sensorTable_14.setGeometry(QRect(0, 0, 960, 1080))
        sizePolicy4.setHeightForWidth(self.sensorTable_14.sizePolicy().hasHeightForWidth())
        self.sensorTable_14.setSizePolicy(sizePolicy4)
        self.sensorTable_14.setMinimumSize(QSize(0, 0))
        self.sensorTable_14.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_14.setSizeIncrement(QSize(0, 0))
        self.sensorTable_14.setLineWidth(1)
        self.sensorTable_14.setAlternatingRowColors(True)
        self.sensorTable_14.setRowCount(40)
        self.sensorTable_14.setColumnCount(6)
        self.sensorTable_14.horizontalHeader().setVisible(True)
        self.sensorTable_14.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_14.horizontalHeader().setDefaultSectionSize(150)
        self.sensorTable_14.verticalHeader().setVisible(False)
        self.sensorTable_14.verticalHeader().setStretchLastSection(False)
        self.tabWidget_2.addTab(self.tab_14, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.sensorTable_15 = QTableWidget(self.tab_15)
        if (self.sensorTable_15.columnCount() < 6):
            self.sensorTable_15.setColumnCount(6)
        if (self.sensorTable_15.rowCount() < 40):
            self.sensorTable_15.setRowCount(40)
        self.sensorTable_15.setObjectName(u"sensorTable_15")
        self.sensorTable_15.setGeometry(QRect(0, 0, 960, 1080))
        sizePolicy4.setHeightForWidth(self.sensorTable_15.sizePolicy().hasHeightForWidth())
        self.sensorTable_15.setSizePolicy(sizePolicy4)
        self.sensorTable_15.setMinimumSize(QSize(0, 0))
        self.sensorTable_15.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_15.setSizeIncrement(QSize(0, 0))
        self.sensorTable_15.setLineWidth(1)
        self.sensorTable_15.setAlternatingRowColors(True)
        self.sensorTable_15.setRowCount(40)
        self.sensorTable_15.setColumnCount(6)
        self.sensorTable_15.horizontalHeader().setVisible(True)
        self.sensorTable_15.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_15.horizontalHeader().setDefaultSectionSize(150)
        self.sensorTable_15.verticalHeader().setVisible(False)
        self.sensorTable_15.verticalHeader().setStretchLastSection(False)
        self.tabWidget_2.addTab(self.tab_15, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.sensorTable_16 = QTableWidget(self.tab_16)
        if (self.sensorTable_16.columnCount() < 6):
            self.sensorTable_16.setColumnCount(6)
        if (self.sensorTable_16.rowCount() < 40):
            self.sensorTable_16.setRowCount(40)
        self.sensorTable_16.setObjectName(u"sensorTable_16")
        self.sensorTable_16.setGeometry(QRect(0, 0, 960, 1080))
        sizePolicy4.setHeightForWidth(self.sensorTable_16.sizePolicy().hasHeightForWidth())
        self.sensorTable_16.setSizePolicy(sizePolicy4)
        self.sensorTable_16.setMinimumSize(QSize(0, 0))
        self.sensorTable_16.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_16.setSizeIncrement(QSize(0, 0))
        self.sensorTable_16.setLineWidth(1)
        self.sensorTable_16.setAlternatingRowColors(True)
        self.sensorTable_16.setRowCount(40)
        self.sensorTable_16.setColumnCount(6)
        self.sensorTable_16.horizontalHeader().setVisible(True)
        self.sensorTable_16.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_16.horizontalHeader().setDefaultSectionSize(150)
        self.sensorTable_16.verticalHeader().setVisible(False)
        self.sensorTable_16.verticalHeader().setStretchLastSection(False)
        self.tabWidget_2.addTab(self.tab_16, "")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.sensorTable_17 = QTableWidget(self.tab_17)
        if (self.sensorTable_17.columnCount() < 6):
            self.sensorTable_17.setColumnCount(6)
        if (self.sensorTable_17.rowCount() < 40):
            self.sensorTable_17.setRowCount(40)
        self.sensorTable_17.setObjectName(u"sensorTable_17")
        self.sensorTable_17.setGeometry(QRect(0, 0, 960, 1080))
        sizePolicy4.setHeightForWidth(self.sensorTable_17.sizePolicy().hasHeightForWidth())
        self.sensorTable_17.setSizePolicy(sizePolicy4)
        self.sensorTable_17.setMinimumSize(QSize(0, 0))
        self.sensorTable_17.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_17.setSizeIncrement(QSize(0, 0))
        self.sensorTable_17.setLineWidth(1)
        self.sensorTable_17.setAlternatingRowColors(True)
        self.sensorTable_17.setRowCount(40)
        self.sensorTable_17.setColumnCount(6)
        self.sensorTable_17.horizontalHeader().setVisible(True)
        self.sensorTable_17.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_17.horizontalHeader().setDefaultSectionSize(150)
        self.sensorTable_17.verticalHeader().setVisible(False)
        self.sensorTable_17.verticalHeader().setStretchLastSection(False)
        self.tabWidget_2.addTab(self.tab_17, "")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.sensorTable_18 = QTableWidget(self.tab_18)
        if (self.sensorTable_18.columnCount() < 6):
            self.sensorTable_18.setColumnCount(6)
        if (self.sensorTable_18.rowCount() < 40):
            self.sensorTable_18.setRowCount(40)
        self.sensorTable_18.setObjectName(u"sensorTable_18")
        self.sensorTable_18.setGeometry(QRect(0, 0, 960, 1080))
        sizePolicy4.setHeightForWidth(self.sensorTable_18.sizePolicy().hasHeightForWidth())
        self.sensorTable_18.setSizePolicy(sizePolicy4)
        self.sensorTable_18.setMinimumSize(QSize(0, 0))
        self.sensorTable_18.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_18.setSizeIncrement(QSize(0, 0))
        self.sensorTable_18.setLineWidth(1)
        self.sensorTable_18.setAlternatingRowColors(True)
        self.sensorTable_18.setRowCount(40)
        self.sensorTable_18.setColumnCount(6)
        self.sensorTable_18.horizontalHeader().setVisible(True)
        self.sensorTable_18.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_18.horizontalHeader().setDefaultSectionSize(150)
        self.sensorTable_18.verticalHeader().setVisible(False)
        self.sensorTable_18.verticalHeader().setStretchLastSection(False)
        self.tabWidget_2.addTab(self.tab_18, "")
        self.stackedWidget.addWidget(self.testing)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.settings.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.settings)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.settings)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.settings)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.commandLinkButton.setIcon(icon5)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.settings)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(88, 71, 64, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.settings)
        self.monitor = QWidget()
        self.monitor.setObjectName(u"monitor")
        self.monitor.setStyleSheet(u"background: transparent;")
        self.verticalLayout_20 = QVBoxLayout(self.monitor)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.monitor)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy5)
        self.tabWidget.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy5.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy5)
        self.sensorTable = QTableWidget(self.tab)
        if (self.sensorTable.columnCount() < 6):
            self.sensorTable.setColumnCount(6)
        if (self.sensorTable.rowCount() < 40):
            self.sensorTable.setRowCount(40)
        self.sensorTable.setObjectName(u"sensorTable")
        self.sensorTable.setGeometry(QRect(0, 0, 800, 1080))
        sizePolicy4.setHeightForWidth(self.sensorTable.sizePolicy().hasHeightForWidth())
        self.sensorTable.setSizePolicy(sizePolicy4)
        self.sensorTable.setMinimumSize(QSize(0, 0))
        self.sensorTable.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable.setSizeIncrement(QSize(0, 0))
        self.sensorTable.setLineWidth(1)
        self.sensorTable.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sensorTable.setDragEnabled(True)
        self.sensorTable.setAlternatingRowColors(True)
        self.sensorTable.setRowCount(40)
        self.sensorTable.setColumnCount(6)
        self.sensorTable.horizontalHeader().setVisible(True)
        self.sensorTable.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable.horizontalHeader().setDefaultSectionSize(180)
        self.sensorTable.verticalHeader().setVisible(False)
        self.sensorTable.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.sensorTable_2 = QTableWidget(self.tab_2)
        if (self.sensorTable_2.columnCount() < 6):
            self.sensorTable_2.setColumnCount(6)
        if (self.sensorTable_2.rowCount() < 40):
            self.sensorTable_2.setRowCount(40)
        self.sensorTable_2.setObjectName(u"sensorTable_2")
        self.sensorTable_2.setGeometry(QRect(0, 0, 960, 1080))
        self.sensorTable_2.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_2.setAlternatingRowColors(True)
        self.sensorTable_2.setRowCount(40)
        self.sensorTable_2.setColumnCount(6)
        self.sensorTable_2.horizontalHeader().setVisible(True)
        self.sensorTable_2.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_2.horizontalHeader().setDefaultSectionSize(180)
        self.sensorTable_2.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.sensorTable_3 = QTableWidget(self.tab_3)
        if (self.sensorTable_3.columnCount() < 6):
            self.sensorTable_3.setColumnCount(6)
        if (self.sensorTable_3.rowCount() < 40):
            self.sensorTable_3.setRowCount(40)
        self.sensorTable_3.setObjectName(u"sensorTable_3")
        self.sensorTable_3.setGeometry(QRect(0, 0, 960, 1080))
        self.sensorTable_3.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_3.setAlternatingRowColors(True)
        self.sensorTable_3.setRowCount(40)
        self.sensorTable_3.setColumnCount(6)
        self.sensorTable_3.horizontalHeader().setVisible(True)
        self.sensorTable_3.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_3.horizontalHeader().setDefaultSectionSize(180)
        self.sensorTable_3.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.sensorTable_4 = QTableWidget(self.tab_4)
        if (self.sensorTable_4.columnCount() < 6):
            self.sensorTable_4.setColumnCount(6)
        if (self.sensorTable_4.rowCount() < 40):
            self.sensorTable_4.setRowCount(40)
        self.sensorTable_4.setObjectName(u"sensorTable_4")
        self.sensorTable_4.setGeometry(QRect(0, 0, 960, 1080))
        self.sensorTable_4.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_4.setAlternatingRowColors(True)
        self.sensorTable_4.setRowCount(40)
        self.sensorTable_4.setColumnCount(6)
        self.sensorTable_4.horizontalHeader().setVisible(True)
        self.sensorTable_4.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_4.horizontalHeader().setDefaultSectionSize(180)
        self.sensorTable_4.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.sensorTable_5 = QTableWidget(self.tab_5)
        if (self.sensorTable_5.columnCount() < 6):
            self.sensorTable_5.setColumnCount(6)
        if (self.sensorTable_5.rowCount() < 40):
            self.sensorTable_5.setRowCount(40)
        self.sensorTable_5.setObjectName(u"sensorTable_5")
        self.sensorTable_5.setGeometry(QRect(0, 0, 960, 1080))
        self.sensorTable_5.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_5.setAlternatingRowColors(True)
        self.sensorTable_5.setRowCount(40)
        self.sensorTable_5.setColumnCount(6)
        self.sensorTable_5.horizontalHeader().setVisible(True)
        self.sensorTable_5.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_5.horizontalHeader().setDefaultSectionSize(180)
        self.sensorTable_5.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.sensorTable_6 = QTableWidget(self.tab_6)
        if (self.sensorTable_6.columnCount() < 6):
            self.sensorTable_6.setColumnCount(6)
        if (self.sensorTable_6.rowCount() < 40):
            self.sensorTable_6.setRowCount(40)
        self.sensorTable_6.setObjectName(u"sensorTable_6")
        self.sensorTable_6.setGeometry(QRect(0, 0, 960, 1080))
        self.sensorTable_6.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_6.setAlternatingRowColors(True)
        self.sensorTable_6.setRowCount(40)
        self.sensorTable_6.setColumnCount(6)
        self.sensorTable_6.horizontalHeader().setVisible(True)
        self.sensorTable_6.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_6.horizontalHeader().setDefaultSectionSize(180)
        self.sensorTable_6.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.sensorTable_7 = QTableWidget(self.tab_7)
        if (self.sensorTable_7.columnCount() < 6):
            self.sensorTable_7.setColumnCount(6)
        if (self.sensorTable_7.rowCount() < 40):
            self.sensorTable_7.setRowCount(40)
        self.sensorTable_7.setObjectName(u"sensorTable_7")
        self.sensorTable_7.setGeometry(QRect(0, 0, 960, 1080))
        self.sensorTable_7.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_7.setAlternatingRowColors(True)
        self.sensorTable_7.setRowCount(40)
        self.sensorTable_7.setColumnCount(6)
        self.sensorTable_7.horizontalHeader().setVisible(True)
        self.sensorTable_7.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_7.horizontalHeader().setDefaultSectionSize(180)
        self.sensorTable_7.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.sensorTable_8 = QTableWidget(self.tab_8)
        if (self.sensorTable_8.columnCount() < 6):
            self.sensorTable_8.setColumnCount(6)
        if (self.sensorTable_8.rowCount() < 40):
            self.sensorTable_8.setRowCount(40)
        self.sensorTable_8.setObjectName(u"sensorTable_8")
        self.sensorTable_8.setGeometry(QRect(0, 0, 960, 1080))
        self.sensorTable_8.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_8.setAlternatingRowColors(True)
        self.sensorTable_8.setRowCount(40)
        self.sensorTable_8.setColumnCount(6)
        self.sensorTable_8.horizontalHeader().setVisible(True)
        self.sensorTable_8.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_8.horizontalHeader().setDefaultSectionSize(180)
        self.sensorTable_8.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.sensorTable_9 = QTableWidget(self.tab_9)
        if (self.sensorTable_9.columnCount() < 6):
            self.sensorTable_9.setColumnCount(6)
        if (self.sensorTable_9.rowCount() < 40):
            self.sensorTable_9.setRowCount(40)
        self.sensorTable_9.setObjectName(u"sensorTable_9")
        self.sensorTable_9.setGeometry(QRect(0, 0, 960, 1080))
        self.sensorTable_9.setMaximumSize(QSize(16777215, 16777215))
        self.sensorTable_9.setAlternatingRowColors(True)
        self.sensorTable_9.setRowCount(40)
        self.sensorTable_9.setColumnCount(6)
        self.sensorTable_9.horizontalHeader().setVisible(True)
        self.sensorTable_9.horizontalHeader().setMinimumSectionSize(32)
        self.sensorTable_9.horizontalHeader().setDefaultSectionSize(180)
        self.sensorTable_9.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_9, "")

        self.verticalLayout_20.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.monitor)
        self.report = QWidget()
        self.report.setObjectName(u"report")
        self.report.setEnabled(True)
        self.report.setAutoFillBackground(False)
        self.row_4 = QFrame(self.report)
        self.row_4.setObjectName(u"row_4")
        self.row_4.setGeometry(QRect(10, 10, 872, 112))
        self.row_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.row_4)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_2 = QFrame(self.row_4)
        self.frame_div_content_2.setObjectName(u"frame_div_content_2")
        self.frame_div_content_2.setMinimumSize(QSize(0, 110))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_div_content_2)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_2 = QFrame(self.frame_div_content_2)
        self.frame_title_wid_2.setObjectName(u"frame_title_wid_2")
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.labelBoxBlenderInstalation_2 = QLabel(self.frame_title_wid_2)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")

        self.verticalLayout_24.addWidget(self.labelBoxBlenderInstalation_2)


        self.verticalLayout_23.addWidget(self.frame_title_wid_2)

        self.frame_content_wid_2 = QFrame(self.frame_div_content_2)
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        self.frame_content_wid_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_content_wid_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_2 = QLineEdit(self.frame_content_wid_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_content_wid_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_2.setIcon(icon4)

        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.labelVersion_4 = QLabel(self.frame_content_wid_2)
        self.labelVersion_4.setObjectName(u"labelVersion_4")
        self.labelVersion_4.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelVersion_4, 1, 0, 1, 2)


        self.horizontalLayout_10.addLayout(self.gridLayout_3)


        self.verticalLayout_23.addWidget(self.frame_content_wid_2)


        self.verticalLayout_22.addWidget(self.frame_div_content_2)

        self.row_5 = QFrame(self.report)
        self.row_5.setObjectName(u"row_5")
        self.row_5.setGeometry(QRect(10, 130, 892, 347))
        self.row_5.setMinimumSize(QSize(0, 150))
        self.row_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.row_5)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_2 = QTableWidget(self.row_5)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        if (self.tableWidget_2.rowCount() < 16):
            self.tableWidget_2.setRowCount(16)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font5);
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, __qtablewidgetitem47)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy4.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy4)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(221, 221, 221, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.tableWidget_2.setPalette(palette1)
        self.tableWidget_2.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_13.addWidget(self.tableWidget_2)

        self.stackedWidget.addWidget(self.report)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_polish = QPushButton(self.topMenus)
        self.btn_polish.setObjectName(u"btn_polish")
        sizePolicy.setHeightForWidth(self.btn_polish.sizePolicy().hasHeightForWidth())
        self.btn_polish.setSizePolicy(sizePolicy)
        self.btn_polish.setMinimumSize(QSize(0, 45))
        self.btn_polish.setFont(font)
        self.btn_polish.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_polish.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_polish.setStyleSheet(u"/*background-image: url(:/icons/images/icons/cil-envelope-open.png);*/")

        self.verticalLayout_14.addWidget(self.btn_polish)

        self.btn_arabic = QPushButton(self.topMenus)
        self.btn_arabic.setObjectName(u"btn_arabic")
        sizePolicy.setHeightForWidth(self.btn_arabic.sizePolicy().hasHeightForWidth())
        self.btn_arabic.setSizePolicy(sizePolicy)
        self.btn_arabic.setMinimumSize(QSize(0, 45))
        self.btn_arabic.setFont(font)
        self.btn_arabic.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_arabic.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_arabic.setStyleSheet(u"/*background-image: url(:/icons/images/icons/cil-print.png);*/")

        self.verticalLayout_14.addWidget(self.btn_arabic)

        self.btn_english = QPushButton(self.topMenus)
        self.btn_english.setObjectName(u"btn_english")
        sizePolicy.setHeightForWidth(self.btn_english.sizePolicy().hasHeightForWidth())
        self.btn_english.setSizePolicy(sizePolicy)
        self.btn_english.setMinimumSize(QSize(0, 45))
        self.btn_english.setFont(font)
        self.btn_english.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_english.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_english.setStyleSheet(u"/*background-image: url(:/icons/images/icons/cil-account-logout.png);*/")

        self.verticalLayout_14.addWidget(self.btn_english)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        sizePolicy5.setHeightForWidth(self.bottomBar.sizePolicy().hasHeightForWidth())
        self.bottomBar.setSizePolicy(sizePolicy5)
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.version_2 = QLabel(self.bottomBar)
        self.version_2.setObjectName(u"version_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.version_2.sizePolicy().hasHeightForWidth())
        self.version_2.setSizePolicy(sizePolicy6)
        self.version_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version_2)

        self.cbConnection = QCheckBox(self.bottomBar)
        self.cbConnection.setObjectName(u"cbConnection")
        self.cbConnection.setFont(font)
        self.cbConnection.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.cbConnection.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.cbConnection.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.cbConnection)

        self.cbApproval = QCheckBox(self.bottomBar)
        self.cbApproval.setObjectName(u"cbApproval")
        self.cbApproval.setMinimumSize(QSize(0, 1))
        self.cbApproval.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.cbApproval.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.cbApproval)

        self.cbValue = QCheckBox(self.bottomBar)
        self.cbValue.setObjectName(u"cbValue")
        self.cbValue.setMinimumSize(QSize(0, 0))
        self.cbValue.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.cbValue)

        self.cbUnit = QCheckBox(self.bottomBar)
        self.cbUnit.setObjectName(u"cbUnit")
        self.cbUnit.setMinimumSize(QSize(0, 0))
        self.cbUnit.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.cbUnit)

        self.cbRange = QCheckBox(self.bottomBar)
        self.cbRange.setObjectName(u"cbRange")
        self.cbRange.setMinimumSize(QSize(0, 0))
        self.cbRange.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.cbRange)

        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Monitor", None))
        self.btn_testing.setText(QCoreApplication.translate("MainWindow", u"Testing", None))
        self.btn_open_gl.setText(QCoreApplication.translate("MainWindow", u"Simulation", None))
        self.btn_report.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.extraLabel1.setText(QCoreApplication.translate("MainWindow", u"Preset Settings", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_browse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_graph.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffc679;\">GPMTS</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">General Purpose Missile Testing Software Based on PySide6</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-"
                        "bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffc679;\">PATCH UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">update.cmd </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#f9bd93;\">Hanwha Aerospace PGM Systems</span>                    </p></body></html>", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"GPMTS", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"General Purpose Missile Testing System", None))
        self.titleRightInfo.setText("")
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText(QCoreApplication.translate("MainWindow", u" Languages", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.missile_1.setText("")
        self.missile_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Block I", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Block II", None))
        self.btn_testlaunch.setText(QCoreApplication.translate("MainWindow", u"Test Launch", None))
        self.btn_siteview.setText(QCoreApplication.translate("MainWindow", u"Site View", None))
        self.btn_abortlaunch.setText(QCoreApplication.translate("MainWindow", u"Abort Launch", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_19), QCoreApplication.translate("MainWindow", u"Scenario 1", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_20), QCoreApplication.translate("MainWindow", u"Scenario 2", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\uad6c\ub3d9\uc7a5\uce58\uc601\uc810", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"\ubd84\ud574\ud0c4 \uc810\uac80", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\uc644\uc131\ud0c4 \uc810\uac80", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"\uc7a5\uc785\ud0c4 \uc810\uac80", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"\uccb4\uacc4\ud1b5\ud569 \uc810\uac80", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"\uc13c\uc11c \uc810\uac80", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_16), QCoreApplication.translate("MainWindow", u"GCU/\ud56d\ubc95/RDC \uc810\uac80", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_17), QCoreApplication.translate("MainWindow", u"\uc2dc\ud5d8\uae30 \uc790\uccb4\uc810\uac80", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_18), QCoreApplication.translate("MainWindow", u"\ud658\uacbd\uc2dc\ud5d8", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\uad6c\ub3d9\uc7a5\uce58\uc601\uc810", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\ubd84\ud574\ud0c4 \uc810\uac80", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\uc644\uc131\ud0c4 \uc810\uac80", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\uc7a5\uc785\ud0c4 \uc810\uac80", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\uccb4\uacc4\ud1b5\ud569 \uc810\uac80", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\uc13c\uc11c \uc810\uac80", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"GCU/\ud56d\ubc95/RDC \uc810\uac80", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\uc2dc\ud5d8\uae30 \uc790\uccb4\uc810\uac80", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\ud658\uacbd\uc2dc\ud5d8", None))
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_4.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        ___qtablewidgetitem24 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem25 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem26 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem27 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem28 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem29 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem30 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem32 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem33 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem34 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem35 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem36 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem37 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem38 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem39 = self.tableWidget_2.verticalHeaderItem(11)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem40 = self.tableWidget_2.verticalHeaderItem(12)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem41 = self.tableWidget_2.verticalHeaderItem(13)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem42 = self.tableWidget_2.verticalHeaderItem(14)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem43 = self.tableWidget_2.verticalHeaderItem(15)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem44 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem45 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem46 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem47 = self.tableWidget_2.item(0, 3)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.btn_polish.setText(QCoreApplication.translate("MainWindow", u"Polish", None))
        self.btn_arabic.setText(QCoreApplication.translate("MainWindow", u"Arabic", None))
        self.btn_english.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.version_2.setText("")
        self.cbConnection.setText(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.cbApproval.setText(QCoreApplication.translate("MainWindow", u"Approval", None))
        self.cbValue.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.cbUnit.setText(QCoreApplication.translate("MainWindow", u"Unit", None))
        self.cbRange.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Hanwha Aerospace PGM Systems R&D Team4", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

