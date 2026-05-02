import pytest
from app.observability.metrics import MetricRegistry
from app.observability.models import MetricDefinition
from app.observability.enums import MetricType, MetricUnit, ComponentType
from app.observability.exceptions import InvalidMetricDefinition


@pytest.fixture
def registry():
    return MetricRegistry()


def test_metric_registration(registry):
    defn = MetricDefinition(
        name="test_metric",
        type=MetricType.COUNTER,
        unit=MetricUnit.COUNT,
        component=ComponentType.SYSTEM,
        description="A test metric",
    )
    registry.register(defn)

    assert registry.get_definition("test_metric") == defn

    with pytest.raises(InvalidMetricDefinition):
        registry.register(defn)  # Duplicate


def test_metric_recording(registry):
    defn = MetricDefinition(
        name="test_metric",
        type=MetricType.COUNTER,
        unit=MetricUnit.COUNT,
        component=ComponentType.SYSTEM,
        description="A test metric",
    )
    registry.register(defn)

    registry.record("test_metric", 10.0, tags={"env": "test"})
    samples = registry.get_samples("test_metric")

    assert len(samples) == 1
    assert samples[0].value == 10.0
    assert samples[0].tags["env"] == "test"

    with pytest.raises(InvalidMetricDefinition):
        registry.record("unregistered", 1.0)
