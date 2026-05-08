from datetime import datetime
from typing import List
from .models import DataAvailabilityWindow


class AvailabilityEvaluator:
    def evaluate_window(
        self, start: datetime, end: datetime, completeness: float
    ) -> DataAvailabilityWindow:
        return DataAvailabilityWindow(
            window_id=f"win_{start.timestamp()}_{end.timestamp()}",
            start_time=start,
            end_time=end,
            completeness=completeness,
        )
