from typing import List, Optional
from .models import DataAnomalyFinding, AnomalyClass
from .exceptions import AnomalyHandlingError


class AnomalyDetector:
    def __init__(self):
        self._anomalies: List[DataAnomalyFinding] = []

    def detect_timestamp_skew(
        self, event_time_ms: float, available_at_ms: float, threshold_ms: int
    ) -> Optional[DataAnomalyFinding]:
        if (available_at_ms - event_time_ms) > threshold_ms:
            finding = DataAnomalyFinding(
                anomaly_id=f"skew_{event_time_ms}_{available_at_ms}",
                anomaly_class=AnomalyClass.TIMESTAMP_SKEW,
                details=f"Available at {available_at_ms} is significantly after event time {event_time_ms}",
            )
            self._anomalies.append(finding)
            return finding
        return None

    def list_anomalies(self) -> List[DataAnomalyFinding]:
        return self._anomalies
