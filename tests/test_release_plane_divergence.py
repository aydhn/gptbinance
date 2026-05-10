import pytest
from app.release_plane.divergence import ReleaseDivergenceAnalyzer

def test_divergence_severity():
    analyzer = ReleaseDivergenceAnalyzer()
    rep1 = analyzer.analyze("cand-1", {"environment_drift": ["a"]})
    assert rep1.severity == "high"

    rep2 = analyzer.analyze("cand-1", {"partial_hotfix_drift": True})
    assert rep2.severity == "critical"
