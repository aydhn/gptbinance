from datetime import datetime
from typing import Dict, List, Optional

from .enums import ReliabilityTrustVerdict
from .models import ReliabilityTrustVerdictReport


class TrustManager:
    def __init__(self, registry, quality_analyzer):
        self._registry = registry
        self._quality = quality_analyzer
        self._verdicts: Dict[str, List[ReliabilityTrustVerdictReport]] = {}

    def calculate_verdict(
        self, service_id: str, timestamp: datetime
    ) -> ReliabilityTrustVerdictReport:
        quality_info = self._quality.analyze_service_quality(service_id)

        verdict = ReliabilityTrustVerdict.TRUSTED
        if quality_info["quality_score"] < 50:
            verdict = ReliabilityTrustVerdict.BLOCKED
        elif quality_info["quality_score"] < 80:
            verdict = ReliabilityTrustVerdict.CAUTION

        report = ReliabilityTrustVerdictReport(
            verdict_id=f"v-{service_id}-{int(timestamp.timestamp())}",
            service_id=service_id,
            timestamp=timestamp,
            verdict=verdict,
            factors=quality_info,
        )
        self.record_verdict(report)
        return report

    def record_verdict(self, verdict: ReliabilityTrustVerdictReport) -> None:
        if verdict.service_id not in self._verdicts:
            self._verdicts[verdict.service_id] = []
        self._verdicts[verdict.service_id].append(verdict)

    def get_latest_verdict(
        self, service_id: str
    ) -> Optional[ReliabilityTrustVerdictReport]:
        verdicts = self._verdicts.get(service_id, [])
        if not verdicts:
            return None
        return sorted(verdicts, key=lambda v: v.timestamp)[-1]
