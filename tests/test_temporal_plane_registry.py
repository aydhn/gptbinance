from app.temporal_plane.registry import CanonicalTemporalRegistry
from app.temporal_plane.models import TemporalObject, ClockAuthorityRecord, ValidityWindowRecord, FreshnessRecord, AdmissibilityRecord
from app.temporal_plane.enums import TemporalClass, ClockClass, WindowClass, FreshnessClass, AdmissibilityClass
from datetime import datetime

def test_temporal_plane_registry():
    registry = CanonicalTemporalRegistry()
    t_obj = TemporalObject(
        temporal_id="t-001",
        t_class=TemporalClass.EVENT,
        owner="sys",
        scope="global",
        clock_authority=ClockAuthorityRecord(authority_id="ca-1", clock_ref="clk-1", is_authoritative=True),
        validity=ValidityWindowRecord(window_id="w-1", start_ts=datetime.now(), end_ts=None, window_class=WindowClass.VALIDITY),
        freshness=FreshnessRecord(posture=FreshnessClass.FRESH, evaluated_at=datetime.now()),
        admissibility=AdmissibilityRecord(posture=AdmissibilityClass.ADMISSIBLE, reason="valid")
    )
    registry.register(t_obj, "decision_temporal_record")
    assert registry.get("t-001") == t_obj
