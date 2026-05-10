import pytest
from app.release_plane.quality import ReleaseQualityChecker

def test_quality_checks():
    checker = ReleaseQualityChecker()
    rep1 = checker.check("cand-1", {})
    assert rep1.passed

    rep2 = checker.check("cand-1", {"missing_pins": True})
    assert not rep2.passed
    assert "Missing Pins" in rep2.issues
