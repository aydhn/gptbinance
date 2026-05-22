from app.commitment_plane.models import CommitmentObject
from typing import Dict, Any

class QualityManager:
    @staticmethod
    def evaluate_quality(commitment: CommitmentObject) -> Dict[str, Any]:
        return {
            "promise_inflation_warning": False,
            "ownerless_commitment_warning": len(commitment.owners) == 0,
            "silent_extension_warning": False,
            "relief_abuse_warning": False,
            "roadmap_theater_warning": False,
            "discharge_theater_warning": False,
            "quality_verdict": "pass" if len(commitment.owners) > 0 else "fail"
        }
