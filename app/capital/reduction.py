from datetime import datetime, timezone
import uuid
from typing import Dict, Any

from app.capital.models import CapitalReductionCheck
from app.capital.enums import ReductionVerdict
from app.capital.tiers import get_tier
from app.capital.budgets import budget_evaluator


def evaluate_reduction_needs(
    current_tier_id: str,
    current_usage: Dict[str, float],
    external_alerts: int = 0,
    reconciliation_mismatch: bool = False,
) -> CapitalReductionCheck:
    """
    Evaluates if we need to reduce or freeze capital based on usage and external signals.
    """
    tier = get_tier(current_tier_id)
    reasons = []
    verdict = ReductionVerdict.HOLD

    # Check budgets
    budget_eval = budget_evaluator.evaluate_utilization(tier.budget, current_usage)
    if not budget_eval["ok"]:
        reasons.extend(budget_eval["breaches"])
        verdict = ReductionVerdict.REDUCE

    # Check external criticals
    if reconciliation_mismatch:
        reasons.append("Ledger reconciliation mismatch detected.")
        verdict = ReductionVerdict.FREEZE

    if external_alerts >= 3:
        reasons.append(
            f"High number of critical observability alerts ({external_alerts})."
        )
        verdict = max(verdict, ReductionVerdict.REDUCE)  # FREEZE > REDUCE > HOLD

    # Escalation of verdict
    if "loss" in " ".join(reasons).lower() and verdict == ReductionVerdict.REDUCE:
        # Hard loss breaches might warrant a freeze depending on policy, we stick to reduce for basic breaches
        pass

    return CapitalReductionCheck(
        check_id=f"red_{uuid.uuid4().hex[:8]}",
        timestamp=datetime.now(timezone.utc),
        current_tier_id=current_tier_id,
        verdict=verdict,
        reasons=reasons,
    )
