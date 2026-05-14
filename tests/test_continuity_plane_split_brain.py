import pytest
from datetime import datetime, timezone
from app.continuity_plane.split_brain import SplitBrainRiskManager
from app.continuity_plane.models import SplitBrainRiskRecord

def test_split_brain_manager():
    manager = SplitBrainRiskManager()
    record = SplitBrainRiskRecord(
        risk_id="sbr_1",
        service_id="srv_1",
        risk_type="dual_writer",
        severity="critical",
        description="Dual writer risk detected",
        timestamp=datetime.now(timezone.utc)
    )
    manager.record_risk(record)

    retrieved = manager.get_risk("sbr_1")
    assert retrieved is not None
    assert retrieved.risk_id == "sbr_1"
