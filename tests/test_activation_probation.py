import pytest
from app.activation.probation import ProbationEvaluator
from app.activation.enums import ProbationVerdict


def test_probation_evaluation_fail():
    evaluator = ProbationEvaluator()
    metrics = {
        "market_truth_health": 0.90,  # Below 0.95 threshold
        "shadow_drift_events": 0,
        "lifecycle_orphans": 0,
    }
    status = evaluator.evaluate("intent-1", metrics)
    assert status.verdict == ProbationVerdict.FAIL
    assert "market_truth_health" in status.blockers


def test_probation_evaluation_pass():
    evaluator = ProbationEvaluator()
    metrics = {
        "market_truth_health": 0.99,
        "shadow_drift_events": 1,
        "lifecycle_orphans": 0,
    }
    status = evaluator.evaluate("intent-1", metrics)
    assert status.verdict == ProbationVerdict.PASS
    assert len(status.blockers) == 0
