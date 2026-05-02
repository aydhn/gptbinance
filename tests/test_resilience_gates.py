import pytest
from app.resilience.gates import SafetyGate
from app.resilience.models import (
    ExperimentScope,
    ExperimentDefinition,
    TargetComponentRef,
    AssertionSpec,
)
from app.resilience.enums import (
    SafeScope,
    GateVerdict,
    ExperimentType,
    TargetComponent,
    DegradationMode,
)


@pytest.fixture
def dummy_scenario():
    return ExperimentDefinition(
        id="dummy",
        name="Dummy",
        description="Dummy",
        experiment_type=ExperimentType.FAULT_INJECTION,
        allowed_scopes=[SafeScope.PAPER, SafeScope.SIMULATION],
        target_components=[TargetComponentRef(component=TargetComponent.DATA_STREAM)],
        assertions=[
            AssertionSpec(
                id="a1", description="desc", expected_behavior="bhv", timeout_ms=100
            )
        ],
        recovery_assertions=[],
        expected_degradation_mode=DegradationMode.PAUSE,
    )


def test_gate_blocks_live_mainnet(dummy_scenario):
    gate = SafetyGate()
    scope = ExperimentScope(
        safe_scope=SafeScope.PAPER, environment="test", is_live_mainnet=True
    )
    report = gate.evaluate(dummy_scenario, scope)

    assert report.verdict == GateVerdict.BLOCK
    assert "strictly prohibited" in report.reason


def test_gate_blocks_disallowed_scope(dummy_scenario):
    gate = SafetyGate()
    # dummy_scenario allows PAPER, SIMULATION. Test with SHADOW.
    scope = ExperimentScope(
        safe_scope=SafeScope.SHADOW, environment="test", is_live_mainnet=False
    )
    report = gate.evaluate(dummy_scenario, scope)

    assert report.verdict == GateVerdict.BLOCK
    assert "not in allowed scopes" in report.reason


def test_gate_allows_valid_scope(dummy_scenario):
    gate = SafetyGate()
    scope = ExperimentScope(
        safe_scope=SafeScope.PAPER, environment="test", is_live_mainnet=False
    )
    report = gate.evaluate(dummy_scenario, scope)

    assert report.verdict == GateVerdict.ALLOW
