# stays.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import StayRecord

class StayManager:
    def __init__(self):
        self.stays: Dict[str, StayRecord] = {}

    def enter_stay(self, stay: StayRecord):
        self.stays[stay.stay_id] = stay

    def get_stay(self, stay_id: str) -> Optional[StayRecord]:
        return self.stays.get(stay_id)

    def list_stays(self) -> List[StayRecord]:
        return list(self.stays.values())
