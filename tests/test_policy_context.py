import pytest
from app.policy_kernel.context import (
    assemble_policy_context,
    calculate_context_completeness,
)


def test_assemble_context():
    ctx = assemble_policy_context(
        "test_action", "ws_1", "prof_1", "testnet", capital_posture={"ok": True}
    )
    assert ctx.action_type == "test_action"
    assert ctx.capital_posture == {"ok": True}


def test_calculate_completeness():
    ctx = assemble_policy_context(
        "test_action", "ws_1", "prof_1", "testnet", capital_posture={"ok": True}
    )
    score = calculate_context_completeness(ctx)
    assert score > 0
