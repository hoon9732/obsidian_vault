# modules/socket_client.py

from __future__ import annotations

import json
import socket
from typing import Dict, Optional

from PySide6.QtCore import QThread, Signal

class SensorClient(QThread):
    """A QThread that receives JSON sensor data from a TCP server."""

    data_received: Signal = Signal(dict)

    def __init__(self, host: str = "127.0.0.1", port: int = 9999,
                 parent: Optional[object] = None) -> None:
        super().__init__(parent)
        self.host: str = host
        self.port: int = port
        self._running: bool = True

    def run(self) -> None:
        """Connect to the server and emit data as JSON objects are received."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.host, self.port))
                buffer = ""
                while self._running:
                    chunk = sock.recv(1024)
                    if not chunk:
                        break
                    try:
                        buffer += chunk.decode("utf‑8")
                    except UnicodeDecodeError:
                        continue
                    while "\n" in buffer:
                        line, buffer = buffer.split("\n", 1)
                        if not line:
                            continue
                        try:
                            data: Dict[str, object] = json.loads(line)
                            if isinstance(data, dict):
                                self.data_received.emit(data)
                        except json.JSONDecodeError:
                            continue
        except (ConnectionRefusedError, OSError) as exc:
            print(f"SensorClient: unable to connect to {self.host}:{self.port} ({exc})")

    def stop(self) -> None:
        """Request the thread to terminate."""
        self._running = False
