import pytest
from app.model_plane.equivalence import InferenceEquivalenceEvaluator
from app.model_plane.enums import EquivalenceVerdict


def test_inference_equivalence_match():
    evaluator = InferenceEquivalenceEvaluator()
    offline = {"score": 0.85, "class": "UP"}
    runtime = {"score": 0.85, "class": "UP"}

    report = evaluator.compare("m1", offline, runtime)
    assert report.verdict == EquivalenceVerdict.EQUIVALENT
    assert len(report.differences) == 0


def test_inference_equivalence_mismatch():
    evaluator = InferenceEquivalenceEvaluator()
    offline = {"score": 0.85, "class": "UP"}
    runtime = {"score": 0.82, "class": "UP"}

    report = evaluator.compare("m1", offline, runtime)
    assert report.verdict == EquivalenceVerdict.MAJOR_DIVERGENCE
    assert len(report.differences) == 1
    assert "Mismatch on score" in report.differences[0]


def test_inference_equivalence_missing():
    evaluator = InferenceEquivalenceEvaluator()
    offline = {"score": 0.85, "class": "UP"}
    runtime = {"score": 0.85}

    report = evaluator.compare("m1", offline, runtime)
    assert report.verdict == EquivalenceVerdict.MAJOR_DIVERGENCE
    assert "Output class missing in runtime" in report.differences[0]

    offline2 = {"score": 0.85}
    runtime2 = {"score": 0.85, "class": "UP"}
    report2 = evaluator.compare("m1", offline2, runtime2)
    assert report2.verdict == EquivalenceVerdict.MAJOR_DIVERGENCE
    assert "Output class missing in offline" in report2.differences[0]
