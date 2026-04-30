from abc import ABC, abstractmethod
from typing import List, Dict, Any

from app.portfolio.models import (
    PortfolioIntentBatch,
    PortfolioDecisionBatch,
    PortfolioContext,
    AllocationRequest,
    AllocationResult,
    PortfolioCandidate,
    OpportunityRank,
    OverlapReport,
)
from app.portfolio.enums import OverlapType


class BasePortfolioAllocator(ABC):
    """Base class for portfolio allocation strategies."""

    @abstractmethod
    def allocate(
        self, batch: PortfolioIntentBatch, context: PortfolioContext
    ) -> PortfolioDecisionBatch:
        """Process a batch of approved intents and generate portfolio decisions."""
        pass


class BaseRankingModel(ABC):
    """Base class for opportunity ranking models."""

    @abstractmethod
    def rank_candidates(
        self, candidates: List[PortfolioCandidate], context: PortfolioContext
    ) -> List[PortfolioCandidate]:
        """Rank a list of candidates based on portfolio context."""
        pass


class BaseSleevePolicy(ABC):
    """Base class for sleeve policies."""

    @abstractmethod
    def check_headroom(self, context: PortfolioContext) -> Dict[str, float]:
        """Return remaining headroom for sleeves."""
        pass


class BaseOverlapEstimator(ABC):
    """Base class for overlap estimation."""

    @abstractmethod
    def estimate_overlap(
        self, candidate: PortfolioCandidate, context: PortfolioContext
    ) -> OverlapReport:
        """Estimate overlap for a candidate against current context."""
        pass
