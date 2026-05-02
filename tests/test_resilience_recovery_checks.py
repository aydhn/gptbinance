import pytest
from app.resilience.recovery_checks import RecoveryEvaluator
from app.resilience.models import AssertionSpec
from app.resilience.enums import AssertionVerdict


@pytest.mark.asyncio
async def test_recovery_evaluator():
    evaluator = RecoveryEvaluator()
    spec = AssertionSpec(
        id="test_recovery", description="test", expected_behavior="test", timeout_ms=100
    )

    result = await evaluator.evaluate(spec, "test_run")
    assert result.spec_id == "test_recovery"
    assert result.verdict == AssertionVerdict.PASS
    assert len(result.evidence_refs) > 0
