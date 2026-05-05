import pytest
from app.activation.expansion import ExpansionEvaluator
from app.activation.models import ProbationStatus
from app.activation.enums import ProbationVerdict, ExpansionVerdict


def test_expansion_evaluator_pass():
    status = ProbationStatus(
        intent_id="intent-1", verdict=ProbationVerdict.PASS, blockers=[]
    )
    decision = ExpansionEvaluator.evaluate(status)
    assert decision.verdict == ExpansionVerdict.REQUIRES_APPROVAL


def test_expansion_evaluator_fail():
    status = ProbationStatus(
        intent_id="intent-1",
        verdict=ProbationVerdict.FAIL,
        blockers=["market_truth_health"],
    )
    decision = ExpansionEvaluator.evaluate(status)
    assert decision.verdict == ExpansionVerdict.BLOCKED
