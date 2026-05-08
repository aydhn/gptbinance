from abc import ABC, abstractmethod
from typing import List
from app.simulation_plane.models import (
    SimulationRun,
    AssumptionManifest,
    SimulationPartition,
    SimulationTrustVerdict,
)


class RunRegistryBase(ABC):
    @abstractmethod
    def register_run(self, run: SimulationRun) -> None:
        pass

    @abstractmethod
    def get_run(self, run_id: str) -> SimulationRun:
        pass


class AssumptionEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, manifest: AssumptionManifest) -> List[str]:
        pass


class PartitionEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, partitions: List[SimulationPartition]) -> List[str]:
        pass


class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, run_id: str) -> SimulationTrustVerdict:
        pass
