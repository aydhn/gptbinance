from abc import ABC, abstractmethod
from typing import List
from .models import (
    DecisionFunnelRecord,
    OpportunityOutcome,
    DecisionFrictionRecord,
    OpportunityQualityReport,
    OpportunityCandidate,
)


class FunnelAnalyzerBase(ABC):
    @abstractmethod
    def analyze_funnel(
        self, candidate: OpportunityCandidate, stages_passed: List[str]
    ) -> DecisionFunnelRecord:
        pass


class OutcomeEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_outcome(
        self, candidate: OpportunityCandidate, funnel_record: DecisionFunnelRecord
    ) -> OpportunityOutcome:
        pass


class FrictionAnalyzerBase(ABC):
    @abstractmethod
    def analyze_friction(
        self, funnel_record: DecisionFunnelRecord
    ) -> List[DecisionFrictionRecord]:
        pass


class QualityReporterBase(ABC):
    @abstractmethod
    def generate_summary(self, start_time, end_time) -> OpportunityQualityReport:
        pass
