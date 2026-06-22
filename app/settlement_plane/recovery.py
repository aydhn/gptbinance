from typing import Dict, Any


class RecoveryLinkage:
    @staticmethod
    def bridge_recovery_to_settled(recovery_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_finalized = recovery_posture.get("is_finalized", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_finalized and not is_settled:
            return {
                "status": "caution",
                "notes": "Recovery finalized but not settled. No recovery-safe claim.",
                "recovery_proof_notes": "Recovered value has no beneficiary-final transfer posture."
            }

        return {
            "status": "bridged",
            "notes": "Recovery-flow settlement ready.",
            "recovery_proof_notes": "Finalization matched with valid settlement instructions."
        }
