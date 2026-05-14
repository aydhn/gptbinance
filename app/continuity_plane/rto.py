from typing import Dict, Optional
from app.continuity_plane.models import RtoTarget

class RtoManager:
    def __init__(self):
        self._targets: Dict[str, RtoTarget] = {}

    def register_target(self, objective_id: str, target: RtoTarget) -> None:
        self._targets[objective_id] = target

    def get_target(self, objective_id: str) -> Optional[RtoTarget]:
        return self._targets.get(objective_id)
