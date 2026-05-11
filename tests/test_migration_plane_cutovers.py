import pytest
from app.migration_plane.cutovers import CutoverManager, CutoverEvaluator
from app.migration_plane.enums import CutoverClass

def test_execute_cutover():
    manager = CutoverManager()
    result = manager.execute_cutover("mig_001", "production", CutoverClass.ZERO_DOWNTIME)
    assert result.is_successful is True
    assert result.cutover_class == CutoverClass.ZERO_DOWNTIME
    assert result.environment == "production"

def test_cutover_evaluator():
    evaluator = CutoverEvaluator()
    result = evaluator.evaluate("cut_001")
    assert result["status"] == "EVALUATED"
