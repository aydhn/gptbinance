def check_assurance_alerts(assurance_record) -> list:
    alerts = []
    if not assurance_record.cases:
        alerts.append("insufficient_assurance_detected")
    if assurance_record.expiry and assurance_record.expiry.is_expired:
        alerts.append("stale_certification_detected")
    if assurance_record.contradictions:
        alerts.append("contradiction_detected")
    if not assurance_record.surveillance:
        alerts.append("surveillance_lapse_detected")
    return alerts

ACCOUNTABILITY_ALERTS = ['ownerless_risk_detected', 'material_breach_detected', 'symbolic_sanction_detected', 'unresolved_restitution_detected', 'accountability_gap_detected', 'accountability_review_required']


# Incentive Plane Alerts
INCENTIVE_ALERTS = [
    "gaming_signal_detected",
    "hidden_conflict_detected",
    "symbolic_penalty_detected",
    "beneficiary_cost_spike_detected",
    "clawback_gap_detected",
    "incentive_review_required"
]
