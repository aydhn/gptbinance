from app.strategies.engine import StrategyEngine


def test_allocation_candidates():
    engine = StrategyEngine()
    candidates = engine.produce_candidates()
    assert len(candidates) > 0
    assert candidates[0].symbol == "BTCUSDT"
    assert candidates[0].confidence == 0.85
