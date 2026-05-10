import pytest
from datetime import datetime
from app.postmortem_plane.corrective_actions import CorrectiveActionRegistry
from app.postmortem_plane.exceptions import InvalidRemediationActionError

def test_corrective_action():
    act = CorrectiveActionRegistry.register_action("ACT-1", "Fix index on table X", "user1", datetime.now(), "db_core")
    assert act.action_id == "ACT-1"
    assert act.owner == "user1"

    with pytest.raises(InvalidRemediationActionError):
        CorrectiveActionRegistry.register_action("ACT-2", "Fix index on table X", "", datetime.now(), "db_core")

    with pytest.raises(InvalidRemediationActionError):
        CorrectiveActionRegistry.register_action("ACT-3", "monitor logs", "user1", datetime.now(), "db_core")
