from typing import Dict, Any


class ExceptionLinkage:
    @staticmethod
    def bridge_exception_to_settled(exception_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        has_waiver = exception_posture.get("has_waiver", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if has_waiver and not is_settled:
            return {
                "status": "caution",
                "notes": "Special handling approved but not settled. No exception-safe claim.",
                "exception_proof_notes": "Special settlement handling has hidden destination or cutoff defects."
            }

        return {
            "status": "bridged",
            "notes": "Exception-conditioned settlement ready.",
            "exception_proof_notes": "Waiver matched with valid settlement instructions."
        }
