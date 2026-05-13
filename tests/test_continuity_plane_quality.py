import pytest
from app.continuity_plane.quality import ContinuityQualityChecker

def test_quality_checker():
    checker = ContinuityQualityChecker()
    assert checker is not None
