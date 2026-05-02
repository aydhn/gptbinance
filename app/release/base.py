from abc import ABC, abstractmethod
from typing import Optional, Dict, Any


class ReleaseBuilderBase(ABC):
    @abstractmethod
    def build(self) -> Any:
        pass


class HostProbeBase(ABC):
    @abstractmethod
    def run_probe(self) -> Any:
        pass


class MigrationExecutorBase(ABC):
    @abstractmethod
    def execute(self, plan: Any) -> Any:
        pass


class UpgradePlannerBase(ABC):
    @abstractmethod
    def create_plan(self) -> Any:
        pass


class RollbackPlannerBase(ABC):
    @abstractmethod
    def create_plan(self) -> Any:
        pass
