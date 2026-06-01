def notify_assurance_event(event_type: str, message: str):
    # Simulated notification
    print(f"[Telegram Notify] {event_type}: {message}")

ACCOUNTABILITY_EVENTS = ['accountability manifest ready', 'ownerless risk detected', 'material breach detected', 'unresolved restitution detected', 'accountability review required']
