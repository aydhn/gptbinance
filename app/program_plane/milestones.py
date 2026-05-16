from typing import Dict, List
from app.program_plane.models import MilestoneRecord
from app.program_plane.exceptions import InvalidMilestoneDefinition

class MilestoneRegistry:
    def __init__(self):
        self._milestones: Dict[str, MilestoneRecord] = {}

    def register(self, record: MilestoneRecord):
        if not record.milestone_id or not record.completion_criteria:
            raise InvalidMilestoneDefinition("Vague milestone definition")
        self._milestones[record.milestone_id] = record

    def list_by_program(self, program_id: str) -> List[MilestoneRecord]:
        return [m for m in self._milestones.values() if m.program_id == program_id]
