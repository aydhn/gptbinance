from datetime import datetime
from app.simulation_plane.models import SimulationWindow


class WindowBuilder:
    @staticmethod
    def build_fixed_window(start: datetime, end: datetime) -> SimulationWindow:
        if start >= end:
            raise ValueError("Start time must be before end time")
        return SimulationWindow(
            start_time=start,
            end_time=end,
            window_type="fixed",
            caveats=["Fixed historical window. Does not reflect rolling behavior."],
        )

    @staticmethod
    def build_rolling_window(
        start: datetime, end: datetime, step_days: int
    ) -> SimulationWindow:
        if start >= end:
            raise ValueError("Start time must be before end time")
        return SimulationWindow(
            start_time=start,
            end_time=end,
            window_type="rolling",
            caveats=[
                f"Rolling window with step {step_days} days. May cause overlap anomalies if not partitioned correctly."
            ],
        )
