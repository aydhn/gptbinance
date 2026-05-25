# liability notifications


def notify_telegram_rights(event_type: str, context: dict):
    allowed_types = [
        "rights manifest ready", "pseudo consent detected", "invalid waiver detected",
        "standing burial detected", "rights review required"
    ]
    if event_type in allowed_types:
        print(f"[Telegram] Sent: {event_type}")

def notify_settlement_event():
    pass # Added for Phase 124