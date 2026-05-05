from app.market_truth.marks import MarkPriceTruthEvaluator
from app.market_truth.enums import FreshnessClass


def test_mark_truth():
    engine = MarkPriceTruthEvaluator()
    res = engine.evaluate("BTC", FreshnessClass.STALE)
    assert res.stale_caution is True
