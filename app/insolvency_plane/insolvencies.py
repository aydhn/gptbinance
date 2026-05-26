# insolvencies.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import InsolvencyObject, InsolvencyObjectRef
from app.insolvency_plane.enums import InsolvencyClass

class InsolvencyManager:
    def __init__(self):
        self.insolvencies: Dict[str, InsolvencyObjectRef] = {}

    def add_insolvency(self, insolvency_ref: InsolvencyObjectRef):
        self.insolvencies[insolvency_ref.insolvency_id] = insolvency_ref

    def get_insolvency(self, insolvency_id: str) -> Optional[InsolvencyObjectRef]:
        return self.insolvencies.get(insolvency_id)

    def list_insolvencies(self) -> List[InsolvencyObjectRef]:
        return list(self.insolvencies.values())
