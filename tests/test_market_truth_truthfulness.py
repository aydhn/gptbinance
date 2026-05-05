from app.market_truth.truthfulness import GlobalTruthfulnessEvaluator
from app.market_truth.enums import MarketTruthVerdict


def test_global_truthfulness():
    engine = GlobalTruthfulnessEvaluator()
    res = engine.evaluate("BTC", [{"stale_caution": True}])
    assert res.overall_verdict == MarketTruthVerdict.CAUTION

    res2 = engine.evaluate("BTC", [{"is_aligned": False}])
    assert res2.overall_verdict == MarketTruthVerdict.BLOCK
