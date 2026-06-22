from typing import Dict, Any


class AttestationLinkage:
    @staticmethod
    def bridge_attestation_to_settled(attestation_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_certified = attestation_posture.get("is_certified", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_certified and not is_settled:
            return {
                "status": "caution",
                "notes": "Attestation certified but payout not settled. No attestation-safe claim.",
                "attestation_proof_notes": "Certified payout lacks venue/SSI/finality proof."
            }

        return {
            "status": "bridged",
            "notes": "Certification-linked settlement ready.",
            "attestation_proof_notes": "Certification matched with valid settlement instructions."
        }
