import pytest
from app.model_plane.quality import ModelQualityEvaluator


def test_model_quality_acceptable():
    evaluator = ModelQualityEvaluator()
    verdict = evaluator.evaluate_quality(
        "m1", total_runs=1000, missing_outputs=10, abstentions=50
    )

    assert verdict.missing_output_rate == 0.01
    assert verdict.abstention_rate == 0.05
    assert verdict.is_acceptable is True
    assert len(verdict.warnings) == 0


def test_model_quality_high_missing():
    evaluator = ModelQualityEvaluator()
    verdict = evaluator.evaluate_quality(
        "m1", total_runs=1000, missing_outputs=100, abstentions=50
    )

    assert verdict.missing_output_rate == 0.1
    assert verdict.is_acceptable is False
    assert "too high" in verdict.warnings[0]


def test_model_quality_high_abstention():
    evaluator = ModelQualityEvaluator()
    verdict = evaluator.evaluate_quality(
        "m1", total_runs=1000, missing_outputs=10, abstentions=250
    )

    assert verdict.abstention_rate == 0.25
    assert verdict.is_acceptable is False
    assert "unstable/too high" in verdict.warnings[0]
