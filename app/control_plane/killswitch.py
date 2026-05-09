import uuid
from typing import Dict, List
from app.control_plane.models import KillSwitchRecord
from app.control_plane.enums import KillSwitchClass


class KillSwitchManager:
    def __init__(self):
        self._switches: Dict[str, KillSwitchRecord] = {}

    def engage(
        self, ks_class: KillSwitchClass, actor: str, scope_ref: str
    ) -> KillSwitchRecord:
        record = KillSwitchRecord(
            kill_switch_id=f"KS-{uuid.uuid4().hex[:8]}",
            kill_switch_class=ks_class,
            actor=actor,
            scope_ref=scope_ref,
        )
        self._switches[record.kill_switch_id] = record
        return record

    def release(self, kill_switch_id: str):
        if kill_switch_id in self._switches:
            self._switches[kill_switch_id].is_active = False

    def get_active_switches(self) -> List[KillSwitchRecord]:
        return [ks for ks in self._switches.values() if ks.is_active]
