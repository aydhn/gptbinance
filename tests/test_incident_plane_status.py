from app.incident_plane.status import IncidentStatusMachine
from app.incident_plane.enums import IncidentStatus
from app.incident_plane.exceptions import InvalidStatusTransition
import pytest

def test_status_transition_validity():
    event = IncidentStatusMachine.transition(IncidentStatus.DETECTED, IncidentStatus.TRIAGING, "Start Triage", "operator_1")
    assert event.new_status == IncidentStatus.TRIAGING

    with pytest.raises(InvalidStatusTransition):
        IncidentStatusMachine.transition(IncidentStatus.DETECTED, IncidentStatus.RESOLVED, "Quick fix", "operator_1")
