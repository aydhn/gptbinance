import pytest
from app.policy_kernel.models import PolicyDecisionNode
from app.policy_kernel.enums import PolicyVerdict
from app.policy_kernel.precedence import resolve_precedence


def test_precedence_resolution():
    nodes = [
        PolicyDecisionNode(
            rule_id="R1", verdict=PolicyVerdict.ALLOW, evidence_used=[], reasoning=""
        ),
        PolicyDecisionNode(
            rule_id="R2", verdict=PolicyVerdict.BLOCK, evidence_used=[], reasoning=""
        ),
        PolicyDecisionNode(
            rule_id="R3", verdict=PolicyVerdict.CAUTION, evidence_used=[], reasoning=""
        ),
    ]

    assert resolve_precedence(nodes) == PolicyVerdict.BLOCK

    nodes.append(
        PolicyDecisionNode(
            rule_id="INV1",
            verdict=PolicyVerdict.HARD_BLOCK,
            evidence_used=[],
            reasoning="",
        )
    )
    assert resolve_precedence(nodes) == PolicyVerdict.HARD_BLOCK
