"""Session health monitoring."""
from datetime import datetime
from .models import SessionHealth, SessionHealthSnapshot
from app.observability.metrics import registry as metric_registry
from app.observability.enums import ComponentType


class HealthMonitor:
    def __init__(self):
        self.start_time = datetime.utcnow()
        self.error_count = 0
        self.last_error = None
        self.stream_timestamps = {}
        self.feature_lag = 0.0
        self.max_drawdown = 0.0

    def record_error(self, err: str):
        self.error_count += 1
        self.last_error = err
        try:
            metric_registry.record("paper_execution_error", 1.0, tags={"error": err[:20]})
        except Exception:
            pass

    def record_stream_event(self, symbol: str, event_time_ms: int):
        self.stream_timestamps[symbol] = event_time_ms

    def get_snapshot(
        self, current_drawdown: float, open_positions_count: int
    ) -> SessionHealthSnapshot:
        now = datetime.utcnow()
        uptime = (now - self.start_time).total_seconds()

        # Calculate stream freshness (lag)
        now_ms = int(now.timestamp() * 1000)
        max_lag_ms = 0
        for ts in self.stream_timestamps.values():
            lag = now_ms - ts
            if lag > max_lag_ms:
                max_lag_ms = lag

        health = SessionHealth.HEALTHY
        if self.error_count > 10 or max_lag_ms > 5000:
            health = SessionHealth.DEGRADED
        if self.error_count > 50 or max_lag_ms > 30000:
            health = SessionHealth.CRITICAL

        self.max_drawdown = max(self.max_drawdown, current_drawdown)
        if self.max_drawdown > 0.10:  # 10% drawdown
            health = SessionHealth.CRITICAL

        return SessionHealthSnapshot(
            health=health,
            uptime_seconds=uptime,
            stream_freshness_ms=max_lag_ms,
            feature_lag_ms=self.feature_lag,
            error_count=self.error_count,
            open_positions=open_positions_count,
            current_drawdown_pct=current_drawdown,
            last_error=self.last_error,
        )
