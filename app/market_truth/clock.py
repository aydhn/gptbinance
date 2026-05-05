import time
from datetime import datetime, timezone
from app.market_truth.models import MarketClockSnapshot
from app.market_truth.exceptions import ClockDriftError


class CanonicalMarketClock:
    def __init__(self, max_allowed_drift_ms: float = 5000.0):
        self.max_allowed_drift_ms = max_allowed_drift_ms
        self._last_snapshot: MarketClockSnapshot | None = None

    def capture_snapshot(self, exchange_time: datetime) -> MarketClockSnapshot:
        local_wall = datetime.now(timezone.utc)
        local_mono = time.monotonic()

        drift = abs((local_wall - exchange_time).total_seconds() * 1000)

        if drift > self.max_allowed_drift_ms:
            raise ClockDriftError(
                f"Clock drift {drift}ms exceeds max {self.max_allowed_drift_ms}ms"
            )

        snapshot = MarketClockSnapshot(
            exchange_time=exchange_time,
            local_wall_time=local_wall,
            local_monotonic_time=local_mono,
            processing_lag_ms=0.0,  # Will be updated during event processing
            drift_ms=drift,
        )
        self._last_snapshot = snapshot
        return snapshot
