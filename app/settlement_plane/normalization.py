from typing import Dict, Any


class NormalizationLinkage:
    @staticmethod
    def bridge_normalization_to_settled(normalization_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_reopened = normalization_posture.get("is_reopened", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_reopened and not is_settled:
            return {
                "status": "caution",
                "notes": "State reopened but not settled. No normalization-safe claim.",
                "normalization_proof_notes": "Reopened settlement state has stale reversals or hidden fails."
            }

        return {
            "status": "bridged",
            "notes": "Stabilized settlement posture secured.",
            "normalization_proof_notes": "Reopen matched with valid settlement instructions."
        }
