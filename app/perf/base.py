from abc import ABC, abstractmethod
from typing import Dict, Any, List
from app.perf.models import PerfRun, ResourceUsageSnapshot, WorkloadResult


class ProfilerBase(ABC):
    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def get_summary(self) -> Dict[str, Any]:
        pass


class BenchmarkRunnerBase(ABC):
    @abstractmethod
    def run(self, workload_name: str, iterations: int) -> WorkloadResult:
        pass


class ResourceSamplerBase(ABC):
    @abstractmethod
    def sample(self) -> ResourceUsageSnapshot:
        pass


class RegressionEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, baseline: PerfRun, target: PerfRun) -> Dict[str, Any]:
        pass
