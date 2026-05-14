from typing import Dict, Optional, List
from app.supply_chain_plane.models import SbomRecord


class SbomRegistry:
    def __init__(self):
        self._sboms: Dict[str, SbomRecord] = {}

    def register_sbom(self, sbom: SbomRecord) -> None:
        self._sboms[sbom.sbom_id] = sbom

    def get_sbom(self, sbom_id: str) -> Optional[SbomRecord]:
        return self._sboms.get(sbom_id)

    def get_sboms_for_component(self, component_id: str) -> List[SbomRecord]:
        return [
            s
            for s in self._sboms.values()
            if s.component_ref.component_id == component_id
        ]
