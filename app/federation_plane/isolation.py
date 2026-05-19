from typing import Dict, List, Optional
from app.federation_plane.models import TenantIsolationRecord
from app.federation_plane.exceptions import FederationPlaneError


class IsolationManager:
    def __init__(self):
        self._records: Dict[str, TenantIsolationRecord] = {}

    def register(self, record: TenantIsolationRecord):
        if not record.isolation_id or not record.proof_notes:
            raise FederationPlaneError("No label-only isolation allowed.")
        self._records[record.isolation_id] = record

    def get_isolation(self, isolation_id: str) -> Optional[TenantIsolationRecord]:
        return self._records.get(isolation_id)

    def list_isolations(self) -> List[TenantIsolationRecord]:
        return list(self._records.values())
