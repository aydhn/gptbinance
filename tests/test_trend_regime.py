from datetime import datetime
from app.research.regime.trend_regime import TrendPersistenceEvaluator
from app.research.regime.models import RegimeFeatureBundle
from app.research.regime.enums import TrendRegime


def test_trend_strong_uptrend():
    evaluator = TrendPersistenceEvaluator()
    bundle = RegimeFeatureBundle(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        interval="15m",
        features={
            "trend_sma_fast": 105.0,
            "trend_sma_slow": 100.0,
            "momentum_rsi": 65.0,
        },
    )
    result = evaluator.evaluate(bundle)
    assert result.label.name == TrendRegime.STRONG_UPTREND.name


def test_trend_no_trend():
    evaluator = TrendPersistenceEvaluator()
    bundle = RegimeFeatureBundle(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        interval="15m",
        features={
            "trend_sma_fast": 105.0,
            "trend_sma_slow": 100.0,
            "momentum_rsi": 30.0,
        },
    )
    result = evaluator.evaluate(bundle)
    assert result.label.name == TrendRegime.WEAK_UPTREND.name  # Fixed based on logic

    bundle2 = RegimeFeatureBundle(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        interval="15m",
        features={
            "trend_sma_fast": 100.0,
            "trend_sma_slow": 100.0,
            "momentum_rsi": 50.0,
        },
    )
    result2 = evaluator.evaluate(bundle2)
    assert result2.label.name == TrendRegime.NO_TREND.name
