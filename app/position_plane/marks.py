from decimal import Decimal
from typing import Tuple


class MarkSourceEngine:
    @staticmethod
    def get_trusted_mark(
        symbol: str, current_time: float, last_update_time: float, price: Decimal
    ) -> Tuple[Decimal, float, str]:
        staleness = current_time - last_update_time
        confidence = 1.0

        if staleness > 60:
            confidence = max(0.0, 1.0 - (staleness - 60) / 300)

        return price, confidence, "binance_ticker"
