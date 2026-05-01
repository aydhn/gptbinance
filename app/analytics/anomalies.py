from typing import List, Any

from app.analytics.models import AnalyticsRun, AnomalyReport


class AnomalyDetector:
    def detect(self, run: AnalyticsRun, data: Any) -> List[AnomalyReport]:
        # Simple rule-based mocked detection
        reports = []
        # Example rule: check reject storm
        # If reject storm found:
        # rep = AnomalyReport(
        #     run_id=run.run_id,
        #     anomaly_type="reject_storm",
        #     severity=AnomalySeverity.HIGH,
        #     timestamp=datetime.utcnow(),
        #     evidence=">10 rejects in 1 minute",
        #     affected_symbols=["BTCUSDT"]
        # )
        # reports.append(rep)

        return reports
