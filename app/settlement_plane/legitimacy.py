from typing import Dict, Any


class LegitimacyLinkage:
    @staticmethod
    def bridge_legitimacy_to_settled(legitimacy_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_fair = legitimacy_posture.get("is_fair", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_fair and not is_settled:
            return {
                "status": "caution",
                "notes": "Fairness intended but not settled. No legitimacy-safe claim.",
                "legitimacy_proof_notes": "Beneficiary payment has wrong-destination or duplication bias."
            }

        return {
            "status": "bridged",
            "notes": "Stakeholder-fair settlement posture secured.",
            "legitimacy_proof_notes": "Reparation matched with valid settlement instructions."
        }
