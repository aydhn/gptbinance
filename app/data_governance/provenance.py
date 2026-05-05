from typing import Dict, List
from app.data_governance.models import ProvenanceRecord, DatasetRef


class ProvenanceStore:
    def __init__(self):
        self._records: Dict[str, ProvenanceRecord] = {}

    def _key(self, ref: DatasetRef) -> str:
        return f"{ref.dataset_id}:{ref.version}"

    def record_provenance(self, record: ProvenanceRecord) -> None:
        self._records[self._key(record.dataset_ref)] = record

    def get_provenance(self, ref: DatasetRef) -> ProvenanceRecord:
        return self._records.get(self._key(ref))
