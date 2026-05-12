import pytest
from app.observability_plane.traces import TraceRegistry
from app.observability_plane.models import TraceDefinition
from app.observability_plane.enums import TelemetryClass, TraceClass
from app.observability_plane.exceptions import InvalidSchemaContractError

def test_trace_linkage_requirement():
    reg = TraceRegistry()
    with pytest.raises(InvalidSchemaContractError):
        reg.register_trace(TraceDefinition(telemetry_id="test_trace", telemetry_class=TelemetryClass.TRACE, producer="test", description="desc", trace_class=TraceClass.WORKFLOW, parent_child_linkage=False, expected_spans=[]))

    valid_trace = TraceDefinition(telemetry_id="test_trace", telemetry_class=TelemetryClass.TRACE, producer="test", description="desc", trace_class=TraceClass.WORKFLOW, parent_child_linkage=True, expected_spans=[])
    reg.register_trace(valid_trace)
    assert reg.get_trace("test_trace").parent_child_linkage is True
