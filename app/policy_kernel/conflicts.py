from typing import List
from app.policy_kernel.models import PolicyDecisionNode, PolicyConflict
from app.policy_kernel.enums import ConflictClass, PolicyVerdict
import uuid


def detect_conflicts(
    action_type: str, nodes: List[PolicyDecisionNode]
) -> List[PolicyConflict]:
    conflicts = []

    # Check for ALLOW vs BLOCK/HARD_BLOCK
    allows = [
        n for n in nodes if n.verdict == PolicyVerdict.ALLOW and not n.is_overridden
    ]
    blocks = [
        n
        for n in nodes
        if n.verdict in (PolicyVerdict.BLOCK, PolicyVerdict.HARD_BLOCK)
        and not n.is_overridden
    ]

    for a in allows:
        for b in blocks:
            conflicts.append(
                PolicyConflict(
                    conflict_id=str(uuid.uuid4()),
                    action_type=action_type,
                    rule_a_id=a.rule_id,
                    rule_b_id=b.rule_id,
                    conflict_class=ConflictClass.ALLOW_VS_BLOCK,
                    resolution_notes="Block takes precedence over Allow.",
                )
            )

    return conflicts
