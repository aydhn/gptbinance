from datetime import datetime
from app.research.regime.structure_regime import StructureBreakoutEvaluator
from app.research.regime.models import RegimeFeatureBundle
from app.research.regime.enums import StructureRegime


def test_structure_breakout_pressure():
    evaluator = StructureBreakoutEvaluator()
    bundle = RegimeFeatureBundle(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        interval="15m",
        features={"close": 104.5, "high": 105.0, "low": 95.0},
    )
    result = evaluator.evaluate(bundle)
    assert result.label.name == StructureRegime.BREAKOUT_PRESSURE.name
