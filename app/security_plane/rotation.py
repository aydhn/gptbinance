from typing import Dict, List, Optional
from app.security_plane.models import RotationRecord

class RotationGovernance:
    def __init__(self):
        self._rotations: Dict[str, RotationRecord] = {}

    def record_rotation(self, rotation: RotationRecord) -> None:
        self._rotations[rotation.rotation_id] = rotation

    def get_rotation_history(self, target_id: str) -> List[RotationRecord]:
        return [r for r in self._rotations.values() if r.target_id == target_id]
