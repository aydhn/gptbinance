import pytest
from app.release_plane.equivalence import ReleaseEquivalenceEvaluator
from app.release_plane.enums import EnvironmentClass, EquivalenceVerdict

def test_release_equivalence_clean():
    evaluator = ReleaseEquivalenceEvaluator()
    report = evaluator.evaluate("cand-1", [EnvironmentClass.REPLAY, EnvironmentClass.LIVE_FULL], {})
    assert report.verdict == EquivalenceVerdict.EQUIVALENT

def test_release_equivalence_drift():
    evaluator = ReleaseEquivalenceEvaluator()
    report = evaluator.evaluate("cand-1", [EnvironmentClass.REPLAY, EnvironmentClass.LIVE_FULL], {"drift_detected": True})
    assert report.verdict == EquivalenceVerdict.DIVERGENT
