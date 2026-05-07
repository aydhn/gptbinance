from datetime import datetime, timezone
import uuid
from typing import Dict, Any

from app.capital.models import CapitalPostureSnapshot
from app.capital.enums import CapitalPostureState
from app.capital.tiers import get_tier
from app.capital.tranches import tranche_manager
from app.capital.budgets import budget_evaluator


def generate_posture_snapshot(
    active_tier_id: str, current_usage: Dict[str, float]
) -> CapitalPostureSnapshot:
    tier = get_tier(active_tier_id)

    # Active tranches
    active_tranches = tranche_manager.get_active_tranches()
    total_tranche_cap = tranche_manager.get_total_active_tranche_size()

    deployed = current_usage.get("total_deployed", 0.0)
    reserved = current_usage.get("total_reserved", 0.0)
    frozen = current_usage.get("total_frozen", 0.0)

    # Effective cap is the min of Tier Cap and sum of active tranches
    # (If no tranches used, we just use tier cap for simplicity,
    # but strictly speaking tranches should gate it)
    effective_cap = tier.budget.max_deployable_capital
    if total_tranche_cap > 0:
        effective_cap = min(effective_cap, total_tranche_cap)

    available = max(0.0, effective_cap - deployed - reserved - frozen)

    # Check budget utilization to determine PostureState
    budget_eval = budget_evaluator.evaluate_utilization(tier.budget, current_usage)

    state = CapitalPostureState.NORMAL
    if frozen > 0:
        state = CapitalPostureState.FROZEN
    elif not budget_eval["ok"]:
        state = CapitalPostureState.REDUCED
    elif budget_eval["cautions"]:
        state = CapitalPostureState.CAUTION

    return CapitalPostureSnapshot(
        snapshot_id=f"snap_{uuid.uuid4().hex[:8]}",
        timestamp=datetime.now(timezone.utc),
        active_tier_id=active_tier_id,
        posture_state=state,
        deployed_capital=deployed,
        reserved_capital=reserved,
        frozen_capital=frozen,
        available_headroom=available,
        active_tranches=active_tranches,
        budget_utilization=current_usage,
    )


# Phase 43
def shadow_cleanliness_check(self):
    pass


def export_capital_operability() -> Dict[str, Any]:
    return {"freeze_density": 0.0, "capital_instability": 0.0}

class CapitalPostureFeatures:
    def export_features(self):
        pass
