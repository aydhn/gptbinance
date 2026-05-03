from abc import ABC, abstractmethod
from typing import List, Dict, Any
from app.ledger.models import LedgerEntry, LedgerAccount, ReconciliationResult


class LedgerWriterBase(ABC):
    @abstractmethod
    def record_entry(self, entry: LedgerEntry) -> None:
        pass


class ReconciliationEngineBase(ABC):
    @abstractmethod
    def reconcile(
        self, internal_snapshot: Dict[str, float], external_snapshot: Dict[str, float]
    ) -> ReconciliationResult:
        pass


class BalanceExplainerBase(ABC):
    @abstractmethod
    def explain(self, asset: str, scope: str) -> Dict[str, Any]:
        pass
