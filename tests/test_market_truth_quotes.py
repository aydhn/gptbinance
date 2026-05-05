from app.market_truth.quotes import QuoteTruthEvaluator
from app.market_truth.enums import FreshnessClass


def test_quote_truth():
    engine = QuoteTruthEvaluator()
    res = engine.evaluate("BTC", 100, 99, FreshnessClass.HEALTHY)
    assert res.crossed_suspicion is True
