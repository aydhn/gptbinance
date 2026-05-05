from abc import ABC, abstractmethod
from typing import List
from app.policy_kernel.models import (
    PolicyContext,
    PolicyEvidenceBundle,
    PolicyDecisionNode,
    PolicyDecisionGraph,
)
from app.policy_kernel.enums import PolicyVerdict


class RuleEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(
        self, context: PolicyContext, evidence: PolicyEvidenceBundle
    ) -> List[PolicyDecisionNode]:
        pass


class InvariantEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(
        self, context: PolicyContext, evidence: PolicyEvidenceBundle
    ) -> List[PolicyDecisionNode]:
        pass


class PrecedenceResolverBase(ABC):
    @abstractmethod
    def resolve(self, nodes: List[PolicyDecisionNode]) -> PolicyVerdict:
        pass


class DecisionProofBuilderBase(ABC):
    @abstractmethod
    def build_proof(self, graph: PolicyDecisionGraph) -> str:
        pass
