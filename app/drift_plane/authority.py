from app.drift_plane.models import AuthorityDriftRecord
from typing import Dict

class AuthorityDriftManager:
    def __init__(self):
        self.drifts: Dict[str, AuthorityDriftRecord] = {}

    def add_drift(self, drift_id: str, drift_type: str):
        self.drifts[drift_id] = AuthorityDriftRecord(
            drift_id=drift_id,
            drift_type=drift_type
        )

    def get_drift(self, drift_id: str) -> AuthorityDriftRecord:
        return self.drifts.get(drift_id)
