import pytest
from app.continuity_plane.readiness import ContinuityReadinessAggregator

def test_readiness_aggregator():
    aggregator = ContinuityReadinessAggregator()
    assert aggregator is not None
