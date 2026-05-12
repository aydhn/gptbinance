from typing import Dict, List, Optional

from .models import SliDefinition


class SliManager:
    def __init__(self, registry):
        self._registry = registry

    def register_sli(self, sli: SliDefinition) -> None:
        self._registry.register_sli(sli)

    def get_sli(self, sli_id: str) -> Optional[SliDefinition]:
        return self._registry.get_sli(sli_id)

    def list_slis(self) -> List[SliDefinition]:
        return self._registry.list_slis()
