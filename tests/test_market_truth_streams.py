from app.market_truth.streams import StreamRegistry
from app.market_truth.enums import StreamType


def test_stream_registration():
    registry = StreamRegistry()
    registry.register_stream("BTCUSDT", StreamType.TRADE)
    assert "BTCUSDT_TRADE_live" in registry.streams
    assert registry.get_stream_status("BTCUSDT", StreamType.TRADE) == "active"
