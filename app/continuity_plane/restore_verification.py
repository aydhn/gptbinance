from typing import Dict, List, Optional
from app.continuity_plane.models import RestoreVerificationRecord
from app.continuity_plane.exceptions import RestoreVerificationViolation

class RestoreVerificationManager:
    def __init__(self):
        self._verifications: Dict[str, RestoreVerificationRecord] = {}

    def record_verification(self, record: RestoreVerificationRecord) -> None:
        self._verifications[record.verification_id] = record

    def get_verification(self, verification_id: str) -> Optional[RestoreVerificationRecord]:
        return self._verifications.get(verification_id)

    def list_verifications(self) -> List[RestoreVerificationRecord]:
        return list(self._verifications.values())
