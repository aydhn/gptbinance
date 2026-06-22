from typing import Dict, Any


class OrchestrationLinkage:
    @staticmethod
    def bridge_orchestration_to_settled(orchestration_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_remediated = orchestration_posture.get("is_remediated", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_remediated and not is_settled:
            return {
                "status": "caution",
                "notes": "Flow remediated but not settled. No orchestration-safe claim.",
                "orchestration_proof_notes": "Automated matching/funding/settlement has hidden fail branches."
            }

        return {
            "status": "bridged",
            "notes": "Flow-bound settlement actions ready.",
            "orchestration_proof_notes": "Remediation matched with valid settlement instructions."
        }
