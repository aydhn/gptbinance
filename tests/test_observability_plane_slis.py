import pytest
from app.observability_plane.slis import SliSupportRegistry
from app.observability_plane.models import SliSupportRecord

def test_sli_support():
    reg = SliSupportRegistry()
    reg.register_sli_support(SliSupportRecord(sli_id="sli1", supported_telemetry_refs=["t1"]))
    assert reg.get_sli_support("sli1").supported_telemetry_refs == ["t1"]
