from typing import Dict, Optional, List
from app.supply_chain_plane.models import RuntimeLineageRecord


class RuntimeLineageRegistry:
    def __init__(self):
        self._records: Dict[str, RuntimeLineageRecord] = {}

    def register_record(self, record: RuntimeLineageRecord) -> None:
        self._records[record.runtime_id] = record

    def get_record(self, runtime_id: str) -> Optional[RuntimeLineageRecord]:
        return self._records.get(runtime_id)

    def get_records_for_environment(
        self, environment: str
    ) -> List[RuntimeLineageRecord]:
        return [r for r in self._records.values() if r.environment == environment]
