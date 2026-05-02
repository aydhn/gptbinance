from app.qualification.waivers import WaiverManager
from app.qualification.models import WaiverRecord
from datetime import datetime, timezone, timedelta


def test_waiver_manager():
    manager = WaiverManager()
    finding_id = "f-123"
    future = datetime.now(timezone.utc) + timedelta(days=1)
    record = WaiverRecord(
        finding_id=finding_id, rationale="Test", approved_by="admin", expires_at=future
    )

    manager.add_waiver(record)
    active = manager.get_active_waiver_for_finding(finding_id)
    assert active is not None
    assert active.waiver_id == record.waiver_id
