from typing import Dict, Any


class MetaGovernanceLinkage:
    @staticmethod
    def bridge_meta_governance_to_settled(meta_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_corrected = meta_posture.get("is_corrected", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_corrected and not is_settled:
            return {
                "status": "caution",
                "notes": "Canon corrected but not settled. No canon-safe claim.",
                "meta_governance_proof_notes": "Rule migration has broken instruction or SSI history."
            }

        return {
            "status": "bridged",
            "notes": "Canon-controlled settlement rules ready.",
            "meta_governance_proof_notes": "Canon correction matched with valid settlement instructions."
        }
