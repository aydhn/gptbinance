from app.drift_plane.models import ControlDriftRecord
from typing import Dict

class ControlDriftManager:
    def __init__(self):
        self.drifts: Dict[str, ControlDriftRecord] = {}

    def add_drift(self, drift_id: str, drift_type: str):
        self.drifts[drift_id] = ControlDriftRecord(
            drift_id=drift_id,
            drift_type=drift_type
        )

    def get_drift(self, drift_id: str) -> ControlDriftRecord:
        return self.drifts.get(drift_id)
