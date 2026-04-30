from app.ml.promotion import PromotionGate
from app.ml.enums import PromotionVerdict


def test_promotion_gate():
    gate = PromotionGate()
    report = gate.check_readiness("run_1")

    assert report.run_id == "run_1"
    assert report.verdict == PromotionVerdict.PASS
