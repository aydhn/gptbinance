from abc import ABC, abstractmethod
from typing import Dict, Any


class SourceAdapterBase(ABC):
    @abstractmethod
    def fetch_snapshot(self) -> Dict[str, Any]:
        pass


class TruthEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, context: Any) -> Any:
        pass


class SequenceCheckerBase(ABC):
    @abstractmethod
    def check_integrity(self, events: list) -> Any:
        pass


class ConvergenceCheckerBase(ABC):
    @abstractmethod
    def check_convergence(self, stream_data: Any, snapshot_data: Any) -> Any:
        pass
