from datetime import datetime, timezone
from app.strategies.models import StrategyContext, StrategySpec
from app.strategies.enums import StrategyType, SignalDirection

from app.strategies.implementations.trend_follow_core import TrendFollowCore
from app.strategies.implementations.mean_reversion_core import MeanReversionCore


def test_trend_follow_core():
    spec = StrategySpec(name="trend", strategy_type=StrategyType.TREND_FOLLOW)
    strat = TrendFollowCore(spec)

    ctx = StrategyContext(
        symbol="BTC",
        interval="15m",
        timestamp=datetime.now(timezone.utc),
        features={
            "sma_fast": 105.0,
            "sma_slow": 100.0,
            "prev_sma_fast": 99.0,
            "prev_sma_slow": 101.0,
            "atr": 2.5,
        },
    )

    res = strat.evaluate(ctx)
    assert res.signal is not None
    assert res.signal.direction == SignalDirection.LONG
    assert res.entry_intent is not None


def test_mean_reversion_core():
    spec = StrategySpec(
        name="mr",
        strategy_type=StrategyType.MEAN_REVERSION,
        parameters={"rsi_oversold": 30.0, "rsi_overbought": 70.0},
    )
    strat = MeanReversionCore(spec)

    ctx = StrategyContext(
        symbol="BTC",
        interval="15m",
        timestamp=datetime.now(timezone.utc),
        features={
            "rsi": 25.0,
            "close": 98.0,
            "bollinger_upper": 110.0,
            "bollinger_lower": 100.0,
        },
    )

    res = strat.evaluate(ctx)
    assert res.signal is not None
    assert res.signal.direction == SignalDirection.LONG
