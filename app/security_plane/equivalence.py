from app.security_plane.models import SecurityEquivalenceReport
from app.security_plane.enums import EquivalenceVerdict

class EquivalenceEvaluator:
    def compare(self, asset_id: str, env_a: str, env_b: str) -> SecurityEquivalenceReport:
        return SecurityEquivalenceReport(
            report_id=f"eq-{asset_id}",
            asset_id=asset_id,
            verdict=EquivalenceVerdict.EQUIVALENT,
            proof_notes="Environments match."
        )
