import pytest
from app.observability_plane.retention import RetentionRegistry
from app.observability_plane.models import RetentionRecord
from app.observability_plane.enums import RetentionClass
from app.observability_plane.exceptions import RetentionViolationError

def test_retention_days_enforcement():
    reg = RetentionRegistry()
    with pytest.raises(RetentionViolationError):
        reg.register_retention(RetentionRecord(telemetry_id="t1", retention_class=RetentionClass.HOT, retention_days=0))

    reg.register_retention(RetentionRecord(telemetry_id="t1", retention_class=RetentionClass.HOT, retention_days=7))
    assert reg.get_retention("t1").retention_days == 7
