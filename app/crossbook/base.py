from abc import ABC, abstractmethod

class ExposureGraphBuilderBase(ABC):
    @abstractmethod
    def build(self) -> None:
        pass

class NetExposureEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self) -> None:
        pass

class CollateralAnalyzerBase(ABC):
    @abstractmethod
    def analyze(self) -> None:
        pass

class ConflictDetectorBase(ABC):
    @abstractmethod
    def detect(self) -> None:
        pass
