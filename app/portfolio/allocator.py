from app.portfolio.models import PortfolioSnapshot

from app.products.enums import ProductType
import copy
from typing import List, Dict, Any
from app.portfolio.base import BasePortfolioAllocator
from app.portfolio.models import (
    PortfolioIntentBatch,
    PortfolioDecisionBatch,
    PortfolioContext,
    PortfolioCandidate,
    PortfolioDecision,
    AllocationSlice,
)
from app.portfolio.enums import PortfolioVerdict
from app.portfolio.policies import PortfolioPolicyManager
from app.portfolio.budgets import BudgetManager


class ConservativeAllocator(BasePortfolioAllocator):
    def __init__(
        self, policy_manager: PortfolioPolicyManager, budget_manager: BudgetManager
    ):
        self.policy_manager = policy_manager
        self.budget_manager = budget_manager

    def evaluate_intent(self, snapshot: PortfolioSnapshot, requested_intent) -> float:
        # Penalize concentrated leveraged exposure
        if (
            hasattr(requested_intent, "product_type")
            and requested_intent.product_type != ProductType.SPOT
        ):
            if (
                snapshot.total_leveraged_exposure > snapshot.total_capital * 2
            ):  # Very strict global cap
                logger.warning(
                    "Allocation rejected: Global leveraged exposure cap exceeded."
                )
                return 0.0

        # Base allocation logic (legacy spot support)

    def allocate(
        self,
        batch: PortfolioIntentBatch,
        context: PortfolioContext,
        ranked_candidates: List[PortfolioCandidate],
    ) -> PortfolioDecisionBatch:
        decisions = []
        new_allocations_count = 0

        # Working context to simulate allocations within the batch
        working_context = copy.deepcopy(context)

        for candidate in ranked_candidates:
            intent_id = getattr(
                candidate.intent,
                "intent_id",
                f"{candidate.intent.symbol}_{candidate.intent.side.value}",
            )

            # Simple assumption: we need a requested_notional
            # The intent might just have quantity. Let's assume price=100.0 or extract it.
            # In a real system, intent would carry expected notional or we price it.
            requested_notional = getattr(
                candidate.intent, "expected_notional", candidate.intent.quantity * 100.0
            )

            verdict = PortfolioVerdict.APPROVE
            blocking_reasons = []
            approved_notional = requested_notional

            # 1. Check basic budget availability
            if not self.budget_manager.can_allocate(
                requested_notional, working_context
            ):
                # Try partial? For conservative, we just reject if no budget
                if working_context.budget.available_capital <= 0:
                    verdict = PortfolioVerdict.REJECT
                    blocking_reasons.append("Zero available capital.")
                else:
                    verdict = PortfolioVerdict.REDUCE
                    approved_notional = working_context.budget.available_capital
                    blocking_reasons.append(
                        f"Reduced due to budget limits. Available: {approved_notional:.2f}"
                    )

            # 2. Check Policies
            if verdict in (PortfolioVerdict.APPROVE, PortfolioVerdict.REDUCE):
                err = self.policy_manager.check_max_symbol_weight(
                    candidate.intent.symbol, approved_notional, working_context
                )
                if err:
                    verdict = PortfolioVerdict.REJECT
                    blocking_reasons.append(err)

                # Mock strategy family
                strat_family = "core"
                err = self.policy_manager.check_max_strategy_sleeve_weight(
                    strat_family, approved_notional, working_context
                )
                if err:
                    verdict = PortfolioVerdict.REJECT
                    blocking_reasons.append(err)

                err = self.policy_manager.check_max_correlated_cluster_weight(
                    candidate.intent.symbol, approved_notional, working_context
                )
                if err:
                    verdict = PortfolioVerdict.REJECT
                    blocking_reasons.append(err)

                err = self.policy_manager.check_reserve_cash(
                    approved_notional, working_context
                )
                if err:
                    verdict = PortfolioVerdict.REJECT
                    blocking_reasons.append(err)

                if verdict == PortfolioVerdict.APPROVE:
                    err = self.policy_manager.check_max_new_allocations(
                        new_allocations_count
                    )
                    if err:
                        verdict = PortfolioVerdict.DEFER
                        blocking_reasons.append(err)

            # Form decision
            decision = PortfolioDecision(
                intent_id=intent_id,
                verdict=verdict,
                original_intent=candidate.intent,
                blocking_reasons=blocking_reasons,
                rationale=(
                    candidate.rank.rationale
                    if candidate.rank
                    else "No ranking rationale."
                ),
            )

            if verdict in (PortfolioVerdict.APPROVE, PortfolioVerdict.REDUCE):
                # We approve a new intent with modified quantity
                new_intent = copy.deepcopy(candidate.intent)
                ratio = (
                    approved_notional / requested_notional
                    if requested_notional > 0
                    else 0
                )
                new_intent.quantity = candidate.intent.quantity * ratio

                decision.approved_intent = new_intent
                decision.allocation = AllocationSlice(
                    intent_id=intent_id,
                    approved_notional=approved_notional,
                    requested_notional=requested_notional,
                    reduction_ratio=ratio,
                )

                # Update working context
                working_context.budget.available_capital -= approved_notional
                working_context.budget.pending_allocations_notional += approved_notional

                if candidate.intent.symbol in working_context.symbol_sleeves:
                    working_context.symbol_sleeves[
                        candidate.intent.symbol
                    ].used_notional += approved_notional
                if strat_family in working_context.strategy_sleeves:
                    working_context.strategy_sleeves[
                        strat_family
                    ].used_notional += approved_notional

                new_allocations_count += 1

            decisions.append(decision)

        return PortfolioDecisionBatch(
            timestamp=batch.timestamp, run_id=batch.run_id, decisions=decisions
        )
