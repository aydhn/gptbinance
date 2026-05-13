from typing import Dict, Optional
from app.continuity_plane.models import RpoTarget

class RpoManager:
    def __init__(self):
        self._targets: Dict[str, RpoTarget] = {}

    def register_target(self, objective_id: str, target: RpoTarget) -> None:
        self._targets[objective_id] = target

    def get_target(self, objective_id: str) -> Optional[RpoTarget]:
        return self._targets.get(objective_id)
