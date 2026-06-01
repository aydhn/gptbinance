from app.drift_plane.models import CapabilityRegressionRecord
from typing import Dict

class CapabilityRegressionManager:
    def __init__(self):
        self.regressions: Dict[str, CapabilityRegressionRecord] = {}

    def add_regression(self, regression_id: str, regression_type: str, capability_id: str):
        self.regressions[regression_id] = CapabilityRegressionRecord(
            regression_id=regression_id,
            regression_type=regression_type,
            capability_id=capability_id
        )

    def get_regression(self, regression_id: str) -> CapabilityRegressionRecord:
        return self.regressions.get(regression_id)
