# MAIN IMPORT
from PySide6.QtWidgets import QWidget, QFrame  # whatever you actually need
from .ui_main        import Ui_MainWindow
from .app_settings   import Settings

# WITH ACCESS TO MAIN WINDOW WIDGETS
class AppFunctions:
    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #745449;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #745449;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 198, 121, 255), stop:0.5 rgba(255, 170, 85, 0));
        background-color: #886356;
        """

        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #a47262;")
        self.ui.pushButton.setStyleSheet("background-color: #a47262;")
        self.ui.plainTextEdit.setStyleSheet("background-color: #a47262;")
        self.ui.tableWidget.setStyleSheet("QScrollBar:vertical { background: #a47262; } QScrollBar:horizontal { background: #a47262; }")
        self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: #a47262; } QScrollBar:horizontal { background: #a47262; }")
        self.ui.comboBox.setStyleSheet("background-color: #a47262;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #a47262;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #a47262;")
        self.ui.commandLinkButton.setStyleSheet("color: #ffc679;")
