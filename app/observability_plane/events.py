class AssuranceEvent:
    def __init__(self, event_type: str, data: dict):
        self.event_type = event_type
        self.data = data

def emit_assurance_event(event_type: str, data: dict):
    # Simulated event emission
    event = AssuranceEvent(event_type, data)
    return event

class AccountabilityEvents:
    EVENTS = ['duty_assigned', 'breach_recorded', 'escalation_missed', 'sanction_applied', 'appeal_filed', 'reversal_recorded', 'restitution_assigned', 'reinstatement_granted']


# Incentive Plane Integration
INCENTIVE_EVENTS = [
    "incentive_target_defined",
    "reward_formula_published",
    "reward_issued",
    "penalty_applied",
    "clawback_triggered",
    "incentive_conflict_detected",
    "gaming_signal_detected",
    "incentive_recalibrated"
]
