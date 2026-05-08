from typing import Dict, Optional, List
from app.model_plane.models import AbstentionPolicy, UncertaintyRecord
from app.model_plane.enums import UncertaintyClass
from app.model_plane.exceptions import ModelPlaneError


class AbstentionPolicyHandler:
    def __init__(self):
        self._policies: Dict[str, AbstentionPolicy] = {}

    def register_policy(self, policy: AbstentionPolicy) -> None:
        if not policy.policy_id:
            raise ModelPlaneError("Policy ID is required.")
        if not policy.model_id:
            raise ModelPlaneError("Model ID is required.")

        self._policies[policy.policy_id] = policy

    def get_policy(self, policy_id: str) -> Optional[AbstentionPolicy]:
        return self._policies.get(policy_id)

    def evaluate_abstention(
        self,
        policy_id: str,
        uncertainty_record: Optional[UncertaintyRecord],
        market_truth_degraded: bool,
    ) -> tuple[bool, List[str]]:
        """Returns True if the model should abstain, along with the reasons."""
        policy = self.get_policy(policy_id)
        if not policy:
            return False, []

        reasons = []
        should_abstain = False

        if policy.allow_reject:
            if market_truth_degraded:
                should_abstain = True
                reasons.append("Market truth is degraded")

            if uncertainty_record:
                if (
                    uncertainty_record.uncertainty_class
                    == UncertaintyClass.LOW_CONFIDENCE
                ):
                    should_abstain = True
                    reasons.append("Low confidence")

            else:
                should_abstain = True
                reasons.append("No uncertainty record found")

        return should_abstain, reasons
