from abc import ABC, abstractmethod
from typing import List
from app.allocation.models import (
    AllocationCandidate,
    AllocationIntent,
    AllocationManifest,
)


class CandidateCompilerBase(ABC):
    @abstractmethod
    def compile_candidates(self) -> List[AllocationCandidate]:
        pass


class SleeveEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_sleeve_budgets(self) -> None:
        pass
