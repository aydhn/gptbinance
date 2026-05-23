class ObservabilityEvents:
    EVENTS = [
        "precedent_registered",
        "holding_published",
        "rationale_updated",
        "analogy_asserted",
        "distinction_asserted",
        "precedent_conflict_detected",
        "precedent_overruled"
    ]

# Precedent Plane Integration added

class ObservabilityEvent:
    def __init__(self):
        self.canonical_authority_events = ['authority_registered', 'mandate_granted', 'delegation_recorded', 'override_used', 'veto_exercised', 'ratification_recorded', 'legitimacy_gap_detected']


canonical_rights_events = [
    "right_registered", "claim_asserted", "standing_confirmed",
    "consent_recorded", "waiver_applied", "revocation_effective",
    "right_exhausted", "rights_conflict_detected"
]
