from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import TemporaryAuthorityRecord

class TemporaryAuthorityManager:
    def __init__(self):
        self.records: Dict[str, TemporaryAuthorityRecord] = {}

    def get_time_bounded(self) -> List[TemporaryAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "TIME_BOUNDED"]

    def get_event_bounded(self) -> List[TemporaryAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "EVENT_BOUNDED"]

    def get_acting(self) -> List[TemporaryAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "ACTING"]

    def get_expired(self) -> List[TemporaryAuthorityRecord]:
        return [r for r in self.records.values() if r.expired]
