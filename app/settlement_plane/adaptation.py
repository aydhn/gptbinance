from typing import Dict, Any


class AdaptationLinkage:
    @staticmethod
    def bridge_adaptation_to_settled(adaptation_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_adapted = adaptation_posture.get("is_adapted", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_adapted and not is_settled:
            return {
                "status": "caution",
                "notes": "Package adapted but not settled. No adaptation-safe claim.",
                "adaptation_proof_notes": "Remedial package transfers have unresolved partial/fail residue."
            }

        return {
            "status": "bridged",
            "notes": "Corrective package settlement ready.",
            "adaptation_proof_notes": "Package matched with valid settlement instructions."
        }
