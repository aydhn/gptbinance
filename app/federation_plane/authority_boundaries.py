from typing import Dict, List, Optional
from app.federation_plane.models import AuthorityBoundaryRecord
from app.federation_plane.exceptions import InvalidBoundaryDefinition


class AuthorityBoundaryManager:
    def __init__(self):
        self._boundaries: Dict[str, AuthorityBoundaryRecord] = {}

    def register(self, record: AuthorityBoundaryRecord):
        if not record.authority_id:
            raise InvalidBoundaryDefinition("No authority ambiguity allowed.")
        self._boundaries[record.authority_id] = record

    def get_boundary(self, authority_id: str) -> Optional[AuthorityBoundaryRecord]:
        return self._boundaries.get(authority_id)

    def list_boundaries(self) -> List[AuthorityBoundaryRecord]:
        return list(self._boundaries.values())
