from typing import Dict, List
from app.semantic_plane.models import LabelRecord

class LabelManager:
    def __init__(self, registry):
        self.registry = registry

    def register_label(self, label: LabelRecord):
        self.registry.register_label(label)

    def get_labels_missing_burdens(self) -> List[LabelRecord]:
        return [l for l in self.registry.labels.values() if not l.burden_notes]
