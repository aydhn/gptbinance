from datetime import datetime, timezone
from typing import Dict, Any
from app.universe.models import InstrumentRef, TurnoverSnapshot
from app.universe.enums import LiquiditySeverity
from app.universe.exceptions import LiquidityEvaluationError

class TurnoverEvaluator:
    def evaluate(self, ref: InstrumentRef, market_data: Dict[str, Any]) -> TurnoverSnapshot:
        try:
            count = int(market_data.get("count", 0))
            quote_vol = float(market_data.get("quoteVolume", 0))

            if count > 100000:
                severity = LiquiditySeverity.HIGH
            elif count > 20000:
                severity = LiquiditySeverity.MEDIUM
            elif count > 5000:
                severity = LiquiditySeverity.LOW
            else:
                severity = LiquiditySeverity.VERY_LOW

            return TurnoverSnapshot(
                ref=ref,
                turnover_24h=quote_vol,
                trade_count_24h=count,
                severity=severity,
                snapshot_time=datetime.now(timezone.utc)
            )
        except Exception as e:
            raise LiquidityEvaluationError(f"Failed to evaluate turnover: {e}")
