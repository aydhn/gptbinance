from app.market_truth.trades import TradeTruthEvaluator


def test_trade_truth():
    engine = TradeTruthEvaluator()
    res = engine.evaluate("BTC", True, 500, 1000)
    assert res.trade_continuity is True
    assert res.stale_silence is False
