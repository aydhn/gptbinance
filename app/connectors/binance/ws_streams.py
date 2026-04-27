from app.data.live_stream_models import SubscriptionSpec


def get_kline_stream_name(symbol: str, interval: str) -> str:
    """Returns the stream name for kline updates."""
    return f"{symbol.lower()}@kline_{interval}"


def get_ticker_stream_name(symbol: str) -> str:
    """Returns the stream name for 24hr ticker updates."""
    return f"{symbol.lower()}@ticker"


def get_book_ticker_stream_name(symbol: str) -> str:
    """Returns the stream name for book ticker updates."""
    return f"{symbol.lower()}@bookTicker"


def get_stream_name(spec: SubscriptionSpec) -> str:
    """Returns the formatted stream name based on the specification."""
    return spec.stream_name
