from app.drift_plane.models import MetricErosionRecord
from typing import Dict

class ErosionManager:
    def __init__(self):
        self.erosions: Dict[str, MetricErosionRecord] = {}

    def add_erosion(self, erosion_id: str, erosion_type: str, metric_name: str):
        self.erosions[erosion_id] = MetricErosionRecord(
            erosion_id=erosion_id,
            erosion_type=erosion_type,
            metric_name=metric_name
        )

    def get_erosion(self, erosion_id: str) -> MetricErosionRecord:
        return self.erosions.get(erosion_id)
