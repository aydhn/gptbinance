import pytest
from app.observability_plane.events import EventRegistry
from app.observability_plane.models import EventDefinition
from app.observability_plane.enums import TelemetryClass, EventClass
from app.observability_plane.exceptions import InvalidTelemetryDefinitionError

def test_event_provenance_requirement():
    reg = EventRegistry()
    with pytest.raises(InvalidTelemetryDefinitionError):
        reg.register_event(EventDefinition(telemetry_id="test_event", telemetry_class=TelemetryClass.EVENT, producer="test", description="desc", event_class=EventClass.DOMAIN, provenance=""))

    valid_event = EventDefinition(telemetry_id="test_event", telemetry_class=TelemetryClass.EVENT, producer="test", description="desc", event_class=EventClass.DOMAIN, provenance="workflow_engine")
    reg.register_event(valid_event)
    assert reg.get_event("test_event").provenance == "workflow_engine"
