from app.semantic_plane.registry import CanonicalSemanticRegistry
from app.semantic_plane.models import SemanticConflictRecord
from app.semantic_plane.enums import ConflictClass

class StateSemanticManager:
    def __init__(self, registry: CanonicalSemanticRegistry):
        self.registry = registry

    def validate_state_label(self, label_name: str) -> bool:
        # State Plane integration: check if state label has canonical semantic meaning
        matching_labels = [l for l in self.registry.labels.values() if l.name == label_name]
        if not matching_labels:
            conflict = SemanticConflictRecord(
                 conflict_id=f"state_conf_{label_name}",
                 semantic_id="unknown",
                 conflict_class=ConflictClass.SEMANTIC_SPLIT_BRAIN,
                 unresolved_notes=f"State label {label_name} used without canonical semantic definition. Label theater detected."
            )
            self.registry.conflicts[conflict.conflict_id] = conflict
            return False
        return True
