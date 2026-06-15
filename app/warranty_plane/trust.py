from app.warranty_plane.models import WarrantyTrustVerdict as WTVerdictModel
from app.warranty_plane.enums import WarrantyTrustVerdictEnum

class TrustedWarrantyVerdictEngine:
    def evaluate(self, warranty_id: str, facts: dict) -> WTVerdictModel:
        # Evaluate claim clarity, coverage sufficiency, exclusion integrity, etc.
        degraded = facts.get("has_illusory_backing", False) or facts.get("has_failed_cure", False)
        verdict = WarrantyTrustVerdictEnum.DEGRADED if degraded else WarrantyTrustVerdictEnum.TRUSTED
        return WTVerdictModel(
            warranty_id=warranty_id,
            verdict=verdict,
            breakdown={"reason": "eval"}
        )
