from typing import List, Dict, Any
from datetime import datetime, timezone
import uuid
from app.data_governance.models import (
    DatasetQualityReport, DataQualityResult, QualityScoreBreakdown, DatasetRef
)
from app.data_governance.enums import QualitySeverity, TrustLevel
from app.data_governance.quality_rules import QualityRuleRegistry

class QualityEngine:
    def __init__(self):
        self.rule_registry = QualityRuleRegistry()

    def evaluate(self, dataset_ref: DatasetRef, data: Any, run_id: str = None) -> DatasetQualityReport:
        if run_id is None:
            run_id = str(uuid.uuid4())

        results: List[DataQualityResult] = []

        # Placeholder for actual rule evaluation logic.
        # In a real system, you would iterate over rules and apply them to 'data' (e.g. Pandas DataFrame).
        # We will mock a successful evaluation for now to allow structural integration.

        rule = self.rule_registry.get_rule("duplicate_primary_keys")
        results.append(
            DataQualityResult(
                rule_name=rule.rule_name,
                passed=True,
                severity=rule.severity,
                evidence="No duplicate primary keys found.",
                recommended_action="None"
            )
        )

        return self._compute_report(dataset_ref, run_id, results)

    def _compute_report(self, dataset_ref: DatasetRef, run_id: str, results: List[DataQualityResult]) -> DatasetQualityReport:
        total = len(results)
        passed = sum(1 for r in results if r.passed)
        failed = [r for r in results if not r.passed]

        critical = sum(1 for r in failed if r.severity == QualitySeverity.CRITICAL)
        high = sum(1 for r in failed if r.severity == QualitySeverity.HIGH)
        medium = sum(1 for r in failed if r.severity == QualitySeverity.MEDIUM)
        low = sum(1 for r in failed if r.severity == QualitySeverity.LOW)

        breakdown = QualityScoreBreakdown(
            total_rules=total,
            passed_rules=passed,
            failed_critical=critical,
            failed_high=high,
            failed_medium=medium,
            failed_low=low
        )

        score = passed / total if total > 0 else 0.0

        if critical > 0:
            status = TrustLevel.BLOCKED
        elif high > 0 or medium > 0:
            status = TrustLevel.CAUTION
        else:
            status = TrustLevel.TRUSTED

        return DatasetQualityReport(
            dataset_ref=dataset_ref,
            run_id=run_id,
            timestamp=datetime.now(timezone.utc),
            results=results,
            breakdown=breakdown,
            overall_score=score,
            status=status
        )
