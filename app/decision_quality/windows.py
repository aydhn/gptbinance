from datetime import datetime, timedelta
from typing import Optional
from .enums import OutcomeWindow
from .models import DecisionOutcomeWindow


class WindowManager:
    """
    Manages the calculation of outcome windows based on context.
    """

    def calculate_window(
        self,
        base_time: datetime,
        window_type: OutcomeWindow,
        regime_end: Optional[datetime] = None,
        session_end: Optional[datetime] = None,
    ) -> DecisionOutcomeWindow:
        """
        Calculates the exact start and end times for a given window type.
        """
        start_time = base_time
        end_time = base_time

        if window_type == OutcomeWindow.VERY_SHORT:
            end_time = base_time + timedelta(minutes=5)
        elif window_type == OutcomeWindow.SHORT:
            end_time = base_time + timedelta(hours=1)
        elif window_type == OutcomeWindow.MEDIUM:
            end_time = base_time + timedelta(days=1)
        elif window_type == OutcomeWindow.SESSION_BOUND:
            if not session_end:
                raise ValueError("Session end time required for SESSION_BOUND window")
            end_time = session_end
        elif window_type == OutcomeWindow.REGIME_BOUND:
            if not regime_end:
                raise ValueError("Regime end time required for REGIME_BOUND window")
            end_time = regime_end

        return DecisionOutcomeWindow(
            window_type=window_type, start_time=start_time, end_time=end_time
        )
