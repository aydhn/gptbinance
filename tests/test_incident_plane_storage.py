from app.incident_plane.storage import IncidentStorage
from app.incident_plane.repository import IncidentRepository
from app.incident_plane.models import IncidentManifest
from app.incident_plane.enums import IncidentStatus, IncidentSeverity, IncidentUrgency

def test_incident_repository_read_write():
    repo = IncidentRepository()
    manifest = IncidentManifest(
        incident_id="INC-001",
        family="data_integrity_incident",
        severity=IncidentSeverity.SEV2_MEDIUM,
        urgency=IncidentUrgency.IMMEDIATE,
        current_status=IncidentStatus.RECOVERING,
        blast_radius={},
        primary_owner="operator_1"
    )

    repo.save(manifest)
    res = repo.get_manifest("INC-001")
    assert res is not None
    assert res.incident_id == "INC-001"
