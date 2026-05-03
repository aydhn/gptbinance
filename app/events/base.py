from abc import ABC, abstractmethod
from typing import List
from datetime import datetime
from app.events.models import EventRecord, EventRiskOverlay


class EventSourceAdapterBase(ABC):
    @abstractmethod
    def fetch_events(self) -> List[dict]:
        pass

    @abstractmethod
    def get_source_health(self) -> dict:
        pass


class EventNormalizerBase(ABC):
    @abstractmethod
    def normalize(self, raw_events: List[dict]) -> List[EventRecord]:
        pass


class EventOverlayEngineBase(ABC):
    @abstractmethod
    def generate_overlay(
        self, events: List[EventRecord], profile_id: str
    ) -> EventRiskOverlay:
        pass


class CalendarProviderBase(ABC):
    @abstractmethod
    def get_calendar(
        self, start_time: datetime, end_time: datetime
    ) -> List[EventRecord]:
        pass
