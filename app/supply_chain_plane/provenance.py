from typing import Dict, Optional, List
from app.supply_chain_plane.models import BuildProvenanceRecord, ComponentRef


class ProvenanceRegistry:
    def __init__(self):
        self._records: Dict[str, BuildProvenanceRecord] = {}

    def register_provenance(self, record: BuildProvenanceRecord) -> None:
        self._records[record.provenance_id] = record

    def get_provenance(self, provenance_id: str) -> Optional[BuildProvenanceRecord]:
        return self._records.get(provenance_id)

    def get_provenance_for_component(
        self, component_id: str
    ) -> Optional[BuildProvenanceRecord]:
        for record in self._records.values():
            if record.output_ref.component_id == component_id:
                return record
        return None
