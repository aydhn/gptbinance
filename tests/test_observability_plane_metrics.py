import pytest
from app.observability_plane.metrics import MetricRegistry
from app.observability_plane.models import MetricDefinition
from app.observability_plane.enums import TelemetryClass, MetricClass
from app.observability_plane.exceptions import InvalidTelemetryDefinitionError

def test_metric_unit_requirement():
    reg = MetricRegistry()
    with pytest.raises(InvalidTelemetryDefinitionError):
        reg.register_metric(MetricDefinition(telemetry_id="test_metric", telemetry_class=TelemetryClass.METRIC, producer="test", description="desc", metric_class=MetricClass.COUNTER, unit="", aggregation_compatibility=["SUM"]))

    valid_metric = MetricDefinition(telemetry_id="test_metric", telemetry_class=TelemetryClass.METRIC, producer="test", description="desc", metric_class=MetricClass.COUNTER, unit="ms", aggregation_compatibility=["SUM"])
    reg.register_metric(valid_metric)
    assert reg.get_metric("test_metric").unit == "ms"
