import pytest
from app.activation.halts import HaltEvaluator
from app.activation.models import ProbationStatus, ActivationScope
from app.activation.enums import ProbationVerdict, HaltSeverity


def test_halt_evaluator_critical():
    status = ProbationStatus(
        intent_id="intent-1",
        verdict=ProbationVerdict.FAIL,
        blockers=["market_truth_health"],
    )
    scope = ActivationScope()
    decision = HaltEvaluator.evaluate(status, scope)
    assert decision.severity == HaltSeverity.CRITICAL_IMMEDIATE


def test_halt_evaluator_caution():
    status = ProbationStatus(
        intent_id="intent-1",
        verdict=ProbationVerdict.FAIL,
        blockers=["non_critical_drift"],
    )
    scope = ActivationScope()
    decision = HaltEvaluator.evaluate(status, scope)
    assert decision.severity == HaltSeverity.CAUTION
