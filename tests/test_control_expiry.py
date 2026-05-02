import pytest
from datetime import datetime, timezone, timedelta
from app.control.expiry import manager as exp_manager
from app.control.requests import manager as req_manager
from app.control.approvals import manager as app_manager
from app.control.enums import SensitiveActionType, OperatorRole, ApprovalStatus
from app.control.models import OperatorIdentity

def test_expiry():
    requester = OperatorIdentity(id="op1", roles=[OperatorRole.OPS])
    req = req_manager.create_request(SensitiveActionType.START_LIVE_SESSION, requester, "test")
    record = app_manager.init_record(req)

    # Simulate time passing
    req.expires_at = datetime.now(timezone.utc) - timedelta(seconds=10)

    expired = exp_manager.check_and_expire(record)
    assert expired is True
    assert record.status == ApprovalStatus.EXPIRED
