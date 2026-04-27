from datetime import datetime, timedelta
from app.strategies.filters import trend_filter, volatility_filter, stale_feature_filter


def test_trend_filter():
    assert trend_filter(1.5, 0.0, True).passed
    assert not trend_filter(-1.5, 0.0, True).passed
    assert trend_filter(-1.5, 0.0, False).passed


def test_volatility_filter():
    assert volatility_filter(1.5, 1.0, 2.0).passed
    assert not volatility_filter(0.5, 1.0, 2.0).passed
    assert not volatility_filter(2.5, 1.0, 2.0).passed


def test_stale_feature_filter():
    now = datetime.utcnow()
    assert stale_feature_filter(now - timedelta(seconds=100), now, 300).passed
    assert not stale_feature_filter(now - timedelta(seconds=400), now, 300).passed
