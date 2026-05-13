from typing import Dict, List, Optional
from app.continuity_plane.models import StandbyModeRecord

class StandbyManager:
    def __init__(self):
        self._standbys: Dict[str, StandbyModeRecord] = {}

    def update_standby_mode(self, record: StandbyModeRecord) -> None:
        self._standbys[record.service_id] = record

    def get_standby_mode(self, service_id: str) -> Optional[StandbyModeRecord]:
        return self._standbys.get(service_id)

    def list_standby_modes(self) -> List[StandbyModeRecord]:
        return list(self._standbys.values())
