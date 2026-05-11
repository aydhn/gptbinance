import pytest
from app.migration_plane.quality import QualityManager

def test_evaluate_quality():
    manager = QualityManager()
    result = manager.evaluate_quality("mig_001")
    assert result["status"] == "EVALUATED"
