from abc import ABC, abstractmethod
from typing import List
from app.control.models import (
    ActionRequest,
    ApprovalRecord,
    AuthorizationResult,
    CommandJournalEntry,
    ApprovalDecision,
)


class ApprovalEngineBase(ABC):
    @abstractmethod
    def evaluate(
        self, request: ActionRequest, decisions: List[ApprovalDecision]
    ) -> ApprovalRecord:
        pass


class AuthorizationEngineBase(ABC):
    @abstractmethod
    def authorize(self, record: ApprovalRecord) -> AuthorizationResult:
        pass


class PolicyEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, request: ActionRequest, record: ApprovalRecord) -> bool:
        pass


class JournalWriterBase(ABC):
    @abstractmethod
    def write(self, entry: CommandJournalEntry) -> None:
        pass
