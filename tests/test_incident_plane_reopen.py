from app.incident_plane.reopen import IncidentReopenEngine
from app.incident_plane.enums import IncidentStatus
import pytest

def test_reopen_lineage_correctness():
    status = IncidentReopenEngine.reopen("INC-001", reason="Failed verification check post-closure")
    assert status == IncidentStatus.REOPENED

    with pytest.raises(ValueError, match="Silent reopen not allowed"):
        IncidentReopenEngine.reopen("INC-001", reason="")
