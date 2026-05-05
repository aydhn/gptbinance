import pytest
from datetime import datetime, timezone
from app.policy_kernel.models import (
    PolicyDecision,
    PolicyDecisionGraph,
    PolicyContext,
    PolicyEvidenceBundle,
)
from app.policy_kernel.enums import PolicyVerdict
from app.policy_kernel.proofs import generate_decision_proof


def test_generate_proof():
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
    proof = generate_decision_proof(decision)
    assert "POLICY DECISION PROOF" in proof
    assert "Final Verdict: ALLOW" in proof
