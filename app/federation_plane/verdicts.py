from typing import Dict, List, Optional
from app.federation_plane.models import FederatedVerdictRecord
from app.federation_plane.exceptions import FederationPlaneError


class VerdictManager:
    def __init__(self):
        self._verdicts: Dict[str, FederatedVerdictRecord] = {}

    def register(self, record: FederatedVerdictRecord):
        if not record.verdict_id or not record.proof_notes:
            raise FederationPlaneError(
                "No local-pass==federated-pass shortcut allowed."
            )
        self._verdicts[record.verdict_id] = record

    def get_verdict(self, verdict_id: str) -> Optional[FederatedVerdictRecord]:
        return self._verdicts.get(verdict_id)

    def list_verdicts(self) -> List[FederatedVerdictRecord]:
        return list(self._verdicts.values())
