class ObservabilityAlerts:
    ALERTS = [
        "controlling_precedent_conflict_detected",
        "precedent_cherry_pick_detected",
        "fake_analogy_detected",
        "silent_override_detected",
        "exception_inflation_detected",
        "precedent_review_required"
    ]

# Precedent Plane Integration added

class ObservabilityAlert:
    def __init__(self):
        self.authority_specific_alert_families = ['material_legitimacy_gap_detected', 'wrong_scope_approval_detected', 'shadow_authority_detected', 'ratification_laundering_detected', 'invalid_override_detected', 'authority_review_required']
