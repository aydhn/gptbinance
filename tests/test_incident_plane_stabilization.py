from app.incident_plane.stabilization import IncidentStabilizationEngine

def test_stabilization_tracking():
    record = IncidentStabilizationEngine.mark_stabilized("INC-001", "Service is degraded but functional")
    assert record.is_stable is True
    assert "degraded" in record.caveats
