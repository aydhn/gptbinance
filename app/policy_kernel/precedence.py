from typing import List
from app.policy_kernel.models import PolicyDecisionNode
from app.policy_kernel.enums import PolicyVerdict


def resolve_precedence(nodes: List[PolicyDecisionNode]) -> PolicyVerdict:
    """
    Resolves conflicting verdicts based on strict precedence rules:
    HARD_BLOCK > BLOCK > CAUTION > ADVISORY > ALLOW
    """
    if not nodes:
        return PolicyVerdict.ALLOW

    highest_severity = PolicyVerdict.ALLOW

    # Map for easy comparison, higher number = higher precedence
    severity_rank = {
        PolicyVerdict.ALLOW: 0,
        PolicyVerdict.ADVISORY: 1,
        PolicyVerdict.CAUTION: 2,
        PolicyVerdict.BLOCK: 3,
        PolicyVerdict.HARD_BLOCK: 4,
    }

    for node in nodes:
        if not node.is_overridden:
            if severity_rank[node.verdict] > severity_rank[highest_severity]:
                highest_severity = node.verdict

    return highest_severity
