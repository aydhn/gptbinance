from typing import Dict, List, Optional
from app.federation_plane.models import TenantRecord
from app.federation_plane.exceptions import InvalidTenantRecord


class TenantManager:
    def __init__(self):
        self._tenants: Dict[str, TenantRecord] = {}

    def register(self, record: TenantRecord):
        if not record.tenant_id:
            raise InvalidTenantRecord("No tenant-blind governance allowed.")
        self._tenants[record.tenant_id] = record

    def get_tenant(self, tenant_id: str) -> Optional[TenantRecord]:
        return self._tenants.get(tenant_id)

    def list_tenants(self) -> List[TenantRecord]:
        return list(self._tenants.values())
