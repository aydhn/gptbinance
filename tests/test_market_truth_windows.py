from app.market_truth.windows import ConsistencyWindows, CanaryConsistencyWindows


def test_windows():
    assert ConsistencyWindows.RECONNECT_GRACE_MS == 5000.0
    assert CanaryConsistencyWindows.RECONNECT_GRACE_MS == 2000.0
