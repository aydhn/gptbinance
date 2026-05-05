from app.market_truth.models import SymbolFeedHealth
from app.market_truth.enums import StreamType
from datetime import datetime, timezone


class SymbolHealthAggregator:
    def aggregate(self, symbol: str, stream_healths: list) -> SymbolFeedHealth:
        # Simplistic aggregation
        is_all_healthy = all(h.get("is_healthy", False) for h in stream_healths)
        return SymbolFeedHealth(
            symbol=symbol,
            stream_type=StreamType.TRADE,  # representative
            is_healthy=is_all_healthy,
            last_update_local=datetime.now(timezone.utc),
            last_update_exchange=datetime.now(timezone.utc),
        )
