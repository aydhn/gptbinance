from app.release_plane.models import HotfixRecord, ReleaseCandidateRef
from app.release_plane.enums import HotfixClass
from app.release_plane.exceptions import HotfixViolation
from typing import Dict, Any
import uuid

class HotfixManager:
    def create_hotfix(self, candidate_id: str, hotfix_class: HotfixClass, scope_limits: Dict[str, Any], review_debt: str) -> HotfixRecord:
        # Enforce hotfix governance
        if not review_debt:
             raise HotfixViolation("Hotfix must have documented review debt mapping back to normal release train.")

        if not scope_limits:
             raise HotfixViolation("Emergency hotfixes must have explicit scope limits. No unbounded permanent hotfixes allowed.")

        return HotfixRecord(
            hotfix_id=f"hf-{uuid.uuid4().hex[:8]}",
            hotfix_class=hotfix_class,
            candidate_ref=ReleaseCandidateRef(candidate_id=candidate_id),
            scope_limits=scope_limits,
            review_debt=review_debt,
            proof_notes="Hotfix instantiated under emergency governance rules."
        )
