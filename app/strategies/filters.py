from typing import Dict, Any
from datetime import datetime
from app.strategies.models import StrategyRationale
from app.strategies.enums import RationaleCategory


class FilterResult:
    def __init__(
        self, passed: bool, reason: str, supporting_values: Dict[str, Any] = None
    ):
        self.passed = passed
        self.reason = reason
        self.supporting_values = supporting_values or {}

    def to_rationale(self) -> StrategyRationale:
        category = (
            RationaleCategory.FILTER_PASS
            if self.passed
            else RationaleCategory.FILTER_FAIL
        )
        return StrategyRationale(
            category=category,
            reason=self.reason,
            supporting_values=self.supporting_values,
        )


def trend_filter(
    trend_indicator: float, threshold: float = 0.0, require_bullish: bool = True
) -> FilterResult:
    if trend_indicator is None:
        return FilterResult(False, "Trend Filter: indicator is missing")

    is_bullish = trend_indicator > threshold

    if require_bullish and is_bullish:
        return FilterResult(
            True, "Trend Filter: Bullish trend confirmed", {"trend": trend_indicator}
        )
    elif not require_bullish and not is_bullish:
        return FilterResult(
            True, "Trend Filter: Bearish trend confirmed", {"trend": trend_indicator}
        )

    return FilterResult(
        False,
        "Trend Filter: Market trend does not align with requirement",
        {"trend": trend_indicator, "require_bullish": require_bullish},
    )


def volatility_filter(
    volatility: float, min_vol: float = 0.0, max_vol: float = float("inf")
) -> FilterResult:
    if volatility is None:
        return FilterResult(False, "Volatility Filter: indicator is missing")

    if min_vol <= volatility <= max_vol:
        return FilterResult(
            True,
            "Volatility Filter: Within acceptable range",
            {"volatility": volatility},
        )

    return FilterResult(
        False,
        f"Volatility Filter: Out of range [{min_vol}, {max_vol}]",
        {"volatility": volatility},
    )


def stale_feature_filter(
    feature_timestamp: datetime, current_timestamp: datetime, max_age_seconds: int = 300
) -> FilterResult:
    if feature_timestamp is None or current_timestamp is None:
        return FilterResult(False, "Stale Filter: Timestamps missing")

    age_seconds = (current_timestamp - feature_timestamp).total_seconds()

    if age_seconds <= max_age_seconds:
        return FilterResult(
            True, "Stale Filter: Features are fresh", {"age_seconds": age_seconds}
        )

    return FilterResult(
        False,
        f"Stale Filter: Features are stale ({age_seconds}s > {max_age_seconds}s)",
        {"age_seconds": age_seconds},
    )
