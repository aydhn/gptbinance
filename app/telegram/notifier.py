class CollateralNotifier:
    def notify(self, event_type: str, details: dict):
        allowed = ["collateral manifest ready", "hidden lien detected", "stale valuation detected", "wrongful liquidation detected", "collateral review required"]
        if event_type in allowed:
            print(f"Telegram Notification [{event_type}]: {details}")

# Phase 160: Waterfall Plane Integrations

def send_waterfall_notification(event_type: str, details: dict):
    valid_events = [
        "waterfall manifest ready",
        "hidden seniority detected",
        "overdistribution detected",
        "clawback gap detected",
        "waterfall review required"
    ]
    if event_type in valid_events:
        print(f"Sending telegram notification: {event_type} - {details}")
# Escrow-plane telegram notifier: fake segregation detected events
