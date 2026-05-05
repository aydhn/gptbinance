def notify_board_event(event_type: str, candidate_id: str, details: str) -> None:
    """
    Mock Telegram notifier for board events.
    """
    print(f"[TELEGRAM] {event_type} for {candidate_id}: {details}")
