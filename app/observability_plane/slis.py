from typing import Dict, List, Optional
from .models import SliSupportRecord

class SliSupportRegistry:
    def __init__(self):
        self._records: Dict[str, SliSupportRecord] = {}

    def register_sli_support(self, record: SliSupportRecord) -> None:
        self._records[record.sli_id] = record

    def get_sli_support(self, sli_id: str) -> Optional[SliSupportRecord]:
        return self._records.get(sli_id)

    def list_sli_support(self) -> List[SliSupportRecord]:
        return list(self._records.values())
