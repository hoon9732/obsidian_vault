from __future__ import annotations

from collections import deque
from math import ceil, floor, sqrt
from typing import Dict, List, Tuple

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCharts import (
    QChart,
    QChartView,
    QLineSeries,
    QValueAxis,
)
from PySide6.QtWidgets import (
    QGridLayout,
    QMainWindow,
    QWidget,
)

class _RollingSeries:
    MAX_POINTS = 200

    def __init__(self, name: str, colour: Qt.GlobalColor, rng: list):
        self.buffer: deque[Tuple[int, float]] = deque(maxlen=self.MAX_POINTS)
        self.series = QLineSeries(name=name)
        self.series.setColor(colour)

        self.range_lines = []
        if rng:
            # bright yellow, dashed, width 2
            rpen = QPen(QColor(255, 0, 0))
            rpen.setWidth(2)
            rpen.setStyle(Qt.DashLine)

            ypen = QPen(QColor(255, 255, 0))
            ypen.setWidth(2)
            ypen.setStyle(Qt.DashLine)

            low_line = QLineSeries(name=f"LB: {rng[0]}")
            low_line.setPen(rpen)
            low_line.append([QPointF(0, rng[0]), QPointF(self.MAX_POINTS, rng[0])])

            high_line = QLineSeries(name=f"UB: {rng[1]}")
            high_line.setPen(ypen)
            high_line.append([QPointF(0, rng[1]), QPointF(self.MAX_POINTS, rng[1])])

            self.range_lines = [low_line, high_line]

        self.axis_x = QValueAxis()
        self.axis_x.setTitleText("time")
        self.axis_y = QValueAxis()
        # self.axis_y.setTitleText(f"value [{unit}]" if unit else "value")

        self.chart = QChart()
        self.chart.setTheme(QChart.ChartThemeDark)
        self.chart.addSeries(self.series)
        for l in self.range_lines:
            self.chart.addSeries(l)

        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)
        for l in self.range_lines:
            l.attachAxis(self.axis_x)
            l.attachAxis(self.axis_y)

        # legend control
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)   # or any alignment you prefer

        # flash control
        self._normal_brush = self.chart.backgroundBrush()
        self._alert_brush = self._normal_brush  # will set below
        if rng:
            self._alert_brush = Qt.red

        self.rng = rng

    # --------------------------------------------------------------
    def append(self, x: int, y: float) -> None:
        self.buffer.append((x, y))
        self.series.replace([QPointF(a, b) for a, b in self.buffer])

        # move range-lines’ x if buffer scrolled
        if self.range_lines:
            for line in self.range_lines:
                line.replace([QPointF(max(0, x - self.MAX_POINTS), line.at(0).y()),
                               QPointF(x, line.at(0).y())])

        self.axis_x.setRange(max(0, x - self.MAX_POINTS), x or 1)
        ys = [b for _, b in self.buffer]
        if ys:
            ymin, ymax = min(ys), max(ys)
            if ymin == ymax:
                ymax += 1
            self.axis_y.setRange(ymin, ymax)

        # flash background if out of range
        if self.rng and not (self.rng[0] <= y <= self.rng[1]):
            self.chart.setBackgroundBrush(Qt.red)
        else:
            self.chart.setBackgroundBrush(self._normal_brush)


class GraphWindow(QMainWindow):
    """Resizable window with multiple charts laid out nicely."""

    COLOURS = [
        Qt.cyan,
        Qt.yellow,
        Qt.magenta,
        Qt.green,
        Qt.red,
        Qt.white,
        Qt.gray,
        Qt.darkYellow,
        Qt.darkCyan,
    ]

    def __init__(self, sensor_defs: Dict[str, str], parent=None) -> None:
        """
        Parameters
        ----------
        sensor_defs : dict
            Mapping sensor_name -> type  (expects only int/float members here).
        """
        super().__init__(parent)
        self.setWindowTitle("Sensor Graphs")
        self.resize(1080, 900)

        self.sample_idx = 0

        # ---------- build charts ------------------------------------------
        self._series_map: Dict[str, _RollingSeries] = {}

        grid = QGridLayout()
        central = QWidget()
        central.setLayout(grid)
        self.setCentralWidget(central)

        numeric_names = list(sensor_defs.keys())
        if not numeric_names:
            return

        rows, cols = self._layout_for(len(numeric_names))

        for idx, name in enumerate(numeric_names):
            meta = sensor_defs[name] 
            colour = self.COLOURS[idx % len(self.COLOURS)]
            rs = _RollingSeries(name, colour, meta.get("range"))
            self._series_map[name] = rs

            view = QChartView(rs.chart)
            view.setRenderHint(QPainter.Antialiasing, True)
            r, c = divmod(idx, cols)
            grid.addWidget(view, r, c)

        # make all cells stretch evenly
        for c in range(cols):
            grid.setColumnStretch(c, 1)
        for r in range(rows):
            grid.setRowStretch(r, 1)

    # --------------------------------------------------------------
    @staticmethod
    def _layout_for(n: int) -> Tuple[int, int]:
        """Return (rows, cols) for the requested layout rules."""
        return ceil(n % sqrt(n)), ceil(sqrt(n))

    # --------------------------------------------------------------
    def update_from_packet(self, packet: dict) -> None:
        self.sample_idx += 1
        for name, rs in self._series_map.items():
            if name in packet:
                try:
                    rs.append(self.sample_idx, float(packet[name]))
                except (TypeError, ValueError):
                    pass  # skip non-numeric
    
    def clear_all(self):
        """Erase every buffer & repaint axes back to origin."""
        self.sample_idx = 0
        for rs in self._series_map.values():
            rs.buffer.clear()
            rs.series.clear()
        self.repaint()

    def set_new_sensors(self, numeric_meta: dict[str, dict]):
        """Replace the entire chart layout with a new sensor set."""
        self.close()
