from typing import Dict, List, Optional
from .models import RiskLimitDefinition
from .enums import RiskDomain


class RiskLimitRegistry:
    def __init__(self):
        self._limits: Dict[str, RiskLimitDefinition] = {}

    def register_limit(self, limit: RiskLimitDefinition) -> None:
        self._limits[limit.limit_id] = limit

    def get_limit(self, limit_id: str) -> Optional[RiskLimitDefinition]:
        return self._limits.get(limit_id)

    def get_limits_by_domain(
        self, domain: RiskDomain, target_id: str
    ) -> List[RiskLimitDefinition]:
        return [
            lim
            for lim in self._limits.values()
            if lim.domain == domain and lim.target_id == target_id
        ]

    def all_limits(self) -> List[RiskLimitDefinition]:
        return list(self._limits.values())

    def clear(self) -> None:
        self._limits.clear()


global_limit_registry = RiskLimitRegistry()
