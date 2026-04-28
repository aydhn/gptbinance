from datetime import datetime
from app.research.regime.volatility_regime import VolatilityExpansionEvaluator
from app.research.regime.models import RegimeFeatureBundle
from app.research.regime.enums import VolatilityRegime


def test_volatility_high():
    evaluator = VolatilityExpansionEvaluator()
    bundle = RegimeFeatureBundle(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        interval="15m",
        features={"volatility_atr": 2.5, "volatility_bb_width": 2.5},
    )
    result = evaluator.evaluate(bundle)
    assert result.label.name == VolatilityRegime.NOISY_HIGH_VOL.name


def test_volatility_low():
    evaluator = VolatilityExpansionEvaluator()
    bundle = RegimeFeatureBundle(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        interval="15m",
        features={"volatility_atr": 0.2, "volatility_bb_width": 0.2},
    )
    result = evaluator.evaluate(bundle)
    assert result.label.name == VolatilityRegime.LOW_ENERGY.name
