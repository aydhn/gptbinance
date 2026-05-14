from typing import Dict, List, Optional
from pydantic import BaseModel, Field

from app.capacity_plane.models import CapacityResource, CapacityQuota
from app.capacity_plane.exceptions import (
    InvalidCapacityDefinition,
    InvalidQuotaDefinition,
)


class CanonicalCapacityRegistry(BaseModel):
    resources: Dict[str, CapacityResource] = Field(default_factory=dict)
    quotas: Dict[str, CapacityQuota] = Field(default_factory=dict)

    def register_resource(self, resource: CapacityResource) -> None:
        if not resource.resource_id:
            raise InvalidCapacityDefinition("Resource ID cannot be empty.")
        if resource.resource_id in self.resources:
            raise InvalidCapacityDefinition(
                f"Resource {resource.resource_id} already registered."
            )
        self.resources[resource.resource_id] = resource

    def get_resource(self, resource_id: str) -> Optional[CapacityResource]:
        return self.resources.get(resource_id)

    def list_resources(self) -> List[CapacityResource]:
        return list(self.resources.values())

    def register_quota(self, quota: CapacityQuota) -> None:
        if not quota.quota_id:
            raise InvalidQuotaDefinition("Quota ID cannot be empty.")
        if quota.quota_id in self.quotas:
            raise InvalidQuotaDefinition(f"Quota {quota.quota_id} already registered.")

        # Verify resource exists (or is a vendor quota that doesn't map to a strict internal resource)
        # Assuming internal quota must map to a resource
        if quota.resource_id and quota.resource_id not in self.resources:
            pass  # External quotas might not have a direct internal resource mapping yet

        self.quotas[quota.quota_id] = quota

    def get_quota(self, quota_id: str) -> Optional[CapacityQuota]:
        return self.quotas.get(quota_id)

    def list_quotas(self) -> List[CapacityQuota]:
        return list(self.quotas.values())


# Global singleton for the capacity registry
capacity_registry = CanonicalCapacityRegistry()
