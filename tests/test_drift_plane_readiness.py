import pytest
from app.drift_plane.readiness import ReadinessManager

def test_readiness_evaluation():
    manager = ReadinessManager()
    readiness = manager.evaluate_readiness("drift-1")
    assert readiness["status"] == "ready"
