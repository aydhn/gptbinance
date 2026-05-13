from typing import Dict, List, Optional
from app.security_plane.models import CompensatingSecurityControl

class CompensatingControlManager:
    def __init__(self):
        self._controls: Dict[str, CompensatingSecurityControl] = {}

    def register_control(self, control: CompensatingSecurityControl) -> None:
        self._controls[control.control_id] = control

    def get_control(self, control_id: str) -> Optional[CompensatingSecurityControl]:
        return self._controls.get(control_id)
