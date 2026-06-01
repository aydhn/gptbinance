from app.drift_plane.models import DriftDivergenceReport

class DivergenceManager:
    def check_divergence(self, drift_id: str) -> DriftDivergenceReport:
        # Dummy implementation
        return DriftDivergenceReport(
            blast_radius="low"
        )
