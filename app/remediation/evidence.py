from typing import Dict, Any, Optional
from datetime import datetime, timezone
from app.remediation.models import RemediationPack, ApplyResult


class EvidenceBundle:
    def __init__(self, pack: RemediationPack):
        self.pack_id = pack.pack_id
        self.finding_ref = pack.finding_ref.model_dump()
        self.recipe_name = pack.recipe.name
        self.created_at = datetime.now(timezone.utc)
        self.apply_result: Optional[Dict[str, Any]] = None
        self.verification_result: Optional[Dict[str, Any]] = None

    def attach_apply_result(self, result: ApplyResult):
        self.apply_result = result.model_dump()

    def attach_verification_result(self, result: Any):
        self.verification_result = result.model_dump()

    def summarize(self) -> Dict[str, Any]:
        return {
            "pack_id": self.pack_id,
            "created_at": self.created_at.isoformat(),
            "has_apply_result": self.apply_result is not None,
            "has_verification": self.verification_result is not None,
        }
