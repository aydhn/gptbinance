import pytest
from app.universe.turnover import TurnoverEvaluator
from app.universe.models import InstrumentRef
from app.universe.enums import InstrumentType, LiquiditySeverity


def test_turnover_evaluator_high():
    evaluator = TurnoverEvaluator()
    ref = InstrumentRef(
        symbol="BTCUSDT", product_type=InstrumentType.SPOT, canonical_symbol="BTCUSDT"
    )
    market_data = {"count": 150000, "quoteVolume": 1000000}

    snap = evaluator.evaluate(ref, market_data)
    assert snap.severity == LiquiditySeverity.HIGH


def test_turnover_evaluator_very_low():
    evaluator = TurnoverEvaluator()
    ref = InstrumentRef(
        symbol="NEWCOIN", product_type=InstrumentType.SPOT, canonical_symbol="NEWCOIN"
    )
    market_data = {"count": 100, "quoteVolume": 1000}

    snap = evaluator.evaluate(ref, market_data)
    assert snap.severity == LiquiditySeverity.VERY_LOW
