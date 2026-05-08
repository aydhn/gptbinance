from typing import Dict, Any, List
from app.performance_plane.models import PerformanceWindow


class ActivationHistory:
    @staticmethod
    def record_stage_activation(
        stage_id: str, stage_name: str, performance_window: PerformanceWindow = None
    ) -> dict:
        record = {"stage_id": stage_id, "stage_name": stage_name, "status": "activated"}
        if performance_window:
            record["window_start"] = performance_window.start_time.isoformat()
            if performance_window.end_time:
                record["window_end"] = performance_window.end_time.isoformat()

        return record
