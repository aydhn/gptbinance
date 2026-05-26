# plans.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import PlanRecord

class PlanManager:
    def __init__(self):
        self.plans: Dict[str, PlanRecord] = {}

    def propose_plan(self, plan: PlanRecord):
        self.plans[plan.plan_id] = plan

    def get_plan(self, plan_id: str) -> Optional[PlanRecord]:
        return self.plans.get(plan_id)

    def list_plans(self) -> List[PlanRecord]:
        return list(self.plans.values())
