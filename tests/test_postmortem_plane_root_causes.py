import pytest
from app.postmortem_plane.root_causes import RootCauseDiscipline

def test_root_cause_creation():
    rc = RootCauseDiscipline.create_root_cause("RC-1", "Lack of circuit breaker", ["N-1", "N-2"], True, "Logs show retries compounding")
    assert rc.root_cause_id == "RC-1"
    assert rc.is_multi_root == True
