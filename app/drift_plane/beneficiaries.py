from app.drift_plane.models import BeneficiaryImpactDriftRecord
from typing import Dict

class BeneficiaryImpactDriftManager:
    def __init__(self):
        self.drifts: Dict[str, BeneficiaryImpactDriftRecord] = {}

    def add_drift(self, drift_id: str, drift_type: str):
        self.drifts[drift_id] = BeneficiaryImpactDriftRecord(
            drift_id=drift_id,
            drift_type=drift_type
        )

    def get_drift(self, drift_id: str) -> BeneficiaryImpactDriftRecord:
        return self.drifts.get(drift_id)
