import pytest
from datetime import datetime, timezone
from app.market_truth.clock import CanonicalMarketClock
from app.market_truth.exceptions import ClockDriftError


def test_canonical_clock_drift():
    clock = CanonicalMarketClock(max_allowed_drift_ms=1000.0)
    # 5 seconds in the past
    exchange_time = datetime.fromtimestamp(
        datetime.now(timezone.utc).timestamp() - 5, timezone.utc
    )
    with pytest.raises(ClockDriftError):
        clock.capture_snapshot(exchange_time)
