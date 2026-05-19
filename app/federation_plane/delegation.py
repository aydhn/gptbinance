from typing import Dict, List, Optional
from app.federation_plane.models import DelegatedAuthorityRecord
from app.federation_plane.exceptions import InvalidDelegatedAuthority


class DelegationManager:
    def __init__(self):
        self._delegations: Dict[str, DelegatedAuthorityRecord] = {}

    def register(self, record: DelegatedAuthorityRecord):
        if not record.delegation_id or not record.bounds:
            raise InvalidDelegatedAuthority("No delegation-without-bounds allowed.")
        self._delegations[record.delegation_id] = record

    def get_delegation(self, delegation_id: str) -> Optional[DelegatedAuthorityRecord]:
        return self._delegations.get(delegation_id)

    def list_delegations(self) -> List[DelegatedAuthorityRecord]:
        return list(self._delegations.values())
