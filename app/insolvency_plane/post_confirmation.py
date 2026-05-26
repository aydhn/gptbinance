# post_confirmation.py
from typing import Dict, List, Optional
from pydantic import BaseModel

class PostConfirmationDutyRecord(BaseModel):
    duty_id: str
    plan_id: str
    description: str
    status: str # pending, performed, missed
    lineage_refs: List[str]

class PostConfirmationManager:
    def __init__(self):
        self.duties: Dict[str, PostConfirmationDutyRecord] = {}

    def register_duty(self, duty: PostConfirmationDutyRecord):
        self.duties[duty.duty_id] = duty

    def get_duty(self, duty_id: str) -> Optional[PostConfirmationDutyRecord]:
        return self.duties.get(duty_id)

    def list_duties(self) -> List[PostConfirmationDutyRecord]:
        return list(self.duties.values())
