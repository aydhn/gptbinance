from app.drift_plane.models import ComplianceDriftRecord
from typing import Dict

class ComplianceDriftManager:
    def __init__(self):
        self.drifts: Dict[str, ComplianceDriftRecord] = {}

    def add_drift(self, drift_id: str, drift_type: str):
        self.drifts[drift_id] = ComplianceDriftRecord(
            drift_id=drift_id,
            drift_type=drift_type
        )

    def get_drift(self, drift_id: str) -> ComplianceDriftRecord:
        return self.drifts.get(drift_id)
