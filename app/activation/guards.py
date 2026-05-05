from typing import Dict, Any
from app.activation.models import ActivationIntent
from app.activation.exceptions import ActivationPolicyViolation


class ActivationGuards:
    @staticmethod
    def verify_pre_activation(intent: ActivationIntent, system_state: Dict[str, Any]):
        if not intent.board_decision_ref:
            raise ActivationPolicyViolation(
                "No activation without a final board decision ref."
            )

        # Example system state checks
        if system_state.get("market_truth_critical_stale"):
            raise ActivationPolicyViolation(
                "Cannot activate during critical market truth stale state."
            )

        if system_state.get("shadow_drift_critical"):
            raise ActivationPolicyViolation(
                "Cannot activate with unresolved critical shadow drift."
            )

        if system_state.get("capital_freeze_active"):
            raise ActivationPolicyViolation(
                "Cannot activate while capital freeze is active."
            )
