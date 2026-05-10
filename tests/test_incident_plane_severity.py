from app.incident_plane.severity import IncidentSeverityEngine
from app.incident_plane.enums import IncidentSeverity
from app.incident_plane.exceptions import InvalidSeverityEscalation
import pytest

def test_severity_escalation():
    new_sev = IncidentSeverityEngine.escalate(
        IncidentSeverity.SEV2_MEDIUM,
        IncidentSeverity.SEV1_HIGH,
        rationale="Impact increased"
    )
    assert new_sev == IncidentSeverity.SEV1_HIGH

    with pytest.raises(InvalidSeverityEscalation):
        IncidentSeverityEngine.escalate(
            IncidentSeverity.SEV2_MEDIUM,
            IncidentSeverity.SEV1_HIGH,
            rationale=""
        )
