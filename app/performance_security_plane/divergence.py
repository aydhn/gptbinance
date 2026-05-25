from app.performance_security_plane.models import SecurityDivergenceReport

class DivergenceManager:
    def assess_divergence(self, report_id: str, security_id: str, divergences: list) -> SecurityDivergenceReport:
        return SecurityDivergenceReport(
            report_id=report_id,
            security_id=security_id,
            divergences=divergences
        )
