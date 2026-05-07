from typing import Dict, Optional
from app.feature_plane.models import LabelDefinition


class LabelRegistry:
    def __init__(self):
        self._labels: Dict[str, LabelDefinition] = {}

    def register(self, label: LabelDefinition) -> None:
        self._labels[label.label_id] = label

    def get(self, label_id: str) -> Optional[LabelDefinition]:
        return self._labels.get(label_id)
