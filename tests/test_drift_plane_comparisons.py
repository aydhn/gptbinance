import pytest
from app.drift_plane.comparisons import ComparisonManager

def test_comparison_creation():
    manager = ComparisonManager()
    manager.add_comparison("comp-1", "baseline_vs_current", "Significant drift detected.")

    comp = manager.get_comparison("comp-1")
    assert comp is not None
    assert comp.comparison_id == "comp-1"
    assert comp.comparison_type == "baseline_vs_current"
    assert comp.result_summary == "Significant drift detected."
