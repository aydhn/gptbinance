from app.control.policies import engine
from app.control.models import OperatorIdentity, ApprovalDecision
from app.control.enums import OperatorRole, SensitiveActionType
from app.control.requests import manager as req_manager
from app.control.approvals import manager as app_manager


def test_four_eyes_policy():
    requester = OperatorIdentity(id="op1", roles=[OperatorRole.OPS])
    req = req_manager.create_request(
        SensitiveActionType.START_LIVE_SESSION, requester, "test"
    )
    record = app_manager.init_record(req)

    # Self-approval
    record.decisions.append(
        ApprovalDecision(
            request_id=req.id,
            approver=requester,
            approved=True,
            timestamp=req.created_at,
        )
    )
    assert engine.evaluate_four_eyes(req, record) is False

    # Different approver
    approver = OperatorIdentity(id="op2", roles=[OperatorRole.OPS])
    record.decisions.clear()
    record.decisions.append(
        ApprovalDecision(
            request_id=req.id,
            approver=approver,
            approved=True,
            timestamp=req.created_at,
        )
    )
    assert engine.evaluate_four_eyes(req, record) is True


def test_duplicate_approval_policy():
    requester = OperatorIdentity(id="op1", roles=[OperatorRole.OPS])
    req = req_manager.create_request(
        SensitiveActionType.START_LIVE_SESSION, requester, "test"
    )
    record = app_manager.init_record(req)

    approver = OperatorIdentity(id="op2", roles=[OperatorRole.OPS])
    record.decisions.append(
        ApprovalDecision(
            request_id=req.id,
            approver=approver,
            approved=True,
            timestamp=req.created_at,
        )
    )
    record.decisions.append(
        ApprovalDecision(
            request_id=req.id,
            approver=approver,
            approved=True,
            timestamp=req.created_at,
        )
    )

    assert engine.check_duplicate_approvals(record) is False
