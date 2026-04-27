from typing import List
from app.strategies.models import StrategySpec
from app.strategies.enums import StrategyType


def get_core_strategy_specs() -> List[StrategySpec]:
    """
    Returns a predefined list of core strategy specifications for testing.
    In a real system, these might be loaded from a configuration file.
    """
    return [
        StrategySpec(
            name="trend_follow_core",
            strategy_type=StrategyType.TREND_FOLLOW,
            required_features=["sma_fast", "sma_slow", "atr"],
            min_history=5,
            parameters={
                "trend_threshold": 0.0,
                "volatility_multiplier": 1.5,
                "score_weight": 1.0,
            },
        ),
        StrategySpec(
            name="mean_reversion_core",
            strategy_type=StrategyType.MEAN_REVERSION,
            required_features=["rsi", "bollinger_upper", "bollinger_lower", "close"],
            min_history=5,
            parameters={
                "rsi_oversold": 30.0,
                "rsi_overbought": 70.0,
                "score_weight": 0.8,
            },
        ),
        StrategySpec(
            name="breakout_core",
            strategy_type=StrategyType.BREAKOUT,
            required_features=[
                "donchian_upper",
                "donchian_lower",
                "close",
                "volume",
                "volume_sma",
            ],
            min_history=5,
            parameters={"volume_multiplier": 1.5, "score_weight": 1.2},
        ),
        StrategySpec(
            name="structure_divergence_core",
            strategy_type=StrategyType.STRUCTURE,
            required_features=["rsi", "close", "pivot_high", "pivot_low"],
            min_history=10,
            parameters={"score_weight": 1.5},
        ),
    ]
