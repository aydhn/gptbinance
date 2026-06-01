from app.drift_plane.models import DriftSignalRecord
from app.drift_plane.enums import SignalClass
from typing import Dict
from datetime import datetime

class SignalManager:
    def __init__(self):
        self.signals: Dict[str, DriftSignalRecord] = {}

    def add_signal(self, signal_id: str, class_type: SignalClass, source: str):
        self.signals[signal_id] = DriftSignalRecord(
            signal_id=signal_id,
            class_type=class_type,
            detected_at=datetime.utcnow(),
            source=source
        )

    def get_signal(self, signal_id: str) -> DriftSignalRecord:
        return self.signals.get(signal_id)
