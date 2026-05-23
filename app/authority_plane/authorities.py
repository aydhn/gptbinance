from typing import Dict, Any, List
# pylint: disable=unused-import
# flake8: noqa, Optional
from .models import AuthorityRecord

class AuthoritiesManager:
    """
    Manages active, suspended, expired, and challenged authorities.
    Strictly avoids shapeless authority or title inflation.
    """
    def __init__(self):
        self.records: Dict[str, AuthorityRecord] = {}

    def register(self, record: AuthorityRecord) -> None:
        self.records[record.authority_id] = record

    def get_active(self) -> List[AuthorityRecord]:
        return [r for r in self.records.values() if r.status == "active"]

    def get_suspended(self) -> List[AuthorityRecord]:
        return [r for r in self.records.values() if r.status == "suspended"]

    def get_expired(self) -> List[AuthorityRecord]:
        return [r for r in self.records.values() if r.status == "expired"]

    def get_challenged(self) -> List[AuthorityRecord]:
        return [r for r in self.records.values() if r.status == "challenged"]

    def get_by_id(self, authority_id: str) -> Optional[AuthorityRecord]:
        return self.records.get(authority_id)
