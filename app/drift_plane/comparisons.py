from app.drift_plane.models import DriftComparisonRecord
from typing import Dict

class ComparisonManager:
    def __init__(self):
        self.comparisons: Dict[str, DriftComparisonRecord] = {}

    def add_comparison(self, comparison_id: str, comparison_type: str, result_summary: str):
        self.comparisons[comparison_id] = DriftComparisonRecord(
            comparison_id=comparison_id,
            comparison_type=comparison_type,
            result_summary=result_summary
        )

    def get_comparison(self, comparison_id: str) -> DriftComparisonRecord:
        return self.comparisons.get(comparison_id)
