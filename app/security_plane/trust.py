from app.security_plane.models import SecurityTrustVerdict
from app.security_plane.enums import SecurityTrustVerdictEnum

class TrustEvaluator:
    def evaluate_trust(self, asset_id: str) -> SecurityTrustVerdict:
        return SecurityTrustVerdict(
            asset_id=asset_id,
            verdict=SecurityTrustVerdictEnum.TRUSTED,
            factors={"patch_hygiene": "good", "no_critical_exposures": True}
        )
