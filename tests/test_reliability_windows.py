from datetime import datetime, timezone, timedelta
from app.reliability.windows import WindowEvaluator
from app.reliability.models import SLOWindow


def test_window_rolling_logic():
    window = SLOWindow(window_id="w1", duration_seconds=3600)
    end = datetime(2025, 5, 5, 12, 0, tzinfo=timezone.utc)
    start, e = WindowEvaluator.get_window_range(window, end)

    assert start == datetime(2025, 5, 5, 11, 0, tzinfo=timezone.utc)
    assert e == end

    data_points = [datetime(2025, 5, 5, 11, 30, tzinfo=timezone.utc)]

    assert WindowEvaluator.is_complete(window, data_points, end_time=end) == True
    assert WindowEvaluator.is_complete(window, []) == False
