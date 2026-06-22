from typing import Dict, Any


class InvestigationLinkage:
    @staticmethod
    def bridge_investigation_to_settled(investigation_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        issue_corrected = investigation_posture.get("issue_corrected", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if issue_corrected and not is_settled:
            return {
                "status": "caution",
                "notes": "Issue corrected but not settled. No investigation-safe claim.",
                "investigation_proof_notes": "Corrected settlement issue lacks transfer-finality remediation."
            }

        return {
            "status": "bridged",
            "notes": "Discovered settlement defects remediated.",
            "investigation_proof_notes": "Correction matched with valid settlement instructions."
        }
