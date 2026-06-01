from app.drift_plane.models import DriftEquivalenceReport
from app.drift_plane.enums import EquivalenceVerdict

class EquivalenceManager:
    def check_equivalence(self, drift_id: str) -> DriftEquivalenceReport:
        # Dummy implementation
        return DriftEquivalenceReport(
            verdict=EquivalenceVerdict.FULLY_EQUIVALENT
        )
