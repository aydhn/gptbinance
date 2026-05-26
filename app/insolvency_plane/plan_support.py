# plan_support.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import PlanSupportRecord

class PlanSupportManager:
    def __init__(self):
        self.supports: Dict[str, PlanSupportRecord] = {}

    def register_support(self, support: PlanSupportRecord):
        self.supports[support.support_id] = support

    def get_support(self, support_id: str) -> Optional[PlanSupportRecord]:
        return self.supports.get(support_id)

    def list_supports(self) -> List[PlanSupportRecord]:
        return list(self.supports.values())
