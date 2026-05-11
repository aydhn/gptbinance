import pytest
from datetime import datetime, timedelta, timezone
from app.migration_plane.dual_write import DualWriteManager

def test_start_dual_write():
    manager = DualWriteManager()
    expiry = datetime.now(timezone.utc) + timedelta(days=1)
    result = manager.start_dual_write("mig_001", expiry)
    assert result.divergence_detected is False
    assert result.expiry == expiry
