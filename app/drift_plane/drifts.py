from app.drift_plane.models import DriftRecord
from typing import Dict, List

class DriftManager:
    def __init__(self):
        self.drifts: Dict[str, DriftRecord] = {}

    def add_drift(self, drift_id: str, lifecycle_state: str, proof_notes: List[str] = None, lineage_refs: List[str] = None):
        self.drifts[drift_id] = DriftRecord(
            drift_id=drift_id,
            lifecycle_state=lifecycle_state,
            proof_notes=proof_notes or [],
            lineage_refs=lineage_refs or []
        )

    def get_drift(self, drift_id: str) -> DriftRecord:
        return self.drifts.get(drift_id)
