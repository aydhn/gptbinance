import pytest
from app.drift_plane.trust import TrustEvaluator
from app.drift_plane.enums import TrustVerdict

def test_trust_evaluation():
    evaluator = TrustEvaluator()
    verdict = evaluator.evaluate_trust("drift-1")
    assert verdict.verdict == TrustVerdict.TRUSTED
