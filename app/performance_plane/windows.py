from datetime import datetime, timezone
from app.performance_plane.models import PerformanceWindow
from app.performance_plane.enums import WindowClass


class WindowManager:
    @staticmethod
    def create_window(
        window_class: WindowClass,
        start_time: datetime,
        end_time: Optional[datetime] = None,
    ) -> PerformanceWindow:
        caveats = []
        is_complete = end_time is not None

        if not is_complete:
            caveats.append("Partial window: end_time not reached.")

        if start_time.tzinfo is None:
            raise ValueError("start_time must be timezone aware")

        return PerformanceWindow(
            window_class=window_class,
            start_time=start_time,
            end_time=end_time,
            is_complete=is_complete,
            caveats=caveats,
        )
