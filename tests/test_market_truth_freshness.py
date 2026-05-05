from app.market_truth.freshness import FreshnessEvaluator
from app.market_truth.enums import TruthDomain, FreshnessClass


def test_freshness_evaluator():
    evaluator = FreshnessEvaluator()
    res = evaluator.evaluate(
        "BTCUSDT", TruthDomain.TRADE, "canary_live_caution", lag_ms=600, silence_ms=100
    )
    assert res.freshness_class == FreshnessClass.STALE
