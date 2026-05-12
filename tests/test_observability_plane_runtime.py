import pytest
from app.observability_plane.runtime import RuntimeTelemetryTracker
from app.observability_plane.models import ObservabilityAuditRecord
from app.observability_plane.enums import TrustVerdict
from datetime import datetime, timezone

def test_runtime_tracking():
    tracker = RuntimeTelemetryTracker()
    tracker.report_audit(ObservabilityAuditRecord(audit_id="a1", timestamp=datetime.now(timezone.utc), verdict=TrustVerdict.TRUSTED))
    assert tracker.get_audit("a1").verdict == TrustVerdict.TRUSTED
