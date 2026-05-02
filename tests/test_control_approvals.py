from app.control.approvals import manager as app_manager
from app.control.requests import manager as req_manager
from app.control.enums import SensitiveActionType, OperatorRole, ApprovalStatus
from app.control.models import OperatorIdentity


def test_approval_lifecycle():
    requester = OperatorIdentity(id="op1", roles=[OperatorRole.OPS])
    req = req_manager.create_request(
        SensitiveActionType.START_LIVE_SESSION, requester, "test"
    )
    record = app_manager.init_record(req)

    assert record.status == ApprovalStatus.PENDING

    approver1 = OperatorIdentity(id="op2", roles=[OperatorRole.OPS])
    record = app_manager.add_decision(req.id, approver1, True, "LGTM")

    # START_LIVE_SESSION needs 2 approvals
    assert record.status == ApprovalStatus.PENDING

    approver2 = OperatorIdentity(id="op3", roles=[OperatorRole.OPS])
    record = app_manager.add_decision(req.id, approver2, True, "Approved")

    assert record.status == ApprovalStatus.APPROVED


def test_approval_rejection():
    requester = OperatorIdentity(id="op1", roles=[OperatorRole.OPS])
    req = req_manager.create_request(
        SensitiveActionType.START_LIVE_SESSION, requester, "test"
    )
    record = app_manager.init_record(req)

    approver1 = OperatorIdentity(id="op2", roles=[OperatorRole.OPS])
    record = app_manager.add_decision(req.id, approver1, False, "Too risky")

    assert record.status == ApprovalStatus.REJECTED
