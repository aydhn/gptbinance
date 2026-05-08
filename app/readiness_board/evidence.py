from typing import Dict, Any, List
from app.performance_plane.models import (
    PerformanceTrustVerdict,
    BenchmarkRelativeReport,
)


class ReadinessEvidenceCollector:
    @staticmethod
    def collect_performance_evidence(
        trust_verdict: PerformanceTrustVerdict,
        benchmark_report: BenchmarkRelativeReport = None,
    ) -> dict:
        evidence = {
            "trust_verdict": trust_verdict.verdict.value,
            "blockers": trust_verdict.blockers,
        }
        if benchmark_report:
            evidence["benchmark_cautions"] = benchmark_report.mismatch_cautions

        return evidence
