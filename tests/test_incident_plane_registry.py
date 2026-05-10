from app.incident_plane.registry import CanonicalIncidentRegistry

def test_registry_integrity():
    assert CanonicalIncidentRegistry.is_valid_family("data_integrity_incident") is True
    assert CanonicalIncidentRegistry.is_valid_family("invalid_family") is False
    assert len(CanonicalIncidentRegistry.FAMILIES) > 0
