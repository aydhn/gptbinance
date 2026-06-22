from typing import Dict, Any


class AdjudicationLinkage:
    @staticmethod
    def bridge_adjudication_to_settled(adjudication_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        has_award = adjudication_posture.get("has_award", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if has_award and not is_settled:
            return {
                "status": "caution",
                "notes": "Award issued but not settled. No adjudication-safe claim.",
                "adjudication_proof_notes": "Award payment lacks final transfer or reversal analysis."
            }

        return {
            "status": "bridged",
            "notes": "Award settlement ready.",
            "adjudication_proof_notes": "Award matched with valid settlement instructions."
        }
