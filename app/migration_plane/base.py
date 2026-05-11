from abc import ABC, abstractmethod
from typing import Dict, Any, List
from app.migration_plane.models import MigrationDefinition

class MigrationRegistryBase(ABC):
    @abstractmethod
    def register(self, migration: MigrationDefinition) -> None:
        pass

    @abstractmethod
    def get(self, migration_id: str) -> MigrationDefinition:
        pass

class CompatibilityEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, migration_id: str) -> Dict[str, Any]:
        pass

class CutoverEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, cutover_id: str) -> Dict[str, Any]:
        pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, migration_id: str) -> Dict[str, Any]:
        pass
