import pytest
from app.observability_plane.cost import CostTracker

def test_cost_tracking():
    tracker = CostTracker()
    tracker.report_cost_burden("t1", "excessive")
    assert tracker.get_cost_burden("t1") == "excessive"
