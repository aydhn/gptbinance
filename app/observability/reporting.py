class ObservabilityReporter:
    def log_perf_digest(self, summary: str) -> None:
        print(f"[OBSERVABILITY PERF DIGEST]\n{summary}")

    def log_perf_alert(self, alert_msg: str) -> None:
        print(f"[OBSERVABILITY PERF ALERT]\n{alert_msg}")
