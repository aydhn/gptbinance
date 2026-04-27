import logging
from datetime import datetime, timezone
from typing import Optional
from threading import Lock

from app.data.live_stream_models import StreamHealthSnapshot, StreamMessageStats

logger = logging.getLogger(__name__)


class WsHealthMonitor:
    """
    Tracks the health of a websocket connection.
    Detects staleness, tracks reconnects, and parsing errors.
    """

    def __init__(self, stale_threshold_seconds: float = 30.0):
        self._lock = Lock()
        self._stale_threshold = stale_threshold_seconds

        self._is_alive = False
        self._reconnect_count = 0
        self._total_received = 0
        self._total_parsed = 0
        self._total_errors = 0
        self._last_message_time: Optional[datetime] = None
        self._last_error: Optional[str] = None

    def mark_connected(self) -> None:
        with self._lock:
            self._is_alive = True

    def mark_disconnected(self) -> None:
        with self._lock:
            self._is_alive = False

    def increment_reconnect(self) -> None:
        with self._lock:
            self._reconnect_count += 1

    def record_message_received(self) -> None:
        with self._lock:
            self._total_received += 1
            self._last_message_time = datetime.now(timezone.utc)

    def record_parse_success(self) -> None:
        with self._lock:
            self._total_parsed += 1

    def record_error(self, error_msg: str) -> None:
        with self._lock:
            self._total_errors += 1
            self._last_error = error_msg

    def is_stale(self) -> bool:
        with self._lock:
            if not self._is_alive or not self._last_message_time:
                return False  # If not alive, it's not "stale", it's disconnected

            delta = (
                datetime.now(timezone.utc) - self._last_message_time
            ).total_seconds()
            return delta > self._stale_threshold

    def get_health_snapshot(self) -> StreamHealthSnapshot:
        with self._lock:
            stats = StreamMessageStats(
                total_received=self._total_received,
                total_parsed=self._total_parsed,
                total_errors=self._total_errors,
                last_message_time=self._last_message_time,
            )

            # Recalculate stale status outside of lock to avoid deadlocks, but using locked values
            is_stale = False
            if self._is_alive and self._last_message_time:
                delta = (
                    datetime.now(timezone.utc) - self._last_message_time
                ).total_seconds()
                is_stale = delta > self._stale_threshold

            return StreamHealthSnapshot(
                is_alive=self._is_alive,
                is_stale=is_stale,
                reconnect_count=self._reconnect_count,
                stats=stats,
                last_error=self._last_error,
            )
