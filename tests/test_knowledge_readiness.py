import pytest
from app.knowledge.readiness import OperatorReadinessEvaluator
from app.knowledge.enums import ReadinessLevel
import app.knowledge.readiness


def test_readiness_evaluation(monkeypatch):
    class MockRegistry:
        def get_results_for_operator(self, op_id):
            return []

    monkeypatch.setattr(app.knowledge.readiness, "quiz_registry", MockRegistry())
    evaluator = OperatorReadinessEvaluator()

    # Empty results -> Caution (advisory) because missing required quizzes
    res = evaluator.evaluate("u1", "ops")
    assert res.readiness_level == ReadinessLevel.CAUTION
    assert len(res.stale_readiness_reasons) > 0
