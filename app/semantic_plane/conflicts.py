from typing import List
from app.semantic_plane.models import SemanticConflictRecord

class ConflictManager:
    def __init__(self, registry):
        self.registry = registry

    def register_conflict(self, conflict: SemanticConflictRecord):
        self.registry.conflicts[conflict.conflict_id] = conflict

    def get_unresolved_conflicts(self) -> List[SemanticConflictRecord]:
        # Return all for now; later we'd filter by status
        return list(self.registry.conflicts.values())
