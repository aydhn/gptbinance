from app.incident_plane.actions import IncidentActionEngine
import pytest

def test_containment_action_correctness():
    action = IncidentActionEngine.record_action("INC-001", "freeze", "Stop market damage", "operator_1")
    assert action.action_type == "freeze"

    with pytest.raises(ValueError):
        IncidentActionEngine.record_action("INC-001", "freeze", "", "operator_1")
