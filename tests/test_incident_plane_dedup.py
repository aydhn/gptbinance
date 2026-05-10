from app.incident_plane.dedup import IncidentDedupEngine

def test_duplicate_incident_detection():
    record = IncidentDedupEngine.mark_duplicate("INC-001", "INC-002", "Same root cause")
    assert record.primary_incident_id == "INC-001"
    assert record.duplicate_incident_id == "INC-002"
    assert record.confidence == "High"
