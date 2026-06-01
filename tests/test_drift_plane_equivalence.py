import pytest
from app.drift_plane.equivalence import EquivalenceManager
from app.drift_plane.enums import EquivalenceVerdict

def test_equivalence_check():
    manager = EquivalenceManager()
    report = manager.check_equivalence("drift-1")
    assert report.verdict == EquivalenceVerdict.FULLY_EQUIVALENT
