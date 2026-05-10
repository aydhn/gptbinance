import pytest
from app.release_plane.readiness import ReleaseReadinessAggregator

def test_readiness_aggregation_pass():
    agg = ReleaseReadinessAggregator()
    report = agg.evaluate("cand-1", {"reviews": {"passed": True}, "bundle_complete": True})
    assert report.sufficient

def test_readiness_aggregation_fail():
    agg = ReleaseReadinessAggregator()
    report = agg.evaluate("cand-1", {"reviews": {"passed": False}, "bundle_complete": True})
    assert not report.sufficient
    assert "Missing review blockers." in report.missing_blockers
