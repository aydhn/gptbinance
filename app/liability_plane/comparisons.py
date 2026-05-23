import uuid
from typing import List
from app.liability_plane.models import LiabilityComparisonRecord
from app.liability_plane.repository import LiabilityRepository

class ComparisonManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def compare(self, target_id: str, comparison_type: str, findings: List[str]) -> LiabilityComparisonRecord:
        return LiabilityComparisonRecord(
            comparison_id=str(uuid.uuid4()),
            target_id=target_id,
            comparison_type=comparison_type,
            findings=findings
        )
