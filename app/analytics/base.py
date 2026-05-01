from abc import ABC, abstractmethod
from typing import Any
from app.analytics.models import AnalyticsRun


class AttributionAnalyzerBase(ABC):
    @abstractmethod
    def analyze(self, run: AnalyticsRun, data: Any) -> Any:
        pass


class DivergenceAnalyzerBase(ABC):
    @abstractmethod
    def analyze(self, run: AnalyticsRun, data: Any) -> Any:
        pass


class JournalBuilderBase(ABC):
    @abstractmethod
    def build(self, run_id: str, data: Any) -> Any:
        pass


class DiagnosticEngineBase(ABC):
    @abstractmethod
    def run_diagnostics(self, run: AnalyticsRun, data: Any) -> Any:
        pass
