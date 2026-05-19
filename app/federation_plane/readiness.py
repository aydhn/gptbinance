from typing import Dict, List, Optional
from app.federation_plane.models import FederationTrustVerdict
from app.federation_plane.exceptions import FederationPlaneError


class ReadinessManager:
    def __init__(self):
        self._verdicts: Dict[str, FederationTrustVerdict] = {}

    def register(self, record: FederationTrustVerdict):
        if not record.verdict_id or not record.breakdown:
            raise FederationPlaneError("Breakdown mandatory for readiness verdict.")
        self._verdicts[record.verdict_id] = record

    def get_readiness(self, verdict_id: str) -> Optional[FederationTrustVerdict]:
        return self._verdicts.get(verdict_id)

    def list_readiness(self) -> List[FederationTrustVerdict]:
        return list(self._verdicts.values())
