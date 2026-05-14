from typing import Dict, Optional, List
from app.supply_chain_plane.models import VerificationRecord


class VerificationRegistry:
    def __init__(self):
        self._verifications: Dict[str, VerificationRecord] = {}

    def register_verification(self, verification: VerificationRecord) -> None:
        self._verifications[verification.verification_id] = verification

    def get_verification(self, verification_id: str) -> Optional[VerificationRecord]:
        return self._verifications.get(verification_id)

    def get_verifications_for_artifact(
        self, artifact_id: str
    ) -> List[VerificationRecord]:
        return [
            v
            for v in self._verifications.values()
            if v.artifact_ref.component_id == artifact_id
        ]
