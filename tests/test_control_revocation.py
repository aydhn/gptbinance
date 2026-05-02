from app.control.revocation import manager as rev_manager
from app.control.requests import manager as req_manager
from app.control.approvals import manager as app_manager
from app.control.enums import (
    SensitiveActionType,
    OperatorRole,
    RevocationReason,
    ApprovalStatus,
)
from app.control.models import OperatorIdentity


def test_revocation():
    requester = OperatorIdentity(id="op1", roles=[OperatorRole.OPS])
    req = req_manager.create_request(
        SensitiveActionType.START_LIVE_SESSION, requester, "test"
    )
    record = app_manager.init_record(req)

    admin = OperatorIdentity(id="admin", roles=[OperatorRole.ADMIN])
    rev_record = rev_manager.revoke(record, admin, RevocationReason.MANUAL_CANCEL)

    assert record.status == ApprovalStatus.REVOKED
    assert rev_record.request_id == req.id
    assert rev_record.reason == RevocationReason.MANUAL_CANCEL
