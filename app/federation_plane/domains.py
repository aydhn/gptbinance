from typing import Dict, List, Optional
from app.federation_plane.models import DomainRecord
from app.federation_plane.exceptions import InvalidDomainRecord


class DomainManager:
    def __init__(self):
        self._domains: Dict[str, DomainRecord] = {}

    def register(self, record: DomainRecord):
        if not record.domain_id or not record.owner:
            raise InvalidDomainRecord("No ambiguous domain ownership allowed.")
        self._domains[record.domain_id] = record

    def get_domain(self, domain_id: str) -> Optional[DomainRecord]:
        return self._domains.get(domain_id)

    def list_domains(self) -> List[DomainRecord]:
        return list(self._domains.values())

    def get_orphan_warnings(self) -> List[DomainRecord]:
        return [d for d in self._domains.values() if d.orphan_warnings]
