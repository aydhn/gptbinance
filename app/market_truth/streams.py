from app.market_truth.enums import StreamType


class StreamRegistry:
    def __init__(self):
        self.streams = {}

    def register_stream(
        self, symbol: str, stream_type: StreamType, is_testnet: bool = False
    ):
        key = f"{symbol}_{stream_type.value}_{'testnet' if is_testnet else 'live'}"
        self.streams[key] = {
            "symbol": symbol,
            "stream_type": stream_type,
            "status": "registered",
            "is_testnet": is_testnet,
        }

    def get_stream_status(self, symbol: str, stream_type: StreamType) -> str:
        # Dummy lookup
        return "active"
