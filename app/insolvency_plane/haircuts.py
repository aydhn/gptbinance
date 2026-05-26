# haircuts.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import HaircutRecord

class HaircutManager:
    def __init__(self):
        self.haircuts: Dict[str, HaircutRecord] = {}

    def register_haircut(self, haircut: HaircutRecord):
        self.haircuts[haircut.haircut_id] = haircut

    def get_haircut(self, haircut_id: str) -> Optional[HaircutRecord]:
        return self.haircuts.get(haircut_id)

    def list_haircuts(self) -> List[HaircutRecord]:
        return list(self.haircuts.values())
