import pytest
from app.continuity_plane.reporting import ContinuityReporter

def test_continuity_reporter():
    reporter = ContinuityReporter()
    assert reporter is not None
