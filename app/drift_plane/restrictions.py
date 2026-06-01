from app.drift_plane.models import RestrictionReimpositionRecord
from app.drift_plane.enums import RestrictionClass
from typing import Dict
from datetime import datetime

class RestrictionManager:
    def __init__(self):
        self.restrictions: Dict[str, RestrictionReimpositionRecord] = {}

    def add_restriction(self, restriction_id: str, class_type: RestrictionClass):
        self.restrictions[restriction_id] = RestrictionReimpositionRecord(
            restriction_id=restriction_id,
            class_type=class_type,
            reimposed_at=datetime.utcnow()
        )

    def get_restriction(self, restriction_id: str) -> RestrictionReimpositionRecord:
        return self.restrictions.get(restriction_id)
