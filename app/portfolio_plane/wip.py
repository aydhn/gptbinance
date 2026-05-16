from typing import Dict, Optional
from app.portfolio_plane.models import WipLimitRecord
from app.portfolio_plane.enums import WIPClass
from app.portfolio_plane.exceptions import InvalidWipStateError, PortfolioStorageError

class WipManager:
    def __init__(self):
        self._records: Dict[str, WipLimitRecord] = {}

    def register(self, record: WipLimitRecord):
        if record.wip_record_id in self._records:
            raise PortfolioStorageError(f"WIP Record {record.wip_record_id} already exists")
        if record.current_wip > record.wip_limit and record.wip_class != WIPClass.OVER_LIMIT:
            raise InvalidWipStateError("WIP limit breached but class is not OVER_LIMIT.")
        self._records[record.wip_record_id] = record

    def get(self, record_id: str) -> Optional[WipLimitRecord]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, WipLimitRecord]:
        return self._records.copy()
