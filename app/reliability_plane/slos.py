from typing import Dict, List, Optional

from .models import SloDefinition


class SloManager:
    def __init__(self, registry):
        self._registry = registry

    def register_slo(self, slo: SloDefinition) -> None:
        self._registry.register_slo(slo)

    def get_slo(self, slo_id: str) -> Optional[SloDefinition]:
        return self._registry.get_slo(slo_id)

    def list_slos(self) -> List[SloDefinition]:
        return self._registry.list_slos()
