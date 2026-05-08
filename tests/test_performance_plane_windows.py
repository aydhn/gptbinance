from datetime import datetime, timezone
import pytest
from app.performance_plane.windows import WindowManager
from app.performance_plane.enums import WindowClass


def test_window_completeness():
    start_time = datetime(2024, 1, 1, tzinfo=timezone.utc)
    # Partial window
    w1 = WindowManager.create_window(WindowClass.SESSION, start_time)
    assert not w1.is_complete
    assert len(w1.caveats) > 0

    # Complete window
    w2 = WindowManager.create_window(
        WindowClass.SESSION, start_time, datetime(2024, 1, 2, tzinfo=timezone.utc)
    )
    assert w2.is_complete
    assert len(w2.caveats) == 0


def test_window_timezone_enforcement():
    start_time = datetime(2024, 1, 1)  # Naive
    with pytest.raises(ValueError):
        WindowManager.create_window(WindowClass.DAILY, start_time)
