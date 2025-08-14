# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0

# BASIC IMPORT
import sys
import os
import platform
import json, pathlib, time # new

# IMPORT GUI AND MODULES AND WIDGETS
from PySide6.QtCore import Qt, QEvent, QTimer, QSettings # new
from PySide6.QtGui import QIcon, QPixmap, QColor, QBrush  # 2 new
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHeaderView,
    QTableWidgetItem,
    QFileDialog # new
)    

# HIGH DPI FIX
os.environ["QT_FONT_DPI"] = "96"

from modules.ui_main import Ui_MainWindow
from modules.app_settings import Settings
from modules.ui_functions import UIFunctions
from modules.app_functions import AppFunctions
from modules.tcp_client import SensorClient
from modules.graph_window import GraphWindow
from modules.gl_viewer import GLViewerWindow

# SET AS GLOBAL WIDGETS
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = QSettings("MyCompany", "MissileGUI")

        # STREAMING STATE
        self.sensor_client: SensorClient | None = None
        self.graph_win: GraphWindow | None = None
        self.streaming = False           # False = paused
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        title = "GPMTS 1.0.0"
        description = ""

        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.missile_1.clicked.connect(self.buttonClick)
        widgets.missile_2.clicked.connect(self.buttonClick)
        widgets.toggleLeftBox.clicked.connect(self.buttonClick)
        widgets.btn_browse.clicked.connect(self.browse_json_for_current_tab)
        widgets.btn_start.clicked.connect(self.toggle_stream)
        widgets.btn_graph.clicked.connect(self.open_graph_window)
        widgets.btn_testing.clicked.connect(self.buttonClick)
        widgets.btn_open_gl.clicked.connect(self.buttonClick)
        widgets.btn_siteview.clicked.connect(self.open_gl_window)
        widgets.btn_testlaunch.clicked.connect(self.buttonClick)
        widgets.btn_abortlaunch.clicked.connect(self.buttonClick)
        widgets.btn_report.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)
        widgets.btn_settings.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SENSOR CLIENT
        self.sensor_client = SensorClient(host="127.0.0.1", port=9999, parent=self)
        self.sensor_client.data_received.connect(self.update_sensor_table)
        self.sensor_client.start()

        # TAB MANAGEMENT
        self.tab_count = widgets.tabWidget.count()
        self.table_map = {}

        # SENSOR LIST
        self.active_sensors = []          # list[str]
        self.last_seen = {}               # sensor → last timestamp
        self.sensor_lists = {}
        self.sensor_meta = {}
        self.last_json_paths = {}        
        
        # BUILD FIXED TABLE_MAP
        for i in range(self.tab_count):
            tbl_name = f"sensorTable_{i+10}"
            self.table_map[i] = getattr(widgets, tbl_name)

            key = f"tab/{i}/lastJson"
            path = self.settings.value(key, "", type=str)
            if path and os.path.isfile(path):
                self.last_json_paths[i] = path
                self.sensor_lists[i] = self._load_json_return_sensor_names(path)
                self._populate_table_structure(i)
        
        # BUILD TABLE_MAP
        for i in range(self.tab_count):
            tbl_name = "sensorTable" if i == 0 else f"sensorTable_{i+1}"
            self.table_map[i] = getattr(widgets, tbl_name)

            key = f"tab/{i}/lastJson"
            path = self.settings.value(key, "", type=str)
            if path and os.path.isfile(path):
                self.last_json_paths[i] = path
                self.sensor_lists[i] = self._load_json_return_sensor_names(path)
                self._populate_table_structure(i)
        

        # GRAPH STATE
        def _on_tab_changed(idx: int):
            # Save lastTab as before
            self.setting.setValue("lastTab", idx)
            # Reset graph if it exists and is visible
            if getattr(self, "graph_win", None) and self.graph_win.isVisible():
                self.open_graph_window()
            widgets.tabWidget.currentChanged.connect(_on_tab_changed)
    
        # SHOW APP
        self._restore_checkboxes()
        self._restore_last_tab()
        self.show()

        # CHECKBOX
        for cb, col in (
                (widgets.cbConnection, 1),
                (widgets.cbApproval, 2),
                (widgets.cbValue, 3),
                (widgets.cbUnit, 4),
                (widgets.cbRange, 5),
        ):
            cb.toggled.connect(lambda checked, c=col: self.hide_show_column(c, checked))


        # SET CUSTOM THEME
        useCustomTheme = True
        #themeFile = "themes\hanwha_light.qss"
        themeFile = "themes\hanwha_dark.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
    '''
    # UPDATE FIXED SENSOR TABLE
    def update_fixed_sensor_table(self, packet: dict):
        for idx, sensors in self.sensor_lists.items():
            tbl = self.table_map[idx+10]
            now = time.time()
            for row, name in enumerate(sensors):
                if name not in packet:
                    continue
                self.last_seen[name] = now
                rng_low, rng_high = None, None
                rng_txt = tbl.item(row, 5).text()
                if rng_txt.strip() not in ("—", ""):
                    try:
                        rng_low, rng_high = eval(rng_txt)  # simple [low, high]
                    except (SyntaxError, ValueError):
                        continue
                
                value = packet[name]
                isok = "OK" if (rng_low is None or rng_low <= value <= rng_high) else "NG"

                tbl.setItem(row, 1, QTableWidgetItem("Connected"))        # connection status
                tbl.setItem(row, 3, QTableWidgetItem(str(round(value, 2))))  # live value

                item_approval = QTableWidgetItem(isok)
                if isok == "OK":
                    item_approval.setForeground(QBrush(QColor(0, 255, 0)))
                elif isok == "NG":
                    item_approval.setForeground(QBrush(QColor(255, 0, 0)))
                else:
                    item_approval.setForeground(QBrush(QColor(255, 255, 255)))
                tbl.setItem(row, 2, item_approval)
    '''
    # UPDATE SENSOR TABLE
    def update_sensor_table(self, packet: dict):
        for idx, sensors in self.sensor_lists.items():
            tbl = self.table_map[idx]
            now = time.time()
            for row, name in enumerate(sensors):
                if name not in packet:
                    continue
                self.last_seen[name] = now
                rng_low, rng_high = None, None
                rng_txt = tbl.item(row, 5).text()
                if rng_txt.strip() not in ("—", ""):
                    try:
                        rng_low, rng_high = eval(rng_txt)  # simple [low, high]
                    except (SyntaxError, ValueError):
                        continue
                
                value = packet[name]
                isok = "OK" if (rng_low is None or rng_low <= value <= rng_high) else "NG"

                tbl.setItem(row, 1, QTableWidgetItem("Connected"))        # connection status
                tbl.setItem(row, 3, QTableWidgetItem(str(round(value, 2))))  # live value

                item_approval = QTableWidgetItem(isok)
                if isok == "OK":
                    item_approval.setForeground(QBrush(QColor(0, 255, 0)))
                elif isok == "NG":
                    item_approval.setForeground(QBrush(QColor(255, 0, 0)))
                else:
                    item_approval.setForeground(QBrush(QColor(255, 255, 255)))
                tbl.setItem(row, 2, item_approval)

    def closeEvent(self, event):
        if self.sensor_client and self.sensor_client.isRunning():
            self.sensor_client.stop()
            self.sensor_client.wait()
        event.accept()

    # BROWSE FILES
    def browse_json_for_current_tab(self):
        idx = widgets.tabWidget.currentIndex()
        path, _ = QFileDialog.getOpenFileName(
            self, "Select sensor JSON", "", "JSON (*.json)"
        )
        if not path:
            return
        self.last_json_paths[idx] = path
        self.settings.setValue(f"tab/{idx}/lastJson", path)
        self.sensor_lists[idx] = self._load_json_return_sensor_names(path)
        self._populate_table_structure(idx)
        if getattr(self, "graph_win", None) and self.graph_win.isVisible():
            self.open_graph_window()

    def load_sensor_list(self, path: str) -> None:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.active_sensors = [s["name"] for s in data["sensors"]]
            self.sensor_meta = {s["name"]: s for s in data["sensors"]}
            ranges = {s["name"]: s.get("range") for s in data["sensors"]}
        except Exception as e:
            print(f"Failed to load {path}: {e}")
            return

        tbl = widgets.sensorTable
        tbl.setRowCount(len(self.active_sensors))
        hdrs = ["Sensor", "Connection", "Range", "Value", "Approval"]
        tbl.setColumnCount(len(hdrs))
        tbl.setHorizontalHeaderLabels(hdrs)

        for row, name in enumerate(self.active_sensors):
            tbl.setItem(row, 0, QTableWidgetItem(name))
            rng = ranges.get(name)
            tbl.setItem(row, 1, QTableWidgetItem(str(rng) if rng else "—"))

        tbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # COLUMN LIST
    def hide_show_column(self, column: int, checked: bool) -> None:
        """Hide / show the same column in every sensorTable."""
        for tbl in self.table_map.values():
            tbl.setColumnHidden(column, not checked)

        # remember in QSettings
        key_map = {1:"col/connection", 2:"col/approval", 3:"col/value", 4:"col/unit", 5:"col/range"}
        if column in key_map:
            self.settings.setValue(key_map[column], checked)

    # LOAD PRESET HELPERS(LAST OPENED JSON)
    def _last_json_path(self) -> str | None:
        idx = widgets.tabWidget.currentIndex()
        return self.last_json_paths.get(idx)
    
    def _restore_checkboxes(self) -> None:
        for cb, key in (
            (widgets.cbConnection, "col/connection"),
            (widgets.cbApproval, "col/approval"),
            (widgets.cbValue, "col/value"),
            (widgets.cbUnit, "col/unit"),
            (widgets.cbRange, "col/range")
        ):
            state = self.settings.value(key, True, type=bool)
            cb.blockSignals(True)        # avoid triggering hide/show during startup
            cb.setChecked(state)
            cb.blockSignals(False)
            self.hide_show_column({widgets.cbConnection:1, widgets.cbApproval:2,
                                   widgets.cbValue:3, widgets.cbUnit:4,
                                   widgets.cbRange:5}[cb], state)

    def _restore_last_tab(self) -> None:
        idx = self.settings.value("lastTab", 0, type=int)
        if hasattr(widgets, "tabWidget"):
            widgets.tabWidget.setCurrentIndex(idx)

    def _load_json_return_sensor_names(self, path: str) -> list[str]:
        try:
            with open(path, "r", encoding = "utf-8") as f:
                obj = json.load(f)
            for s in obj["sensors"]:
                self.sensor_meta[s["name"]] = s
            return [s["name"] for s in obj["sensors"]]
        except Exception as exc:
            print(f"JSON load error {path}: {exc}")
            return []
        
    def _populate_table_structure(self, tab_idx:int) -> None:
        sensors = self.sensor_lists.get(tab_idx, [])
        tbl = self.table_map[tab_idx]
        tbl.setRowCount(len(sensors))
        hdrs = ["Sensor", "Connection", "Approval", "Value", "Unit", "Range"]
        tbl.setColumnCount(len(hdrs))
        tbl.setHorizontalHeaderLabels(hdrs)
        
        for row, name in enumerate(sensors):
            tbl.setItem(row, 0, QTableWidgetItem(name))
            tbl.setItem(row, 1, QTableWidgetItem(""))
            tbl.setItem(row, 2, QTableWidgetItem(""))
            tbl.setItem(row, 3, QTableWidgetItem(""))
            unit = self.sensor_meta[name].get("unit", "-")
            tbl.setItem(row, 4, QTableWidgetItem(unit))
            rng = self.sensor_meta[name].get("range")
            rng_txt = "-" if rng is None else f"[{rng[0]}, {rng[1]}]"
            tbl.setItem(row, 5, QTableWidgetItem(rng_txt))
            
        tbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # BUTTONS TOGGLE
    def toggle_stream(self) -> None:
        """Start or pause receiving sensor data."""
        if not self.streaming:
            # SWITCH TO START
            json_path = self._last_json_path()
            if json_path is None:
                print("No JSON loaded. load one first.")
                return
            if not self.active_sensors:          # table not built yet
                self.load_sensor_list(json_path)

            # (re)create the thread each start to simplify logic
            if self.sensor_client and self.sensor_client.isRunning():
                self.sensor_client.stop()
                self.sensor_client.wait()

            self.sensor_client = SensorClient(host="127.0.0.1", port=9999, parent=self)
            self.sensor_client.data_received.connect(self.update_sensor_table)
            self.sensor_client.start()

            self.streaming = True
            widgets.btn_start.setText("Pause")
            widgets.btn_start.setStyleSheet("background-image: url(:/icons/images/icons/cil-media-pause.png);")
        else:
            # ---- switching to PAUSE -----------------------------------------
            if self.sensor_client and self.sensor_client.isRunning():
                self.sensor_client.stop()
                self.sensor_client.wait()
            self.streaming = False
            widgets.btn_start.setText("Start")
            widgets.btn_start.setStyleSheet("background-image: url(:/icons/images/icons/cil-media-play.png);")

    # GRAPH WINDOW
    def open_graph_window(self) -> None:
        """Show graph for the current tab's numeric sensors(auto-restart safe)."""
        idx = widgets.tabWidget.currentIndex()
        if idx not in self.sensor_lists:
            print("Load a JSON first.")
            return

        # filter to numeric types
        numeric_meta = {
            name: self.sensor_meta[name]
            for name in self.sensor_lists[idx]
            if self.sensor_meta[name]["type"] in ("int", "float")
        }
        if not numeric_meta:
            print("No numeric sensors to plot.")
            return

        """If a graph window already exists but it is based on other sensors, close it."""
        if self.graph_win and self.graph_win.isVisible():
            self.sensor_client.data_received.disconnect(self.graph_win.update_from_packet)
            self.graph_win.close()
            self.graph_win = None
        
        from modules.graph_window import GraphWindow
        self.graph_win = GraphWindow(numeric_meta, parent=self)
        self.sensor_client.data_received.connect(self.graph_win.update_from_packet)
        self.graph_win.destroyed.connect(lambda _: setattr(self, "graph_win", None))
        self.graph_win.show()

    def open_graph_window_2(self) -> None:
        """Show graph for the current tab's numeric sensors(auto-restart safe)."""
        idx = widgets.tabWidget.currentIndex()
        if idx not in self.sensor_lists:
            print("Load a JSON first.")
            return

        # filter to numeric types
        numeric_meta = {
            name: self.sensor_meta[name]
            for name in self.sensor_lists[idx]
            if self.sensor_meta[name]["type"] in ("int", "float")
        }
        if not numeric_meta:
            print("No numeric sensors to plot.")
            return

        """If a graph window already exists but it is based on other sensors, close it."""
        if self.graph_win and self.graph_win.isVisible():
            self.sensor_client.data_received.disconnect(self.graph_win.update_from_packet)
            self.graph_win.close()
            self.graph_win = None
        
        from modules.graph_window import GraphWindow
        self.graph_win = GraphWindow(numeric_meta, parent=self)
        self.sensor_client.data_received.connect(self.graph_win.update_from_packet)
        self.graph_win.destroyed.connect(lambda _: setattr(self, "graph_win", None))
        self.graph_win.show()

    # OPENGL WINDOW
    '''def open_gl_window(self):
        if getattr(self, "_gl_win", None) is None:
            self._gl_win = GLViewerWindow(self)
            # forward telemetry into existing table slot
            self._gl_win.telemetry.connect(self.update_sensor_table)
            self._gl_win.destroyed.connect(lambda _:
                                            setattr(self, "_gl_win", None))
        self._gl_win.show()
        self._gl_win.raise_()'''
    def open_gl_window(self):
        if getattr(self, "_gl_win", None) is None:
            from modules.gl_viewer import GLViewerWindow
            self._gl_win = GLViewerWindow(parent=self)
            # connect rocket telemetry → update table
            self._gl_win.telemetry.connect(self.update_sensor_table)
            self._gl_win.destroyed.connect(lambda _: setattr(self, "_gl_win", None))
        self._gl_win.show()

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW toggleLeftBox PAGE
        if btnName == "toggleLeftBox":
            widgets.stackedWidget.setCurrentWidget(widgets.monitor) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        # SHOW TESTING PAGE
        if btnName == "btn_testing":
            widgets.stackedWidget.setCurrentWidget(widgets.testing)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW RENDERING PAGE
        if btnName == "btn_open_gl":
            widgets.stackedWidget.setCurrentWidget(widgets.open_gl)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW REPORTS PAGE
        if btnName == "btn_report":
            widgets.stackedWidget.setCurrentWidget(widgets.report)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW SETTINGS PAGE
        if btnName == "btn_settings":
            widgets.stackedWidget.setCurrentWidget(widgets.settings)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_exit":
            print("Exit BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
