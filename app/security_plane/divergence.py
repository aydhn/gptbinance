from app.security_plane.models import SecurityDivergenceReport

class DivergenceEvaluator:
    def evaluate(self, asset_id: str) -> SecurityDivergenceReport:
        return SecurityDivergenceReport(
            report_id=f"div-{asset_id}",
            severity="low",
            divergence_details="No significant divergence."
        )
