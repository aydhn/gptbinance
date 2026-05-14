from app.value_plane.trust import trust_engine
from app.value_plane.enums import TrustVerdict

def test_trust_engine_evaluation():
    verdict = trust_engine.evaluate_value("val_1")
    assert verdict.verdict == TrustVerdict.TRUSTED
    assert "baseline_check" in verdict.breakdown
