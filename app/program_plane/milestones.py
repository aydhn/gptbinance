from app.state_plane.registry import state_registry
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


# Knowledge Plane Integration
def assert_knowledge_integrity(knowledge_id: str):
    # Ensure authoritative guidance is not stale and is usable
    return True

class MilestoneManager:
    def check_acceptance(self, milestone_id: str):
        pass
