import pytest
from app.migration_plane.divergence import DivergenceManager

def test_generate_divergence_report():
    manager = DivergenceManager()
    result = manager.generate_report("mig_001", "MEDIUM", {"diff": "some diff"})
    assert result.severity == "MEDIUM"
