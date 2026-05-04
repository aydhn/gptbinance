import json
from app.capital.tiers import get_all_tiers
from app.capital.ladder import get_ladder
from app.capital.posture import generate_posture_snapshot
from app.capital.freeze import freeze_manager
from app.capital.escalation import escalation_engine
from app.capital.evidence import build_evidence_bundle
from app.capital.transitions import create_transition_plan
from app.capital.reduction import evaluate_reduction_needs
from datetime import datetime, timezone


def report_ladder_summary() -> str:
    ladder = get_ladder()
    output = [f"Capital Ladder: {ladder.ladder_id}", "-" * 40]

    for tier in ladder.tiers:
        output.append(f"Tier: {tier.id} ({tier.name}) [Class: {tier.tier_class.value}]")
        output.append(f"  Max Capital: ${tier.budget.max_deployable_capital}")
        output.append(f"  Approvals Required: {tier.requires_approval}")
        next_tiers = ladder.allowed_transitions.get(tier.id, [])
        output.append(
            f"  Allowed Next Tiers: {', '.join(next_tiers) if next_tiers else 'None'}"
        )
        output.append("")
    return "\n".join(output)


def report_posture(active_tier: str, usage: dict) -> str:
    snap = generate_posture_snapshot(active_tier, usage)
    output = [
        f"Capital Posture Snapshot [{snap.timestamp.isoformat()}]",
        "-" * 40,
        f"Active Tier: {snap.active_tier_id}",
        f"State: {snap.posture_state.value}",
        f"Deployed: ${snap.deployed_capital}",
        f"Reserved: ${snap.reserved_capital}",
        f"Frozen: ${snap.frozen_capital}",
        f"Headroom: ${snap.available_headroom}",
        f"Active Tranches: {len(snap.active_tranches)}",
        "",
    ]
    return "\n".join(output)


def report_escalation_check(current_tier: str, target_tier: str, usage: dict) -> str:
    now = datetime.now(timezone.utc)
    bundle = build_evidence_bundle(
        refs={"qualification_pass": "q1", "ledger_clean": "l1"},
        timestamps={"qualification_pass": now, "ledger_clean": now},
    )
    check = escalation_engine.check_escalation_readiness(
        current_tier, target_tier, bundle
    )

    output = [
        f"Escalation Check: {current_tier} -> {target_tier}",
        "-" * 40,
        f"Ready: {check.readiness.is_ready}",
        f"Verdict: {check.readiness.verdict.value}",
        f"Blockers: {json.dumps(check.readiness.blockers)}",
        f"Warnings: {json.dumps(check.readiness.warnings)}",
        f"Next Recommendation: {check.readiness.next_tier_recommendation}",
        "",
    ]
    return "\n".join(output)


def report_reduction_check(current_tier: str, usage: dict) -> str:
    check = evaluate_reduction_needs(current_tier, usage)
    output = [
        f"Reduction Check [Tier: {current_tier}]",
        "-" * 40,
        f"Verdict: {check.verdict.value}",
        f"Reasons: {json.dumps(check.reasons)}",
        "",
    ]
    return "\n".join(output)


def report_budgets(tier_id: str) -> str:
    from app.capital.tiers import get_tier

    tier = get_tier(tier_id)
    output = [
        f"Budgets for Tier: {tier_id}",
        "-" * 40,
        f"Max Deployable: ${tier.budget.max_deployable_capital}",
        f"Max Positions: {tier.budget.max_concurrent_positions}",
        f"Max Leverage: {tier.budget.max_leverage}x",
        f"Concentration Cap: {tier.budget.max_symbol_concentration * 100}%",
        "Loss Budgets:",
    ]
    for lb in tier.budget.loss_budgets:
        output.append(
            f"  - {lb.window.value}: ${lb.max_loss_amount} ({lb.severity.value})"
        )
    output.append("")
    return "\n".join(output)


def report_evidence() -> str:
    now = datetime.now(timezone.utc)
    bundle = build_evidence_bundle(
        refs={"qualification_pass": "q1", "ledger_clean": "l1"},
        timestamps={"qualification_pass": now, "ledger_clean": now},
    )
    output = [
        f"Evidence Bundle [{bundle.timestamp.isoformat()}]",
        "-" * 40,
        f"Freshness: {bundle.freshness.value}",
        f"Refs: {json.dumps(bundle.evidence_refs)}",
        f"Missing Items: {json.dumps(bundle.missing_items)}",
        "",
    ]
    return "\n".join(output)


def report_transition_plan(current: str, target: str) -> str:
    plan = create_transition_plan(current, target)
    output = [
        f"Transition Plan: {current} -> {target}",
        "-" * 40,
        f"Is Upgrade: {plan.is_upgrade}",
        f"Required Approvals: {json.dumps(plan.required_approvals)}",
        f"Required Checks: {json.dumps(plan.required_checks)}",
        f"Activation Order: {json.dumps(plan.safe_activation_order)}",
        "",
    ]
    return "\n".join(output)
