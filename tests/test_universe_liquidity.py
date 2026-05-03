import pytest
from app.universe.liquidity import SimpleLiquidityScorer
from app.universe.models import InstrumentRef
from app.universe.enums import InstrumentType, LiquiditySeverity, SpreadSeverity

def test_score_liquidity_high():
    scorer = SimpleLiquidityScorer()
    ref = InstrumentRef(symbol="BTCUSDT", product_type=InstrumentType.SPOT, canonical_symbol="BTCUSDT")
    market_data = {"volume": 1000, "quoteVolume": 60_000_000}

    snap = scorer.score_liquidity(ref, market_data)
    assert snap.severity == LiquiditySeverity.HIGH
    assert snap.quote_volume == 60_000_000

def test_score_liquidity_very_low():
    scorer = SimpleLiquidityScorer()
    ref = InstrumentRef(symbol="SHIBUSDT", product_type=InstrumentType.SPOT, canonical_symbol="SHIBUSDT")
    market_data = {"volume": 1000, "quoteVolume": 500_000}

    snap = scorer.score_liquidity(ref, market_data)
    assert snap.severity == LiquiditySeverity.VERY_LOW

def test_score_spread_tight():
    scorer = SimpleLiquidityScorer()
    ref = InstrumentRef(symbol="BTCUSDT", product_type=InstrumentType.SPOT, canonical_symbol="BTCUSDT")
    # 0.01 / 50000 = 0.0000002 = 0.002 bps -> Tight
    market_data = {"bidPrice": 50000.00, "askPrice": 50000.01}

    snap = scorer.score_spread(ref, market_data)
    assert snap.severity == SpreadSeverity.TIGHT

def test_score_spread_wide():
    scorer = SimpleLiquidityScorer()
    ref = InstrumentRef(symbol="UNKNOWN", product_type=InstrumentType.SPOT, canonical_symbol="UNKNOWN")
    # 10 / 105 = ~0.095 = 950 bps -> Very Wide
    market_data = {"bidPrice": 100.00, "askPrice": 110.00}

    snap = scorer.score_spread(ref, market_data)
    assert snap.severity == SpreadSeverity.VERY_WIDE
