from typing import Dict, Any


class ViabilityLinkage:
    @staticmethod
    def bridge_viability_to_settled(viability_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_viable = viability_posture.get("is_viable", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_viable and not is_settled:
            return {
                "status": "caution",
                "notes": "Restructuring intended but not settled. No viability-safe claim.",
                "viability_proof_notes": "Viable-looking settlement channel has chronic fail or bank fragility."
            }

        return {
            "status": "bridged",
            "notes": "Transfer-channel viability secured.",
            "viability_proof_notes": "Restructuring matched with valid settlement instructions."
        }
