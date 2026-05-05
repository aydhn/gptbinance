import pytest
from app.policy_kernel.storage import store_decision, get_decision
from app.policy_kernel.models import (
    PolicyDecision,
    PolicyContext,
    PolicyEvidenceBundle,
    PolicyDecisionGraph,
)
from app.policy_kernel.enums import PolicyVerdict


def test_storage():
    ctx = PolicyContext(action_type="t", workspace_id="w", profile_id="p", mode="m")
    ev = PolicyEvidenceBundle()
    decision = PolicyDecision(
        decision_id="d1",
        action_type="t",
        context=ctx,
        evidence=ev,
        graph=PolicyDecisionGraph(root_verdict=PolicyVerdict.ALLOW),
        final_verdict=PolicyVerdict.ALLOW,
        winning_rules=[],
        reasoning="Test",
    )
    store_decision(decision)
    assert get_decision("d1") == decision
