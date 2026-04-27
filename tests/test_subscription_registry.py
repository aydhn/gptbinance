import pytest
from app.connectors.binance.subscription_registry import SubscriptionRegistry
from app.data.live_stream_models import SubscriptionSpec


def test_subscription_registry():
    registry = SubscriptionRegistry()

    spec1 = SubscriptionSpec(symbol="BTCUSDT", stream_type="kline", interval="1m")
    spec2 = SubscriptionSpec(symbol="BTCUSDT", stream_type="ticker")
    spec3 = SubscriptionSpec(
        symbol="BTCUSDT", stream_type="kline", interval="1m"
    )  # duplicate

    # Add new
    added = registry.add_subscriptions([spec1, spec2])
    assert len(added) == 2
    assert "btcusdt@kline_1m" in added
    assert "btcusdt@ticker" in added

    assert registry.has_subscriptions() is True

    # Try adding duplicate
    added = registry.add_subscriptions([spec3])
    assert len(added) == 0

    # Remove one
    removed = registry.remove_subscriptions([spec1])
    assert len(removed) == 1
    assert "btcusdt@kline_1m" in removed

    # Check active
    active = registry.get_active_streams()
    assert len(active) == 1
    assert active[0] == "btcusdt@ticker"
