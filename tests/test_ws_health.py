import pytest
from datetime import datetime, timezone, timedelta
from unittest.mock import patch
from app.connectors.binance.ws_health import WsHealthMonitor


def test_ws_health_stale_detection():
    # Set threshold low for testing
    monitor = WsHealthMonitor(stale_threshold_seconds=1.0)

    # Not alive, shouldn't be stale
    assert not monitor.is_stale()

    monitor.mark_connected()
    monitor.record_message_received()

    # Just received, not stale
    assert not monitor.is_stale()

    # Mock time to be 2 seconds in the future
    with patch("app.connectors.binance.ws_health.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime.now(timezone.utc) + timedelta(
            seconds=2
        )
        assert monitor.is_stale()


def test_ws_health_counters():
    monitor = WsHealthMonitor()

    monitor.mark_connected()
    monitor.increment_reconnect()
    monitor.increment_reconnect()
    monitor.record_message_received()
    monitor.record_parse_success()
    monitor.record_error("Bad json")

    snap = monitor.get_health_snapshot()

    assert snap.is_alive is True
    assert snap.reconnect_count == 2
    assert snap.stats.total_received == 1
    assert snap.stats.total_parsed == 1
    assert snap.stats.total_errors == 1
    assert snap.last_error == "Bad json"
