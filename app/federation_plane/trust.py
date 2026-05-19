from typing import Dict, List, Optional
from app.federation_plane.models import FederationTrustVerdict
from app.federation_plane.exceptions import FederationPlaneError


class TrustEngine:
    def __init__(self):
        self._verdicts: Dict[str, FederationTrustVerdict] = {}

    def synthesize(self, verdict: FederationTrustVerdict):
        if not verdict.breakdown:
            raise FederationPlaneError("Trust verdict synthesis requires breakdown.")
        self._verdicts[verdict.verdict_id] = verdict

    def get_verdict(self, verdict_id: str) -> Optional[FederationTrustVerdict]:
        return self._verdicts.get(verdict_id)

    def list_verdicts(self) -> List[FederationTrustVerdict]:
        return list(self._verdicts.values())
