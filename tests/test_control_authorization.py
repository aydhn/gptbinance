from app.control.authorization import engine
from app.control.requests import manager as req_manager
from app.control.approvals import manager as app_manager
from app.control.enums import SensitiveActionType, OperatorRole, AuthorizationVerdict, ApprovalStatus
from app.control.models import OperatorIdentity

def test_authorization_success():
    requester = OperatorIdentity(id="op1", roles=[OperatorRole.OPS])
    req = req_manager.create_request(SensitiveActionType.START_LIVE_SESSION, requester, "test")
    record = app_manager.init_record(req)

    approver1 = OperatorIdentity(id="op2", roles=[OperatorRole.OPS])
    approver2 = OperatorIdentity(id="op3", roles=[OperatorRole.OPS])
    app_manager.add_decision(req.id, approver1, True, "OK")
    record = app_manager.add_decision(req.id, approver2, True, "OK")

    assert record.status == ApprovalStatus.APPROVED

    auth_res = engine.authorize(record)
    assert auth_res.verdict == AuthorizationVerdict.APPROVED

def test_authorization_stale_context():
    requester = OperatorIdentity(id="op1", roles=[OperatorRole.OPS])
    req = req_manager.create_request(SensitiveActionType.START_LIVE_SESSION, requester, "test", run_id="run-A")
    record = app_manager.init_record(req)

    approver1 = OperatorIdentity(id="op2", roles=[OperatorRole.OPS])
    approver2 = OperatorIdentity(id="op3", roles=[OperatorRole.OPS])
    app_manager.add_decision(req.id, approver1, True, "OK")
    record = app_manager.add_decision(req.id, approver2, True, "OK")

    auth_res = engine.authorize(record, execution_context={"run_id": "run-B"})
    assert auth_res.verdict == AuthorizationVerdict.STALE
