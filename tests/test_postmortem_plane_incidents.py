import pytest
from app.postmortem_plane.incidents import IncidentLinker
from app.postmortem_plane.exceptions import PostmortemPlaneError

def test_incident_bundle_creation():
    bundle = IncidentLinker.create_bundle(["INC-1", "INC-2"], "HIGH", "SYSTEM", "FAMILY-A")
    assert bundle.incident_ids == ["INC-1", "INC-2"]
    assert bundle.severity_carryover == "HIGH"
    assert bundle.incident_family == "FAMILY-A"

    with pytest.raises(PostmortemPlaneError):
        IncidentLinker.create_bundle([], "HIGH", "SYSTEM")
