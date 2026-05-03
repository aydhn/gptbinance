import uuid
from typing import List, Dict, Any
from datetime import datetime, timezone
from app.events.base import EventSourceAdapterBase
from app.events.enums import EventFreshness


class DummyMacroCalendarAdapter(EventSourceAdapterBase):
    def fetch_events(self) -> List[Dict[str, Any]]:
        # Free/meşru mock veri, scraping yok
        return [
            {
                "id": str(uuid.uuid4()),
                "title": "US CPI Release",
                "time": datetime.now(timezone.utc).isoformat(),
                "importance": "High",
                "country": "US",
            }
        ]

    def get_source_health(self) -> Dict[str, Any]:
        return {"status": "ok", "freshness": EventFreshness.FRESH.value}


class ExchangeMaintenanceAdapter(EventSourceAdapterBase):
    def fetch_events(self) -> List[Dict[str, Any]]:
        return []

    def get_source_health(self) -> Dict[str, Any]:
        return {"status": "ok", "freshness": EventFreshness.FRESH.value}


class InternalSystemEventAdapter(EventSourceAdapterBase):
    def fetch_events(self) -> List[Dict[str, Any]]:
        return []

    def get_source_health(self) -> Dict[str, Any]:
        return {"status": "ok", "freshness": EventFreshness.FRESH.value}


class ManualEventAdapter(EventSourceAdapterBase):
    def fetch_events(self) -> List[Dict[str, Any]]:
        return []

    def get_source_health(self) -> Dict[str, Any]:
        return {"status": "ok", "freshness": EventFreshness.FRESH.value}
