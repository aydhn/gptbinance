import pytest
from app.model_plane.skew import ServingSkewEvaluator


def test_serving_skew_no_skew():
    evaluator = ServingSkewEvaluator()
    report = evaluator.evaluate_skew(
        "m1", "schema_v1", "schema_v1", threshold_diff=False
    )

    assert report.skew_detected is False
    assert len(report.suspected_causes) == 0


def test_serving_skew_schema_mismatch():
    evaluator = ServingSkewEvaluator()
    report = evaluator.evaluate_skew(
        "m1", "schema_v1", "schema_v2", threshold_diff=False
    )

    assert report.skew_detected is True
    assert "Schema mismatch between training and serving" in report.suspected_causes


def test_serving_skew_threshold_diff():
    evaluator = ServingSkewEvaluator()
    report = evaluator.evaluate_skew(
        "m1", "schema_v1", "schema_v1", threshold_diff=True
    )

    assert report.skew_detected is True
    assert "Threshold policy mismatch detected" in report.suspected_causes
