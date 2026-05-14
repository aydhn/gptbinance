from typing import Dict, Optional
from app.supply_chain_plane.models import OriginTrustRecord


class OriginTrustRegistry:
    def __init__(self):
        self._records: Dict[str, OriginTrustRecord] = {}

    def register_trust_record(self, record: OriginTrustRecord) -> None:
        self._records[record.trust_id] = record

    def get_trust_record(self, trust_id: str) -> Optional[OriginTrustRecord]:
        return self._records.get(trust_id)
