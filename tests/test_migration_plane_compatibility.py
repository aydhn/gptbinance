import pytest
from app.migration_plane.compatibility import CompatibilityEvaluator
from app.migration_plane.enums import CompatibilityClass

def test_compatibility_evaluator():
    evaluator = CompatibilityEvaluator()
    result = evaluator.evaluate("mig_001")
    assert result["status"] == CompatibilityClass.FULLY_COMPATIBLE
    assert "details" in result
