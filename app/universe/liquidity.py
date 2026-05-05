from datetime import datetime, timezone
from typing import Dict, Any
from app.universe.base import LiquidityScorer
from app.universe.models import (
    InstrumentRef,
    LiquiditySnapshot,
    SpreadSnapshot,
    TurnoverSnapshot,
)
from app.universe.enums import LiquiditySeverity, SpreadSeverity
from app.universe.exceptions import LiquidityEvaluationError


class SimpleLiquidityScorer(LiquidityScorer):
    """
    Evaluates liquidity based on coarse 24h ticker data.
    """

    def score_liquidity(
        self, ref: InstrumentRef, market_data: Dict[str, Any]
    ) -> LiquiditySnapshot:
        try:
            quote_vol = float(market_data.get("quoteVolume", 0))
            volume = float(market_data.get("volume", 0))

            # Very simple thresholds
            if quote_vol > 50_000_000:
                severity = LiquiditySeverity.HIGH
            elif quote_vol > 10_000_000:
                severity = LiquiditySeverity.MEDIUM
            elif quote_vol > 1_000_000:
                severity = LiquiditySeverity.LOW
            else:
                severity = LiquiditySeverity.VERY_LOW

            return LiquiditySnapshot(
                ref=ref,
                rolling_volume=volume,
                quote_volume=quote_vol,
                activity_score=quote_vol / 1_000_000,  # basic normalization
                severity=severity,
                snapshot_time=datetime.now(timezone.utc),
            )
        except Exception as e:
            raise LiquidityEvaluationError(f"Failed to score liquidity: {e}")

    def score_spread(
        self, ref: InstrumentRef, market_data: Dict[str, Any]
    ) -> SpreadSnapshot:
        try:
            bid = float(market_data.get("bidPrice", 0))
            ask = float(market_data.get("askPrice", 0))

            if bid == 0 or ask == 0:
                spread_val = 0
                rel_spread = 0
                severity = SpreadSeverity.UNKNOWN
            else:
                spread_val = ask - bid
                rel_spread = spread_val / ((ask + bid) / 2)

                if rel_spread < 0.0005:  # 5 bps
                    severity = SpreadSeverity.TIGHT
                elif rel_spread < 0.0020:  # 20 bps
                    severity = SpreadSeverity.NORMAL
                elif rel_spread < 0.0050:  # 50 bps
                    severity = SpreadSeverity.WIDE
                else:
                    severity = SpreadSeverity.VERY_WIDE

            return SpreadSnapshot(
                ref=ref,
                bid_ask_spread=spread_val,
                relative_spread=rel_spread,
                severity=severity,
                snapshot_time=datetime.now(timezone.utc),
            )
        except Exception as e:
            raise LiquidityEvaluationError(f"Failed to score spread: {e}")
