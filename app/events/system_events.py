from app.events.base import EventSourceAdapterBase
from typing import List, Dict, Any

from app.events.enums import EventFreshness


class SystemEventAdapter(EventSourceAdapterBase):
    def fetch_events(self) -> List[Dict[str, Any]]:
        # Dummy system events
        return []

    def get_source_health(self) -> Dict[str, Any]:
        return {"status": "ok", "freshness": EventFreshness.FRESH.value}
