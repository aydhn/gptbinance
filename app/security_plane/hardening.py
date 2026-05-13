from typing import Dict, List, Optional
from app.security_plane.models import HardeningControlRecord

class HardeningManager:
    def __init__(self):
        self._controls: Dict[str, HardeningControlRecord] = {}

    def register_control(self, control: HardeningControlRecord) -> None:
        self._controls[control.control_id] = control

    def get_controls_for_asset(self, asset_id: str) -> List[HardeningControlRecord]:
        return [c for c in self._controls.values() if c.asset_id == asset_id]
