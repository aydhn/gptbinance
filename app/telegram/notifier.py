class TelegramNotifier:

    def send_data_governance_alert(self, event_type: str, severity: str, dataset_id: str, version: str, details: str, runbook_url: str):
        if not self._check_rate_limit(f"data_gov_{event_type}_{dataset_id}"):
            return

        message = TelegramTemplates.DATA_GOVERNANCE_ALERT.format(
            event_type=event_type,
            severity=severity,
            dataset_id=dataset_id,
            version=version,
            details=details,
            runbook_url=runbook_url
        )
        self.send_message(message)

    def send_data_governance_summary(self, total: int, trusted: int, caution: int, blocked: int):
        message = TelegramTemplates.DATA_GOVERNANCE_SUMMARY.format(
            total_datasets=total,
            trusted_count=trusted,
            caution_count=caution,
            blocked_count=blocked
        )
        self.send_message(message)

    def send_perf_alert(self, alert_type: str, message: str, severity: str) -> None:
        if severity in ["MAJOR", "CRITICAL", "HARD"]:
            print(f"[TELEGRAM] ALERT ({alert_type}): {message}")
        else:
            # Rate limit or ignore minor ones to prevent spam
            pass
