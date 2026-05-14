import pytest
from datetime import datetime, timezone
from app.continuity_plane.exposures import ContinuityExposureManager
from app.continuity_plane.models import ContinuityExposureRecord

def test_exposure_manager():
    manager = ContinuityExposureManager()
    record = ContinuityExposureRecord(
        exposure_id="exp_1",
        service_id="srv_1",
        exposure_type="rto_breach",
        severity="high",
        description="RTO target missed",
        timestamp=datetime.now(timezone.utc)
    )
    manager.record_exposure(record)

    retrieved = manager.get_exposure("exp_1")
    assert retrieved is not None
    assert retrieved.exposure_id == "exp_1"
