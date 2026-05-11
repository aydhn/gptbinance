from app.compliance_plane.models import AttestationRecord
from typing import Dict, List
from datetime import datetime, timezone


class AttestationManager:
    def __init__(self):
        self._attestations: Dict[str, AttestationRecord] = {}

    def register_attestation(self, attestation: AttestationRecord) -> None:
        self._attestations[attestation.attestation_id] = attestation

    def update_stale_states(self) -> None:
        now = datetime.now(timezone.utc)
        for att in self._attestations.values():
            if now > att.expires_at:
                att.is_stale = True

    def get_active_attestations(self) -> List[AttestationRecord]:
        return [a for a in self._attestations.values() if not a.is_stale]

    def list_attestations(self) -> List[AttestationRecord]:
        return list(self._attestations.values())
