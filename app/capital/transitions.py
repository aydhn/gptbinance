from datetime import datetime, timezone
import uuid
from typing import List, Dict

from app.capital.models import ScaleTransitionPlan
from app.capital.tiers import get_tier
from app.capital.ladder import is_transition_allowed


def create_transition_plan(
    current_tier_id: str, target_tier_id: str
) -> ScaleTransitionPlan:
    is_upgrade = False

    # Simple heuristic for upgrade vs downgrade: check allowed transitions (upward)
    from app.capital.ladder import get_ladder

    ladder = get_ladder()

    if (
        current_tier_id in ladder.allowed_transitions
        and target_tier_id in ladder.allowed_transitions[current_tier_id]
    ):
        is_upgrade = True

    target_tier = get_tier(target_tier_id)

    approvals = []
    if target_tier.requires_approval:
        approvals.append("governance_capital_committee")

    checks = target_tier.required_evidence_types.copy()
    if is_upgrade:
        checks.append("escalation_readiness_pass")

    # Safe activation order
    activation_order = []
    if is_upgrade:
        activation_order = [
            "freeze_current_posture",
            "verify_evidence",
            "activate_target_tier",
            "thaw_posture",
        ]
    else:
        activation_order = [
            "cancel_open_orders",
            "reduce_positions_to_target_budget",
            "activate_target_tier",
        ]

    return ScaleTransitionPlan(
        plan_id=f"plan_{uuid.uuid4().hex[:8]}",
        current_tier_id=current_tier_id,
        target_tier_id=target_tier_id,
        is_upgrade=is_upgrade,
        required_approvals=approvals,
        required_checks=checks,
        safe_activation_order=activation_order,
        dry_run_summary={
            "target_budget": target_tier.budget.model_dump(),
            "warning": "This is a dry-run plan. No changes applied.",
        },
    )
