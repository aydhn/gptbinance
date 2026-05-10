from app.incident_plane.containment import IncidentContainmentEngine

def test_containment_record():
    record = IncidentContainmentEngine.record_containment("INC-001", ["workflow"], ["hold_allocations"])
    assert record.is_complete is True
    assert record.scopes_contained == ["workflow"]
