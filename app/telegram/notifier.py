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


# Phase 162: Netting Notifications
class NettingNotifier:
    def notify(self, event_type, data):
        # types: netting manifest ready, mutuality failure detected, stale valuation detected, mistaken setoff detected, netting review required
        pass

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/telegram/notifier.py")
    return integration.evaluate_posture()
