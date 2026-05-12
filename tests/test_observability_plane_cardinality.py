import pytest
from app.observability_plane.cardinality import CardinalityTracker
from app.observability_plane.models import CardinalityCostRecord

def test_cardinality_tracking():
    tracker = CardinalityTracker()
    tracker.report_cardinality(CardinalityCostRecord(telemetry_id="t1", estimated_series=10000, cost_burden="high"))
    assert tracker.get_cardinality("t1").estimated_series == 10000
