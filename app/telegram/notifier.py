class TelegramNotifier:
    def notify(self, template: str, data: dict):
        # Ensures notifier fail doesn't break allocation evaluation
        pass

class ExecutionNotifier:
    @staticmethod
    def send_alert(alert_type: str, details: dict):
        # Stub with rate-limit logic implied
        print(f"Telegram Alert: {alert_type} - {details}")
