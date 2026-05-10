import pytest
from datetime import datetime
from app.postmortem_plane.preventive_actions import PreventiveActionRegistry
from app.postmortem_plane.exceptions import InvalidRemediationActionError

def test_preventive_action():
    act = PreventiveActionRegistry.register_action("PA-1", "Implement circuit breaker", "user2", datetime.now(), "core", "Prevent cascade failure")
    assert act.action_id == "PA-1"

    with pytest.raises(InvalidRemediationActionError):
        PreventiveActionRegistry.register_action("PA-2", "Implement circuit breaker", "user2", datetime.now(), "core", "")
