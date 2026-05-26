# plan_classes.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import PlanClassRecord

class PlanClassManager:
    def __init__(self):
        self.classes: Dict[str, PlanClassRecord] = {}

    def add_plan_class(self, plan_class: PlanClassRecord):
        self.classes[plan_class.class_id] = plan_class

    def get_plan_class(self, class_id: str) -> Optional[PlanClassRecord]:
        return self.classes.get(class_id)

    def list_plan_classes(self) -> List[PlanClassRecord]:
        return list(self.classes.values())
