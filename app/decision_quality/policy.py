from typing import List, Dict
from .models import BlockReasonRecord
from .enums import BlockReasonClass


class PolicyFrictionAnalyzer:
    """
    Analyzes friction caused specifically by policy constraints.
    """

    def analyze_policy_friction(
        self, block_reasons: List[BlockReasonRecord]
    ) -> Dict[str, int]:
        """
        Analyzes policy-related block reasons to identify the most restrictive rules.
        """
        policy_frictions = {}

        for reason in block_reasons:
            if reason.reason_class in (
                BlockReasonClass.POLICY_HARD_BLOCK,
                BlockReasonClass.POLICY_BLOCK,
            ):
                # In a real app, reason.description might contain the specific policy invariant name
                # Here we just count occurrences of the description as a proxy
                rule_name = reason.description
                policy_frictions[rule_name] = policy_frictions.get(rule_name, 0) + 1

        return policy_frictions
