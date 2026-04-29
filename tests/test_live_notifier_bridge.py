import pytest
from unittest.mock import MagicMock
from app.execution.live_runtime.notifier_bridge import LiveNotifierBridge


def test_live_notifier_rate_limits():
    mock_notifier = MagicMock()
    bridge = LiveNotifierBridge(mock_notifier)

    # Send a fill
    bridge.notify_live_fill("r1", "BTCUSDT", "BUY", 1.0, 50000.0, 0.0)
    assert mock_notifier.send_message.call_count == 1

    # Try sending immediately again (should be rate limited)
    bridge.notify_live_fill("r1", "BTCUSDT", "SELL", 0.5, 60000.0, 5000.0)
    assert mock_notifier.send_message.call_count == 1  # Still 1
