from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from app.knowledge.models import (
    KnowledgeItem,
    KnowledgeSearchResult,
    ApplicabilityRule,
    FreshnessReport,
    OperatorReadinessRecord,
    QuizResult,
)


class KnowledgeRegistryBase(ABC):
    @abstractmethod
    def register(self, item: KnowledgeItem) -> None:
        pass

    @abstractmethod
    def get(self, item_id: str) -> Optional[KnowledgeItem]:
        pass

    @abstractmethod
    def list_all(self) -> List[KnowledgeItem]:
        pass


class RunbookValidatorBase(ABC):
    @abstractmethod
    def validate_runbook(self, runbook: KnowledgeItem) -> bool:
        pass


class TrainingGeneratorBase(ABC):
    @abstractmethod
    def generate_scenario(self, module_id: str) -> Any:
        pass


class ReadinessEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(
        self, operator_id: str, context: Dict[str, Any]
    ) -> OperatorReadinessRecord:
        pass
