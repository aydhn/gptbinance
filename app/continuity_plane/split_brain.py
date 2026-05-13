from typing import Dict, List, Optional
from app.continuity_plane.models import SplitBrainRiskRecord
from app.continuity_plane.exceptions import SplitBrainViolation

class SplitBrainRiskManager:
    def __init__(self):
        self._risks: Dict[str, SplitBrainRiskRecord] = {}

    def record_risk(self, record: SplitBrainRiskRecord) -> None:
        self._risks[record.risk_id] = record

    def get_risk(self, risk_id: str) -> Optional[SplitBrainRiskRecord]:
        return self._risks.get(risk_id)

    def list_risks(self) -> List[SplitBrainRiskRecord]:
        return list(self._risks.values())
