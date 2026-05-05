from abc import ABC, abstractmethod
from typing import List, Dict
from app.migrations.models import (
    MigrationDefinition,
    MigrationPlan,
    CompatibilityMatrix,
    CompatibilityCheckResult,
    MigrationScope,
    MigrationApplyResult,
)


class MigrationCompilerBase(ABC):
    @abstractmethod
    def compile_plan(
        self, target_scope: MigrationScope, target_versions: Dict[str, str]
    ) -> MigrationPlan:
        pass


class DependencyResolverBase(ABC):
    @abstractmethod
    def resolve(
        self, migrations: List[MigrationDefinition]
    ) -> List[MigrationDefinition]:
        pass


class CompatibilityEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(
        self, plan: MigrationPlan, current_matrix: CompatibilityMatrix
    ) -> CompatibilityCheckResult:
        pass


class ApplyExecutorBase(ABC):
    @abstractmethod
    def execute(self, plan: MigrationPlan) -> MigrationApplyResult:
        pass
