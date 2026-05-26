# cures.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import CureRecord

class CureManager:
    def __init__(self):
        self.cures: Dict[str, CureRecord] = {}

    def register_cure(self, cure: CureRecord):
        self.cures[cure.cure_id] = cure

    def get_cure(self, cure_id: str) -> Optional[CureRecord]:
        return self.cures.get(cure_id)

    def list_cures(self) -> List[CureRecord]:
        return list(self.cures.values())
