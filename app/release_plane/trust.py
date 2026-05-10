from app.release_plane.models import ReleaseTrustVerdict, ReleaseCandidateRef
from app.release_plane.enums import TrustVerdict
from typing import Dict, Any
import uuid

class ReleaseTrustEngine:
    def synthesize_verdict(self, candidate_id: str, quality_report: Any, equivalence_report: Any) -> ReleaseTrustVerdict:
        factors = {
            "quality_passed": getattr(quality_report, "passed", False),
            "equivalence_verdict": getattr(equivalence_report, "verdict", "unknown"),
        }

        verdict = TrustVerdict.TRUSTED

        if not factors["quality_passed"]:
             verdict = TrustVerdict.CAUTION

        if factors["equivalence_verdict"] != "equivalent":
             verdict = TrustVerdict.DEGRADED

        # Add blocked / review_required rules based on context
        if "Missing Pins" in getattr(quality_report, "issues", []):
             verdict = TrustVerdict.BLOCKED

        return ReleaseTrustVerdict(
            verdict_id=f"trust-{uuid.uuid4().hex[:8]}",
            candidate_ref=ReleaseCandidateRef(candidate_id=candidate_id),
            verdict=verdict,
            factors=factors
        )
