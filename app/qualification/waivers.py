from typing import Dict, List
from datetime import datetime, timezone
from app.qualification.models import WaiverRecord
from app.qualification.enums import WaiverStatus

# In-memory mock storage
_WAIVER_STORE: Dict[str, WaiverRecord] = {}


class WaiverManager:
    def add_waiver(self, record: WaiverRecord):
        _WAIVER_STORE[record.waiver_id] = record

    def get_active_waiver_for_finding(self, finding_id: str) -> WaiverRecord | None:
        for w in _WAIVER_STORE.values():
            if w.finding_id == finding_id and w.status == WaiverStatus.ACTIVE:
                if w.expires_at > datetime.now(timezone.utc):
                    return w
                else:
                    w.status = WaiverStatus.EXPIRED
        return None

    def list_all_waivers(self) -> List[WaiverRecord]:
        return list(_WAIVER_STORE.values())
