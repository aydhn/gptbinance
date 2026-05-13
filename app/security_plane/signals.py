from typing import Dict, List, Optional
from app.security_plane.models import SecuritySignalRecord

class SignalBuilder:
    def __init__(self):
        self._signals: Dict[str, SecuritySignalRecord] = {}

    def emit_signal(self, signal: SecuritySignalRecord) -> None:
        self._signals[signal.signal_id] = signal

    def list_signals(self) -> List[SecuritySignalRecord]:
        return list(self._signals.values())
