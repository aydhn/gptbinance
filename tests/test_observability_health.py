import pytest
from app.observability.health import HealthAggregator
from app.observability.enums import ComponentType, HealthSeverity


@pytest.fixture
def aggregator():
    return HealthAggregator()


def test_component_health(aggregator):
    aggregator.record_signal(
        component=ComponentType.DATA_STREAM,
        severity=HealthSeverity.DEGRADED,
        reason="Minor lag",
    )

    snap = aggregator.evaluate_component(ComponentType.DATA_STREAM)
    assert snap.severity == HealthSeverity.DEGRADED

    # Critical overrides degraded
    aggregator.record_signal(
        component=ComponentType.DATA_STREAM,
        severity=HealthSeverity.CRITICAL,
        reason="Stream disconnected",
    )
    snap = aggregator.evaluate_component(ComponentType.DATA_STREAM)
    assert snap.severity == HealthSeverity.CRITICAL


def test_system_health(aggregator):
    aggregator.record_signal(
        component=ComponentType.DATA_STREAM,
        severity=HealthSeverity.DEGRADED,
        reason="Minor lag",
    )
    aggregator.record_signal(
        component=ComponentType.EXECUTION,
        severity=HealthSeverity.HEALTHY,
        reason="All good",
    )

    sys_snap = aggregator.evaluate_system()
    assert (
        sys_snap.severity == HealthSeverity.DEGRADED
    )  # System inherits highest severity
    assert (
        sys_snap.components[ComponentType.DATA_STREAM].severity
        == HealthSeverity.DEGRADED
    )
