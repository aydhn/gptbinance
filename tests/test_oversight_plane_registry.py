from app.oversight_plane.registry import CanonicalOversightRegistry
from app.oversight_plane.models import OversightRecord
import pytest
from app.oversight_plane.exceptions import InvalidOversightObjectError

def test_registry_registration():
    reg = CanonicalOversightRegistry()
    rec = OversightRecord(
        oversight_id="OV-001",
        class_type="authoritative",
        owner="admin",
        scope_ref="full",
        scrutiny_posture="light",
        intervention_posture="advisory"
    )
    reg.register_oversight(rec)
    assert reg.get_oversight("OV-001") == rec

def test_registry_missing_id():
    reg = CanonicalOversightRegistry()
    rec = OversightRecord(
        oversight_id="",
        class_type="authoritative",
        owner="admin",
        scope_ref="full",
        scrutiny_posture="light",
        intervention_posture="advisory"
    )
    with pytest.raises(InvalidOversightObjectError):
        reg.register_oversight(rec)
