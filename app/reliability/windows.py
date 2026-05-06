from datetime import datetime, timezone, timedelta
from typing import List, Tuple
from app.reliability.models import SLOWindow
from app.reliability.exceptions import ReliabilityTowerError


class WindowEvaluator:
    @staticmethod
    def get_window_range(
        window: SLOWindow, end_time: datetime = None
    ) -> Tuple[datetime, datetime]:
        if end_time is None:
            end_time = datetime.now(timezone.utc)

        start_time = end_time - timedelta(seconds=window.duration_seconds)
        return start_time, end_time

    @staticmethod
    def is_complete(
        window: SLOWindow,
        data_points: List[datetime],
        required_density: float = 0.8,
        end_time: datetime = None,
    ) -> bool:
        """
        Checks if the window has enough data points to be considered complete.
        This is a simplified completeness check.
        """
        if not data_points:
            return False

        start, end = WindowEvaluator.get_window_range(window, end_time)
        points_in_window = [p for p in data_points if start <= p <= end]

        # In a real system, we'd check the interval between points.
        # Here we just ensure we have *some* points to avoid zero-division or invalid conclusions.
        if len(points_in_window) < 1:
            return False

        return True
