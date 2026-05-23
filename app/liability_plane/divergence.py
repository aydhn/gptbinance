import uuid
from app.liability_plane.models import LiabilityDivergenceReport
from app.liability_plane.repository import LiabilityRepository

class DivergenceManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def log_divergence(self, liability_id: str, divergence_type: str, severity: str, blast_radius: str) -> LiabilityDivergenceReport:
        return LiabilityDivergenceReport(
            report_id=str(uuid.uuid4()),
            liability_id=liability_id,
            divergence_type=divergence_type,
            severity=severity,
            blast_radius=blast_radius
        )
