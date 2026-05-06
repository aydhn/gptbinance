import uuid
from typing import Dict, Any, List
from app.reliability.models import ReliabilityEvidenceBundle, HealthScorecard


class ReliabilityEvidenceBundleAssembly:
    @staticmethod
    def assemble(
        metrics: Dict[str, Any], scorecards: List[HealthScorecard]
    ) -> ReliabilityEvidenceBundle:
        return ReliabilityEvidenceBundle(
            bundle_id=f"ev_bundle_{uuid.uuid4().hex[:8]}",
            metrics=metrics,
            scorecards=scorecards,
        )
