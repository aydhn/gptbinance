from typing import Dict, Any
from app.commitment_plane.models import CommitmentObject

class ReadinessManager:
    @staticmethod
    def evaluate_readiness(commitment: CommitmentObject) -> Dict[str, Any]:
        """Evaluates readiness of a commitment based on specific criteria."""
        readiness = {
            "binding_clarity": "high" if commitment.binding else "low",
            "owner_accountability": "high" if commitment.accountability and commitment.owners else "low",
            "deadline_hygiene": "high" if commitment.deadlines else "low",
            "breach_visibility": "high" if commitment.breaches else "low",
            "discharge_rigor": "high" if commitment.discharges else "low"
        }

        # Calculate overall readiness class
        high_count = sum(1 for v in readiness.values() if v == "high")
        if high_count == 5:
            readiness["overall_class"] = "ready"
        elif high_count >= 3:
            readiness["overall_class"] = "caution"
        else:
            readiness["overall_class"] = "not_ready"

        return readiness
