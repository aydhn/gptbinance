import pytest
from app.control.break_glass import manager as bg_manager
from app.control.requests import manager as req_manager
from app.control.enums import (
    SensitiveActionType,
    OperatorRole,
    BreakGlassSeverity,
    AuthorizationVerdict,
)
from app.control.models import OperatorIdentity
from app.control.exceptions import BreakGlassViolation


def test_break_glass_success():
    requester = OperatorIdentity(id="op1", roles=[OperatorRole.OPS])
    req = req_manager.create_request(
        SensitiveActionType.FLATTEN_LIVE_SESSION, requester, "test"
    )

    bg_req = bg_manager.request_break_glass(
        req.id, BreakGlassSeverity.CRITICAL_RISK, "System bleeding"
    )

    admin = OperatorIdentity(id="admin", roles=[OperatorRole.ADMIN])
    auth_res = bg_manager.authorize_break_glass(req, admin, bg_req)

    assert auth_res.verdict == AuthorizationVerdict.APPROVED
    assert auth_res.is_break_glass is True


def test_break_glass_not_allowed():
    requester = OperatorIdentity(id="op1", roles=[OperatorRole.OPS])
    # Action that doesn't allow break glass
    req = req_manager.create_request(
        SensitiveActionType.DESTRUCTIVE_RETENTION_CLEANUP, requester, "test"
    )

    bg_req = bg_manager.request_break_glass(
        req.id, BreakGlassSeverity.SYSTEM_DOWN, "Need space"
    )

    admin = OperatorIdentity(id="admin", roles=[OperatorRole.ADMIN])

    with pytest.raises(BreakGlassViolation):
        bg_manager.authorize_break_glass(req, admin, bg_req)
