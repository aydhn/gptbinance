from app.incident_plane.manifests import IncidentManifestBuilder
from app.incident_plane.models import IncidentManifest
from app.incident_plane.enums import IncidentStatus, IncidentSeverity, IncidentUrgency

def test_manifest_builder():
    manifest = IncidentManifest(
        incident_id="INC-001",
        family="data_integrity_incident",
        severity=IncidentSeverity.SEV2_MEDIUM,
        urgency=IncidentUrgency.IMMEDIATE,
        current_status=IncidentStatus.RECOVERING,
        blast_radius={},
        primary_owner="operator_1"
    )

    built = IncidentManifestBuilder.build(manifest)
    assert built.incident_id == "INC-001"
