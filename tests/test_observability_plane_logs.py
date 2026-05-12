import pytest
from app.observability_plane.logs import LogSchemaRegistry
from app.observability_plane.models import LogSchema
from app.observability_plane.enums import TelemetryClass, LogClass
from app.observability_plane.exceptions import InvalidSchemaContractError

def test_log_schema_requires_fields():
    reg = LogSchemaRegistry()
    with pytest.raises(InvalidSchemaContractError):
        reg.register_schema(LogSchema(telemetry_id="test_log", telemetry_class=TelemetryClass.LOG, producer="test", description="desc", log_class=LogClass.STRUCTURED, required_fields=[], severity_taxonomy=["INFO", "ERROR"], schema_version="1.0"))

    valid_log = LogSchema(telemetry_id="test_log", telemetry_class=TelemetryClass.LOG, producer="test", description="desc", log_class=LogClass.STRUCTURED, required_fields=["run_id"], severity_taxonomy=["INFO", "ERROR"], schema_version="1.0")
    reg.register_schema(valid_log)
    assert reg.get_schema("test_log").required_fields == ["run_id"]
