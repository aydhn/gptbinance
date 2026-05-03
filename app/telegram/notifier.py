class TelegramNotifier:
    def send_perf_alert(self, alert_type: str, message: str, severity: str) -> None:
        if severity in ["MAJOR", "CRITICAL", "HARD"]:
            print(f"[TELEGRAM] ALERT ({alert_type}): {message}")
        else:
            # Rate limit or ignore minor ones to prevent spam
            pass
