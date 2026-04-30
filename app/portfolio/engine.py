from typing import List, Dict, Any
from app.portfolio.models import (
    PortfolioConfig,
    PortfolioContext,
    PortfolioIntentBatch,
    PortfolioDecisionBatch,
    PortfolioCandidate,
)
from app.portfolio.policies import PortfolioPolicyManager
from app.portfolio.budgets import BudgetManager
from app.portfolio.ranking import SimpleRankingModel
from app.portfolio.overlap import OverlapEstimator
from app.portfolio.concentration import ConcentrationEvaluator
from app.portfolio.allocator import ConservativeAllocator


class PortfolioEngine:
    def __init__(self, config: PortfolioConfig):
        self.config = config
        self.policy_manager = PortfolioPolicyManager(config)
        self.budget_manager = BudgetManager(config)
        self.ranking_model = SimpleRankingModel()
        self.overlap_estimator = OverlapEstimator()
        self.concentration_evaluator = ConcentrationEvaluator(config)
        self.allocator = ConservativeAllocator(self.policy_manager, self.budget_manager)

    def process_intents(
        self, batch: PortfolioIntentBatch, context: PortfolioContext
    ) -> PortfolioDecisionBatch:
        """
        Orchestrates the portfolio allocation flow:
        1. Intake risk-approved intents
        2. Create Candidates
        3. Estimate Overlaps
        4. Check Concentration
        5. Rank Candidates
        6. Allocate Capital
        """

        # 1. Update Context Concentration Snapshot before processing
        context.concentration = self.concentration_evaluator.evaluate(
            context, batch.timestamp
        )

        # 2. Create Candidates
        candidates = []
        for intent in batch.risk_approved_intents:
            candidate = PortfolioCandidate(intent=intent)
            # 3. Overlap
            candidate.overlap_report = self.overlap_estimator.estimate_overlap(
                candidate, context
            )
            candidates.append(candidate)

        # 4. Rank
        ranked_candidates = self.ranking_model.rank_candidates(candidates, context)

        # 5. Allocate
        decision_batch = self.allocator.allocate(batch, context, ranked_candidates)

        return decision_batch
