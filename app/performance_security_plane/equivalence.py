from app.performance_security_plane.models import SecurityEquivalenceReport
from app.performance_security_plane.enums import SecurityEquivalenceVerdict

class EquivalenceManager:
    def assess_equivalence(self, report_id: str, security_id: str, verdict: SecurityEquivalenceVerdict, blockers: list) -> SecurityEquivalenceReport:
        return SecurityEquivalenceReport(
            report_id=report_id,
            security_id=security_id,
            verdict=verdict,
            blockers=blockers
        )
