import pytest
from app.universe.liquidity import SimpleLiquidityScorer
from app.universe.models import InstrumentRef
from app.universe.enums import InstrumentType, SpreadSeverity

# Focus on spread scoring tests, implemented within SimpleLiquidityScorer for now
def test_spread_score_normal():
    scorer = SimpleLiquidityScorer()
    ref = InstrumentRef(symbol="BTCUSDT", product_type=InstrumentType.SPOT, canonical_symbol="BTCUSDT")
    # 0.001 spread relative -> 10 bps -> Normal
    market_data = {"bidPrice": 1000.00, "askPrice": 1001.00}

    snap = scorer.score_spread(ref, market_data)
    assert snap.severity == SpreadSeverity.NORMAL

def test_spread_score_zero():
    scorer = SimpleLiquidityScorer()
    ref = InstrumentRef(symbol="BTCUSDT", product_type=InstrumentType.SPOT, canonical_symbol="BTCUSDT")
    market_data = {"bidPrice": 0, "askPrice": 0}

    snap = scorer.score_spread(ref, market_data)
    assert snap.severity == SpreadSeverity.UNKNOWN
