# liability events

# dispute events
canonical_dispute_events = [
    "dispute_registered", "complaint_filed", "issue_framed",
    "burden_assigned", "hearing_started", "ruling_issued",
    "dismissal_recorded", "appeal_opened", "remand_ordered", "reopen_granted"
]


# Phase 162: Netting Events
class NettingEvents:
    events = [
        "netting_set_created", "mutuality_validated", "valuation_snapshotted",
        "setoff_executed", "closeout_amount_fixed", "residual_carried",
        "mistaken_setoff_detected", "netting_closed"
    ]
