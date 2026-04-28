from datetime import datetime
from app.research.regime.mean_reversion_regime import MeanReversionProneEvaluator
from app.research.regime.models import RegimeFeatureBundle


def test_mean_reversion_overstretched():
    evaluator = MeanReversionProneEvaluator()
    bundle = RegimeFeatureBundle(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        interval="15m",
        features={"momentum_rsi": 80.0, "price_to_sma_dist": 0.02},
    )
    result = evaluator.evaluate(bundle)
    assert result.label.name == "OVERSTRETCHED"


def test_mean_reversion_range_bound():
    evaluator = MeanReversionProneEvaluator()
    bundle = RegimeFeatureBundle(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        interval="15m",
        features={"momentum_rsi": 50.0, "price_to_sma_dist": 0.0},
    )
    result = evaluator.evaluate(bundle)
    assert result.label.name == "RANGE_BOUND"
