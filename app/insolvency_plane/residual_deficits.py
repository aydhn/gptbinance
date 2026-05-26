# residual_deficits.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import ResidualDeficitRecord

class ResidualDeficitManager:
    def __init__(self):
        self.deficits: Dict[str, ResidualDeficitRecord] = {}

    def register_deficit(self, deficit: ResidualDeficitRecord):
        self.deficits[deficit.deficit_id] = deficit

    def get_deficit(self, deficit_id: str) -> Optional[ResidualDeficitRecord]:
        return self.deficits.get(deficit_id)

    def list_deficits(self) -> List[ResidualDeficitRecord]:
        return list(self.deficits.values())
