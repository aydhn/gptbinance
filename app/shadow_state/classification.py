from typing import List
from app.shadow_state.models import DriftFinding
from app.shadow_state.enums import DriftSeverity, ConvergenceVerdict


class DriftClassifier:
    """Classifies a list of drift findings to a convergence verdict."""

    def evaluate_verdict(self, findings: List[DriftFinding]) -> ConvergenceVerdict:
        if not findings:
            return ConvergenceVerdict.CLEAN

        severities = [f.severity for f in findings]

        if DriftSeverity.BLOCKER in severities or DriftSeverity.CRITICAL in severities:
            return ConvergenceVerdict.CRITICAL_DIVERGENCE

        if DriftSeverity.WARNING in severities:
            return ConvergenceVerdict.SUSPICIOUS_DIVERGENCE

        return ConvergenceVerdict.TRANSIENT_DIVERGENCE
