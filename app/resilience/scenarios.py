from app.resilience.models import (
    ExperimentDefinition,
    TargetComponentRef,
    FaultInjectionSpec,
    AssertionSpec,
)
from app.resilience.enums import (
    ExperimentType,
    TargetComponent,
    FaultType,
    SafeScope,
    DegradationMode,
)

SCENARIO_REGISTRY = {}


def register_scenario(definition: ExperimentDefinition):
    SCENARIO_REGISTRY[definition.id] = definition


stale_stream_scenario = ExperimentDefinition(
    id="stale_stream_scenario",
    name="Stale Data Stream Simulation",
    description="Simulates a stale data stream to verify that the system detects it and gracefully degrades.",
    experiment_type=ExperimentType.FAULT_INJECTION,
    allowed_scopes=[
        SafeScope.SIMULATION,
        SafeScope.PAPER,
        SafeScope.SHADOW,
        SafeScope.TESTNET,
    ],
    target_components=[TargetComponentRef(component=TargetComponent.DATA_STREAM)],
    fault_specs=[
        FaultInjectionSpec(
            fault_type=FaultType.STALE_DATA_INJECTION,
            target=TargetComponentRef(component=TargetComponent.DATA_STREAM),
            duration_ms=5000,
            parameters={"staleness_ms": 10000},
        )
    ],
    assertions=[
        AssertionSpec(
            id="stale_detected",
            description="System should detect stale data",
            expected_behavior="Alert opened for stale data stream",
            timeout_ms=6000,
        )
    ],
    recovery_assertions=[
        AssertionSpec(
            id="stale_cleared",
            description="System should clear stale state after fault is removed",
            expected_behavior="Stale data alert resolved",
            timeout_ms=5000,
        )
    ],
    expected_degradation_mode=DegradationMode.PAUSE,
)
register_scenario(stale_stream_scenario)

reject_storm_scenario = ExperimentDefinition(
    id="reject_storm_scenario",
    name="Order Reject Storm Simulation",
    description="Simulates a burst of order rejections to test gateway containment.",
    experiment_type=ExperimentType.FAULT_INJECTION,
    allowed_scopes=[SafeScope.SIMULATION, SafeScope.PAPER, SafeScope.TESTNET],
    target_components=[TargetComponentRef(component=TargetComponent.EXECUTION_GATEWAY)],
    fault_specs=[
        FaultInjectionSpec(
            fault_type=FaultType.EXCEPTION_BURST,
            target=TargetComponentRef(component=TargetComponent.EXECUTION_GATEWAY),
            duration_ms=2000,
            parameters={"exception_type": "OrderRejected", "count": 50},
        )
    ],
    assertions=[
        AssertionSpec(
            id="reject_storm_detected",
            description="Gateway should detect high rejection rate",
            expected_behavior="Kill switch engaged for execution gateway",
            timeout_ms=3000,
        )
    ],
    recovery_assertions=[
        AssertionSpec(
            id="gateway_recovered",
            description="Gateway should recover after manual/auto reset",
            expected_behavior="Gateway health restored",
            timeout_ms=5000,
        )
    ],
    expected_degradation_mode=DegradationMode.HALT,
)
register_scenario(reject_storm_scenario)

reconciliation_drift_scenario = ExperimentDefinition(
    id="reconciliation_drift_scenario",
    name="Reconciliation Drift Spike",
    description="Injects artificial drift to verify reconciliation alerts.",
    experiment_type=ExperimentType.FAULT_INJECTION,
    allowed_scopes=[
        SafeScope.SIMULATION,
        SafeScope.PAPER,
        SafeScope.SHADOW,
        SafeScope.TESTNET,
    ],
    target_components=[TargetComponentRef(component=TargetComponent.RECONCILIATION)],
    fault_specs=[
        FaultInjectionSpec(
            fault_type=FaultType.DRIFT_SPIKE,
            target=TargetComponentRef(component=TargetComponent.RECONCILIATION),
            duration_ms=5000,
            parameters={"drift_amount": 1000.0},
        )
    ],
    assertions=[
        AssertionSpec(
            id="drift_alerted",
            description="System should alert on high drift",
            expected_behavior="High drift alert triggered",
            timeout_ms=6000,
        )
    ],
    recovery_assertions=[
        AssertionSpec(
            id="drift_resolved",
            description="Drift alert should resolve when drift is removed",
            expected_behavior="High drift alert resolved",
            timeout_ms=5000,
        )
    ],
    expected_degradation_mode=DegradationMode.SAFE_FALLBACK,
)
register_scenario(reconciliation_drift_scenario)

backup_verify_fail_scenario = ExperimentDefinition(
    id="backup_verify_fail_scenario",
    name="Backup Verification Failure",
    description="Simulates a failure during backup verification.",
    experiment_type=ExperimentType.FAULT_INJECTION,
    allowed_scopes=[SafeScope.SIMULATION, SafeScope.PAPER, SafeScope.SHADOW],
    target_components=[TargetComponentRef(component=TargetComponent.STORAGE)],
    fault_specs=[
        FaultInjectionSpec(
            fault_type=FaultType.CHECKSUM_MISMATCH,
            target=TargetComponentRef(component=TargetComponent.STORAGE),
            duration_ms=10000,
            parameters={"file": "backup.db"},
        )
    ],
    assertions=[
        AssertionSpec(
            id="backup_alert",
            description="Should alert on backup verify fail",
            expected_behavior="Backup verification alert opened",
            timeout_ms=5000,
        )
    ],
    recovery_assertions=[
        AssertionSpec(
            id="backup_resolved",
            description="Should resolve after next successful verify",
            expected_behavior="Backup verification alert resolved",
            timeout_ms=5000,
        )
    ],
    expected_degradation_mode=DegradationMode.IGNORE,
)
register_scenario(backup_verify_fail_scenario)


def get_scenario(scenario_id: str) -> ExperimentDefinition:
    if scenario_id not in SCENARIO_REGISTRY:
        from app.resilience.exceptions import InvalidExperimentDefinitionError

        raise InvalidExperimentDefinitionError(f"Scenario not found: {scenario_id}")
    return SCENARIO_REGISTRY[scenario_id]


def list_scenarios():
    return list(SCENARIO_REGISTRY.values())
