from typing import Dict, List, Optional
from app.security_plane.models import CredentialStateRecord

class CredentialStateManager:
    def __init__(self):
        self._credentials: Dict[str, CredentialStateRecord] = {}

    def update_state(self, state_record: CredentialStateRecord) -> None:
        self._credentials[state_record.credential_id] = state_record

    def get_state(self, credential_id: str) -> Optional[CredentialStateRecord]:
        return self._credentials.get(credential_id)

    def list_all(self) -> List[CredentialStateRecord]:
        return list(self._credentials.values())
