import pytest
from app.policy_kernel.models import PolicyDecisionNode
from app.policy_kernel.enums import PolicyVerdict, ConflictClass
from app.policy_kernel.conflicts import detect_conflicts


def test_detect_conflicts():
    nodes = [
        PolicyDecisionNode(
            rule_id="R1", verdict=PolicyVerdict.ALLOW, evidence_used=[], reasoning=""
        ),
        PolicyDecisionNode(
            rule_id="R2", verdict=PolicyVerdict.BLOCK, evidence_used=[], reasoning=""
        ),
    ]
    conflicts = detect_conflicts("test", nodes)
    assert len(conflicts) == 1
    assert conflicts[0].conflict_class == ConflictClass.ALLOW_VS_BLOCK
