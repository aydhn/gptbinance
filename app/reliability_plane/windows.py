from datetime import datetime
from typing import Dict, List, Optional

from .models import ReliabilityWindow


class WindowManager:
    def __init__(self):
        self._windows: Dict[str, ReliabilityWindow] = {}

    def register_window(self, window: ReliabilityWindow) -> None:
        self._windows[window.window_id] = window

    def get_window(self, window_id: str) -> Optional[ReliabilityWindow]:
        return self._windows.get(window_id)

    def list_windows(self) -> List[ReliabilityWindow]:
        return list(self._windows.values())

    def get_active_windows(self, current_time: datetime) -> List[ReliabilityWindow]:
        active = []
        for w in self._windows.values():
            if w.start_time <= current_time and (
                w.end_time is None or w.end_time >= current_time
            ):
                active.append(w)
        return active
