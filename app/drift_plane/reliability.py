from app.drift_plane.models import ReliabilityRegressionRecord
from typing import Dict

class ReliabilityRegressionManager:
    def __init__(self):
        self.regressions: Dict[str, ReliabilityRegressionRecord] = {}

    def add_regression(self, regression_id: str, regression_type: str):
        self.regressions[regression_id] = ReliabilityRegressionRecord(
            regression_id=regression_id,
            regression_type=regression_type
        )

    def get_regression(self, regression_id: str) -> ReliabilityRegressionRecord:
        return self.regressions.get(regression_id)
