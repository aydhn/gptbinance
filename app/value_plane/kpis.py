from typing import Dict, List, Optional
from app.value_plane.models import KpiDefinition
from app.value_plane.exceptions import InvalidKpiDefinition

class KpiRegistry:
    def __init__(self):
        self._kpis: Dict[str, KpiDefinition] = {}

    def register(self, kpi: KpiDefinition):
        if not kpi.denominator:
            raise InvalidKpiDefinition("KPI must have a denominator")
        self._kpis[kpi.kpi_id] = kpi

    def get(self, kpi_id: str) -> Optional[KpiDefinition]:
        return self._kpis.get(kpi_id)

    def list_all(self) -> List[KpiDefinition]:
        return list(self._kpis.values())

kpi_registry = KpiRegistry()
