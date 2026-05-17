import pytest
from app.environment_plane.readiness import evaluate_readiness
from app.environment_plane.enums import ReadinessClass

def test_evaluate_readiness():
    readiness = evaluate_readiness(ReadinessClass.PROMOTION_READY, "All tests passed")
    assert readiness.readiness_class == ReadinessClass.PROMOTION_READY
    assert readiness.proof_notes == "All tests passed"
