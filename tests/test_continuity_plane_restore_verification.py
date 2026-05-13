import pytest
from datetime import datetime, timezone
from app.continuity_plane.restore_verification import RestoreVerificationManager
from app.continuity_plane.models import RestoreVerificationRecord

def test_restore_verification_manager():
    manager = RestoreVerificationManager()
    record = RestoreVerificationRecord(
        verification_id="verif_1",
        restore_id="rest_1",
        is_verified=True,
        details="All checks passed",
        timestamp=datetime.now(timezone.utc)
    )
    manager.record_verification(record)

    retrieved = manager.get_verification("verif_1")
    assert retrieved is not None
    assert retrieved.verification_id == "verif_1"
