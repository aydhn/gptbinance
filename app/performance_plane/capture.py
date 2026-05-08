import uuid
from typing import List
from app.performance_plane.models import CaptureRatioRecord


class CaptureAnalyzer:
    @staticmethod
    def calculate_ratio(
        step_name: str,
        initial_opportunity: float,
        captured_value: float,
        degradation_notes: List[str] = None,
    ) -> CaptureRatioRecord:
        ratio = 0.0
        if initial_opportunity > 0:
            ratio = captured_value / initial_opportunity

        return CaptureRatioRecord(
            record_id=str(uuid.uuid4()),
            step_name=step_name,
            ratio=ratio,
            degradation_notes=degradation_notes or [],
        )
