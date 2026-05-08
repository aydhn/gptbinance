from typing import List
from datetime import datetime, timezone
import hashlib
from app.allocation.models import (
    AllocationCandidate,
    AllocationIntent,
    AllocationManifest,
    TrustVerdict,
)
from app.allocation.sizing import SizingEngine
from app.allocation.budgets import BudgetManager


class IntentBuilder:
    def __init__(self, budget_manager: BudgetManager, sizing_engine: SizingEngine):
        self.budget_manager = budget_manager
        self.sizing_engine = sizing_engine

    def build_intents(
        self, candidates: List[AllocationCandidate]
    ) -> List[AllocationIntent]:
        intents = []
        for cand in candidates:
            try:
                budget = self.budget_manager.get_budget(cand.sleeve_ref)
                if budget.is_frozen:
                    intent = self._reject_intent(cand, "budget_frozen")
                else:
                    intent = self.sizing_engine.determine_size(cand, budget.headroom)
                    if intent.verdict in [
                        AllocationVerdict.ACCEPTED,
                        AllocationVerdict.CLIPPED,
                    ]:
                        self.budget_manager.consume(
                            cand.sleeve_ref, intent.clipped_size
                        )
            except Exception as e:
                intent = self._reject_intent(cand, str(e))
            intents.append(intent)
        return intents

    def _reject_intent(
        self, cand: AllocationCandidate, reason: str
    ) -> AllocationIntent:
        from app.allocation.enums import AllocationVerdict

        return AllocationIntent(
            intent_id=f"intent_{cand.candidate_id}",
            candidate_id=cand.candidate_id,
            symbol=cand.symbol,
            sleeve_ref=cand.sleeve_ref,
            verdict=AllocationVerdict.REJECTED,
            base_size=cand.requested_notional,
            clipped_size=0.0,
            reject_reason=reason,
            budget_ref="none",
            route_ref="none",
        )

class AllocationIntent:
    def __init__(self, intent_id: str, symbol: str, target_size: float, direction: str, is_reduce_only: bool = False):
        self.intent_id = intent_id
        self.symbol = symbol
        self.target_size = target_size
        self.direction = direction
        self.is_reduce_only = is_reduce_only
        self.venue_class_preference = "paper"
        self.clipped_reasons = []

    def add_clip_reason(self, reason: str):
        self.clipped_reasons.append(reason)
