def notify_assurance_event(event_type: str, message: str):
    # Simulated notification
    print(f"[Telegram Notify] {event_type}: {message}")

ACCOUNTABILITY_EVENTS = ['accountability manifest ready', 'ownerless risk detected', 'material breach detected', 'unresolved restitution detected', 'accountability review required']


# Incentive Plane Notifier Support
INCENTIVE_NOTIFIER_EVENTS = [
    "incentive_manifest_ready",
    "gaming_signal_detected",
    "hidden_conflict_detected",
    "beneficiary_cost_spike_detected",
    "incentive_review_required"
]
