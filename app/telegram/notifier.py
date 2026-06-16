class CollateralNotifier:
    def notify(self, event_type: str, details: dict):
        allowed = ["collateral manifest ready", "hidden lien detected", "stale valuation detected", "wrongful liquidation detected", "collateral review required"]
        if event_type in allowed:
            print(f"Telegram Notification [{event_type}]: {details}")
