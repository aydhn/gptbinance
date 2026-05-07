from typing import Dict, Optional
from app.feature_plane.models import TargetDefinition


class TargetRegistry:
    def __init__(self):
        self._targets: Dict[str, TargetDefinition] = {}

    def register(self, target: TargetDefinition) -> None:
        self._targets[target.target_id] = target

    def get(self, target_id: str) -> Optional[TargetDefinition]:
        return self._targets.get(target_id)
