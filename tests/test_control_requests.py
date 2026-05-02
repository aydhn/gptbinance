import pytest
from app.control.requests import manager
from app.control.enums import SensitiveActionType, OperatorRole
from app.control.models import OperatorIdentity
from app.control.exceptions import InvalidActionRequest

def test_create_request_success():
    op = OperatorIdentity(id="op1", roles=[OperatorRole.OPS])
    req = manager.create_request(
        SensitiveActionType.START_LIVE_SESSION,
        op,
        rationale="Starting live for event X",
        run_id="run-123"
    )
    assert req.id.startswith("req-")
    assert req.action_type == SensitiveActionType.START_LIVE_SESSION
    assert req.rationale == "Starting live for event X"
    assert req.context.run_id == "run-123"

def test_create_request_missing_rationale():
    op = OperatorIdentity(id="op1", roles=[OperatorRole.OPS])
    with pytest.raises(InvalidActionRequest):
        manager.create_request(SensitiveActionType.START_LIVE_SESSION, op, rationale="")
