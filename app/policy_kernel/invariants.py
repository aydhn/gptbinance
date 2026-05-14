CAPACITY_INVARIANTS = [
    "no_trusted_live_expansion_under_insufficient_reserved_headroom",
    "no_critical_backfill_or_migration_under_unbounded_live_path_contention",
    "no_activation_progression_under_unresolved_severe_saturation_in_required_paths",
    "no_guaranteed_capacity_claim_without_explicit_reservation_lineage"
]



# Cost plane evaluation integration
def append_cost_invariants(existing_invariants):
    existing_invariants.extend([
        "no_trusted_high_risk_expansion_under_breached_critical_cost_guardrail",
        "no_guaranteed_economic_sustainability_claim_without_attribution_complete_unit_economics",
        "no_large_scale_replay_under_unresolved_live_path_cost_contention",
        "no_cost_optimization_claim_that_hides_degraded_reliability_posture"
    ])
    return existing_invariants
