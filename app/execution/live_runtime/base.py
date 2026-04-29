from abc import ABC, abstractmethod
from typing import Optional
from app.execution.live_runtime.models import (
    LiveAccountSnapshot,
    LiveFlattenRequest,
    LiveFlattenResult,
    LiveAuditRecord,
)


class AccountSyncBase(ABC):
    @abstractmethod
    def fetch_snapshot(self, run_id: str) -> LiveAccountSnapshot:
        pass

    @abstractmethod
    def hydrate(self, run_id: str) -> None:
        pass


class FlattenControllerBase(ABC):
    @abstractmethod
    def execute_flatten(self, request: LiveFlattenRequest) -> LiveFlattenResult:
        pass


class AuditWriterBase(ABC):
    @abstractmethod
    def write_record(self, record: LiveAuditRecord) -> None:
        pass
