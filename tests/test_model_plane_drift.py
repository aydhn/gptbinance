import pytest
from app.model_plane.drift import ModelDriftEvaluator
from app.model_plane.enums import DriftSeverity


def test_model_drift_none():
    evaluator = ModelDriftEvaluator()
    report = evaluator.evaluate_drift(
        "m1", score_drift_metric=0.1, abstention_drift_metric=0.1
    )

    assert report.drift_severity == DriftSeverity.NONE
    assert len(report.caveats) == 0


def test_model_drift_moderate():
    evaluator = ModelDriftEvaluator()
    report = evaluator.evaluate_drift(
        "m1", score_drift_metric=0.3, abstention_drift_metric=0.1
    )

    assert report.drift_severity == DriftSeverity.MODERATE
    assert "Moderate score drift detected" in report.caveats


def test_model_drift_critical():
    evaluator = ModelDriftEvaluator()
    report = evaluator.evaluate_drift(
        "m1", score_drift_metric=0.6, abstention_drift_metric=0.1
    )

    assert report.drift_severity == DriftSeverity.CRITICAL
    assert "Score distribution drifted significantly" in report.caveats


def test_model_drift_abstention():
    evaluator = ModelDriftEvaluator()
    report = evaluator.evaluate_drift(
        "m1", score_drift_metric=0.1, abstention_drift_metric=0.4
    )

    assert report.drift_severity == DriftSeverity.MODERATE
    assert "Abstention rate shifted unexpectedly" in report.caveats
