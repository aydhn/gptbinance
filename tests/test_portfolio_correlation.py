import pytest
from datetime import datetime, timezone
from app.portfolio.correlation import CorrelationEstimator
from app.portfolio.enums import CorrelationRegime


def test_estimate_correlation():
    estimator = CorrelationEstimator()
    prices = {
        "BTCUSDT": [1.0, 1.1, 1.2],
        "ETHUSDT": [2.0, 2.2, 2.4],
        "SOLBUSD": [5.0, 5.5, 6.0],
    }

    snap = estimator.estimate(prices, datetime.now(timezone.utc))

    assert snap.regime == CorrelationRegime.NORMAL
    assert "USDT_QUOTE" in snap.clusters
    assert "BTCUSDT" in snap.clusters["USDT_QUOTE"]
    assert "ETHUSDT" in snap.clusters["USDT_QUOTE"]
    assert "SOLBUSD" not in snap.clusters["USDT_QUOTE"]

    assert snap.correlations["BTCUSDT"]["ETHUSDT"] == 0.8
