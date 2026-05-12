import pytest
from app.observability_plane.replay import ReplayReconstructionTracker

def test_replay_tracking():
    tracker = ReplayReconstructionTracker()
    tracker.report_reconstruction("rep1", "man1")
    assert tracker.get_reconstruction("rep1") == "man1"
