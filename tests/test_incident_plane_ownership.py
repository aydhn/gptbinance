from app.incident_plane.ownership import IncidentOwnershipEngine
import pytest

def test_owner_assignment():
    assignment = IncidentOwnershipEngine.assign_owner(primary="op1", secondary="op2", notes="Initial assignment")
    assert assignment.primary == "op1"
    assert assignment.secondary == "op2"

    with pytest.raises(ValueError):
        IncidentOwnershipEngine.assign_owner(primary="")
