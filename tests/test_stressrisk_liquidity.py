from app.stressrisk.liquidity import LiquidityStressEngine


def test_liquidity_engine():
    engine = LiquidityStressEngine()
    snapshot = engine.evaluate({}, {})
    assert snapshot.average_spread_widening_pct == 200.0
