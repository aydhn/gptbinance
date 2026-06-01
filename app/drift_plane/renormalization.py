from app.drift_plane.models import RenormalizationPrerequisiteRecord
from app.drift_plane.enums import RenormalizationClass
from typing import Dict

class RenormalizationManager:
    def __init__(self):
        self.prerequisites: Dict[str, RenormalizationPrerequisiteRecord] = {}

    def add_prerequisite(self, prereq_id: str, class_type: RenormalizationClass):
        self.prerequisites[prereq_id] = RenormalizationPrerequisiteRecord(
            prereq_id=prereq_id,
            class_type=class_type
        )

    def get_prerequisite(self, prereq_id: str) -> RenormalizationPrerequisiteRecord:
        return self.prerequisites.get(prereq_id)
