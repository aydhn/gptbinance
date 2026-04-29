import abc
from typing import Any


class SupervisorBase(abc.ABC):
    @abc.abstractmethod
    def start(self, run_id: str) -> None:
        pass

    @abc.abstractmethod
    def pause(self, run_id: str, reason: str) -> None:
        pass

    @abc.abstractmethod
    def resume(self, run_id: str, clearance_code: str) -> None:
        pass

    @abc.abstractmethod
    def drain(self, run_id: str) -> None:
        pass

    @abc.abstractmethod
    def stop(self, run_id: str) -> None:
        pass


class ReadinessCheckerBase(abc.ABC):
    @abc.abstractmethod
    def check_all(self, run_id: str) -> Any:
        pass


class RecoveryCoordinatorBase(abc.ABC):
    @abc.abstractmethod
    def coordinate_recovery(self, run_id: str) -> Any:
        pass


class IncidentHandlerBase(abc.ABC):
    @abc.abstractmethod
    def report_incident(
        self, run_id: str, type: str, severity: str, details: str
    ) -> str:
        pass
