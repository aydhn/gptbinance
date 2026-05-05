from app.market_truth.klines import KlineTruthEvaluator


def test_kline_truth():
    engine = KlineTruthEvaluator()
    res = engine.evaluate("BTCUSDT", "1m", 1000, 1005, 0)
    assert res.is_aligned is True

    res2 = engine.evaluate("BTCUSDT", "1m", 1000, 5000, 0)
    assert res2.is_aligned is False
