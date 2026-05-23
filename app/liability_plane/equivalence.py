import uuid
from typing import List
from app.liability_plane.models import LiabilityEquivalenceReport
from app.liability_plane.enums import EquivalenceVerdict
from app.liability_plane.repository import LiabilityRepository

class EquivalenceManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def evaluate_equivalence(self, liability_id: str, environments: List[str], verdict: EquivalenceVerdict, notes: List[str]) -> LiabilityEquivalenceReport:
        return LiabilityEquivalenceReport(
            report_id=str(uuid.uuid4()),
            liability_id=liability_id,
            environments=environments,
            verdict=verdict,
            divergence_notes=notes
        )
