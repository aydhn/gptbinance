from app.incident_plane.trust import IncidentTrustEngine
from app.incident_plane.models import IncidentManifest
from app.incident_plane.enums import IncidentStatus, IncidentSeverity, IncidentUrgency, IncidentTrustVerdict
from datetime import datetime, timezone

def test_trust_verdict_synthesis():
    manifest = IncidentManifest(
        incident_id="INC-001",
        family="data_integrity_incident",
        severity=IncidentSeverity.SEV1_HIGH,
        urgency=IncidentUrgency.IMMEDIATE,
        current_status=IncidentStatus.RECOVERING,
        blast_radius={"scope": "market_data"},
        primary_owner="operator_1"
    )

    verdict = IncidentTrustEngine.evaluate(manifest)
    assert verdict == IncidentTrustVerdict.DEGRADED

    manifest.severity = IncidentSeverity.SEV0_EMERGENCY
    verdict2 = IncidentTrustEngine.evaluate(manifest)
    assert verdict2 == IncidentTrustVerdict.BLOCKED
