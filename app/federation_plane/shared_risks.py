from typing import Dict, List, Optional
from app.federation_plane.models import SharedRiskRecord
from app.federation_plane.exceptions import InvalidSharedRiskMapping


class SharedRiskManager:
    def __init__(self):
        self._risks: Dict[str, SharedRiskRecord] = {}

    def register(self, record: SharedRiskRecord):
        if not record.risk_id or not record.burden_notes:
            raise InvalidSharedRiskMapping(
                "No local-only comfort allowed. Burden notes required."
            )
        self._risks[record.risk_id] = record

    def get_risk(self, risk_id: str) -> Optional[SharedRiskRecord]:
        return self._risks.get(risk_id)

    def list_risks(self) -> List[SharedRiskRecord]:
        return list(self._risks.values())
