import pytest
from app.resilience.assertions import AssertionEvaluator
from app.resilience.models import AssertionSpec
from app.resilience.enums import AssertionVerdict


@pytest.mark.asyncio
async def test_assertion_evaluator():
    evaluator = AssertionEvaluator()
    spec = AssertionSpec(
        id="test_assertion",
        description="test",
        expected_behavior="test",
        timeout_ms=100,
    )

    result = await evaluator.evaluate(spec, "test_run")
    assert result.spec_id == "test_assertion"
    assert result.verdict == AssertionVerdict.PASS
    assert len(result.evidence_refs) > 0
