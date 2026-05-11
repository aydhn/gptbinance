import pytest
from app.migration_plane.equivalence import EquivalenceManager
from app.migration_plane.enums import EquivalenceVerdict

def test_generate_equivalence_report():
    manager = EquivalenceManager()
    result = manager.generate_report("mig_001", EquivalenceVerdict.EQUIVALENT, {"test": "passed"})
    assert result.verdict == EquivalenceVerdict.EQUIVALENT
