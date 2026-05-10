from app.incident_plane.recovery import IncidentRecoveryEngine

def test_recovery_orchestration():
    record = IncidentRecoveryEngine.record_recovery("INC-001", objectives_met=True, blockers=[])
    assert record.objectives_met is True
    assert record.pending_blockers == []
