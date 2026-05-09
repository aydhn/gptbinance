import pytest
from app.control_plane.repository import ControlPlaneRepository
from app.control_plane.models import ActionRequest, ApprovalDecision
from app.control_plane.enums import CommandClass, ScopeClass, KillSwitchClass
from app.control_plane.exceptions import ControlPlaneError

def test_command_registry():
    repo = ControlPlaneRepository()
    cmds = repo.registry.list_commands()
    assert len(cmds) > 0
    assert any(c.command_id == CommandClass.FREEZE_SYMBOL for c in cmds)

def test_preview_and_apply_flow():
    repo = ControlPlaneRepository()
    req = ActionRequest(
        action_id="ACT-123",
        command_id=CommandClass.PAUSE_WORKFLOW,
        actor="operator_1",
        scope_class=ScopeClass.GLOBAL,
        scope_ref="ALL",
        intent="Stop for review",
        payload={}
    )

    # 1. Preview
    preview = repo.preview_engine.generate_preview(req)
    assert preview.action_id == "ACT-123"

    # 2. Approval
    decision = ApprovalDecision(action_id="ACT-123", approver="admin_1", is_approved=True, rationale="Looks ok")
    repo.approval_engine.record_decision(decision)

    is_approved = repo.approval_engine.is_approved("ACT-123")
    assert is_approved is True

    # 3. Apply
    receipt = repo.apply_engine.apply_action(req, is_approved=is_approved)
    assert receipt.apply_outcome == "SUCCESS"

def test_apply_without_approval_fails():
    repo = ControlPlaneRepository()
    req = ActionRequest(
        action_id="ACT-999",
        command_id=CommandClass.FREEZE_SYMBOL,
        actor="operator_1",
        scope_class=ScopeClass.SYMBOL,
        scope_ref="BTCUSDT",
        intent="Test fail",
        payload={}
    )
    with pytest.raises(ControlPlaneError):
        repo.apply_engine.apply_action(req, is_approved=False)

def test_kill_switches():
    repo = ControlPlaneRepository()
    repo.kill_switches.engage(KillSwitchClass.EXECUTION_GLOBAL, "admin_override", "LIVE")
    switches = repo.kill_switches.get_active_switches()
    assert len(switches) == 1
    assert switches[0].actor == "admin_override"

def test_trust_verdict():
    repo = ControlPlaneRepository()
    verdict = repo.trust_evaluator.evaluate(unapproved_actions=0)
    assert verdict.verdict.value == "trusted"

    verdict_degraded = repo.trust_evaluator.evaluate(unapproved_actions=2)
    assert verdict_degraded.verdict.value == "degraded"
