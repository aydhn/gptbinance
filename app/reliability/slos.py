CAPACITY_SLOS = [
    "live_headroom_floor",
    "quota_exhaustion_absence",
    "queue_starvation_absence",
    "repeated_emergency_shedding_ceiling",
    "trusted_capacity_degraded_ratio"
]



# Cost plane evaluation integration
def append_cost_slos(slos):
    slos.extend([
        "unattributed_critical_spend_absence",
        "budget_guardrail_breach_ceiling",
        "stale_invoice_reconciliation_absence",
        "unsustainable_unit_cost_spike_ceiling",
        "trusted_cost_degraded_ratio"
    ])
    return slos
