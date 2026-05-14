from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

from app.capacity_plane.models import (
    CapacityResource,
    CapacityQuota,
    ReservationRecord,
    AllocationRecord,
    UsageSnapshot,
    SaturationRecord,
    CapacityTrustVerdictModel,
)


class BaseCapacityRegistry(ABC):
    @abstractmethod
    def register_resource(self, resource: CapacityResource) -> None:
        pass

    @abstractmethod
    def get_resource(self, resource_id: str) -> Optional[CapacityResource]:
        pass

    @abstractmethod
    def register_quota(self, quota: CapacityQuota) -> None:
        pass

    @abstractmethod
    def get_quota(self, quota_id: str) -> Optional[CapacityQuota]:
        pass


class BaseAllocationEvaluator(ABC):
    @abstractmethod
    def evaluate_allocation(
        self, allocation: AllocationRecord, usage: UsageSnapshot
    ) -> Dict[str, Any]:
        pass


class BaseSaturationEvaluator(ABC):
    @abstractmethod
    def evaluate_saturation(
        self, resource_id: str, usage: UsageSnapshot, limit: float
    ) -> SaturationRecord:
        pass


class BaseTrustEvaluator(ABC):
    @abstractmethod
    def evaluate_trust(self) -> CapacityTrustVerdictModel:
        pass
