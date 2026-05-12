import pytest
from app.observability_plane.registry import CanonicalTelemetryRegistry
from app.observability_plane.models import TelemetryDefinition
from app.observability_plane.enums import TelemetryClass
from app.observability_plane.exceptions import InvalidTelemetryDefinitionError

def test_registry_enforcement():
    reg = CanonicalTelemetryRegistry()
    metric = TelemetryDefinition(telemetry_id="valid_metric_1", telemetry_class=TelemetryClass.METRIC, producer="test", description="desc")
    reg.register(metric)
    reg.assert_registered("valid_metric_1")

    with pytest.raises(InvalidTelemetryDefinitionError):
        reg.assert_registered("untracked_metric")

    with pytest.raises(InvalidTelemetryDefinitionError):
        reg.register(TelemetryDefinition(telemetry_id="valid_metric_1", telemetry_class=TelemetryClass.LOG, producer="test", description="desc"))
