from typing import Dict, List, Optional
from app.security_plane.models import RevocationRecord

class RevocationGovernance:
    def __init__(self):
        self._revocations: Dict[str, RevocationRecord] = {}

    def revoke(self, revocation: RevocationRecord) -> None:
        self._revocations[revocation.revocation_id] = revocation

    def is_revoked(self, target_id: str) -> bool:
        for r in self._revocations.values():
            if r.target_id == target_id:
                return True
        return False
