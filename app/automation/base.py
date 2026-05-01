import abc
from typing import Dict, Any
from app.automation.models import JobDefinition, GateCheckResult, JobRunContext


class JobExecutorBase(abc.ABC):
    @abc.abstractmethod
    def execute(self, job_def: JobDefinition, context: JobRunContext) -> Dict[str, Any]:
        """
        Execute the job and return artifacts.
        Should raise exception on failure.
        """
        pass


class PreconditionCheckerBase(abc.ABC):
    @abc.abstractmethod
    def check(self, job_def: JobDefinition, context: JobRunContext) -> GateCheckResult:
        pass
