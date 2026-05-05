from datetime import datetime, timezone
import uuid
from typing import Dict, List
from app.shadow_state.models import (
    ShadowTwinSnapshot,
    ConvergenceRun,
    ConvergenceResult,
    DriftSeveritySummary,
    DriftFinding,
)
from app.shadow_state.enums import ShadowDomain, ConvergenceVerdict
from app.shadow_state.drift import DriftDetector
from app.shadow_state.classification import DriftClassifier


class ConvergenceEngine:
    def __init__(self):
        self.drift_detector = DriftDetector()
        self.classifier = DriftClassifier()

    def run_convergence(self, twin: ShadowTwinSnapshot) -> ConvergenceRun:
        results: Dict[str, ConvergenceResult] = {}
        all_findings: List[DriftFinding] = []

        for domain in ShadowDomain:
            findings = self.drift_detector.detect_drift(twin, domain)
            verdict = self.classifier.evaluate_verdict(findings)

            is_clean = verdict == ConvergenceVerdict.CLEAN
            results[domain.value] = ConvergenceResult(
                domain=domain, verdict=verdict, findings=findings, is_clean=is_clean
            )
            all_findings.extend(findings)

        global_verdict = self.classifier.evaluate_verdict(all_findings)

        severity_summary = DriftSeveritySummary()
        for f in all_findings:
            if f.severity == "info":
                severity_summary.info += 1
            elif f.severity == "warning":
                severity_summary.warning += 1
            elif f.severity == "critical":
                severity_summary.critical += 1
            elif f.severity == "blocker":
                severity_summary.blocker += 1

        return ConvergenceRun(
            run_id=f"conv_{uuid.uuid4().hex[:8]}",
            twin_ref=twin.twin_id,
            timestamp=datetime.now(timezone.utc),
            domain_results=results,
            global_verdict=global_verdict,
            drift_summary=severity_summary,
        )


convergence_engine = ConvergenceEngine()
