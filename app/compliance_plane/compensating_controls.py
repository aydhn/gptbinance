from app.compliance_plane.models import CompensatingControlRecord
from typing import Dict, List
from datetime import datetime, timezone


class CompensatingControlManager:
    def __init__(self):
        self._controls: Dict[str, CompensatingControlRecord] = {}

    def register_control(self, control: CompensatingControlRecord) -> None:
        self._controls[control.compensating_id] = control

    def get_active_controls(self) -> List[CompensatingControlRecord]:
        now = datetime.now(timezone.utc)
        return [c for c in self._controls.values() if now <= c.expires_at]

    def list_controls(self) -> List[CompensatingControlRecord]:
        return list(self._controls.values())
