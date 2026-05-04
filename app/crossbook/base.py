"""
base.py
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from app.crossbook.models import (
    ExposureGraphModel,
    NetExposureSnapshot,
    CollateralPressureReport,
    CrossBookConflict,
    BookPositionRef,
)


class ExposureGraphBuilderBase(ABC):
    @abstractmethod
    def build(self, positions: List[BookPositionRef]) -> ExposureGraphModel:
        pass


class NetExposureEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, graph: ExposureGraphModel) -> NetExposureSnapshot:
        pass


class CollateralAnalyzerBase(ABC):
    @abstractmethod
    def analyze(self, graph: ExposureGraphModel) -> CollateralPressureReport:
        pass


class ConflictDetectorBase(ABC):
    @abstractmethod
    def detect(
        self, graph: ExposureGraphModel, net_exposure: NetExposureSnapshot
    ) -> List[CrossBookConflict]:
        pass


class StandardOutputMixin:
    def standard_metadata(self) -> Dict[str, Any]:
        return {"version": "1.0", "module": self.__class__.__name__}
