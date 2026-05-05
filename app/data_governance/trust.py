from typing import Dict, List
from app.data_governance.models import (
    DatasetRef,
    TrustVerdict,
    DatasetQualityReport,
    ProvenanceRecord,
)
from app.data_governance.enums import TrustLevel


class TrustVerdictEngine:
    def evaluate(
        self,
        dataset_ref: DatasetRef,
        quality_report: DatasetQualityReport,
        provenance_record: ProvenanceRecord = None,
        lineage_complete: bool = True,
        canonical_confidence: bool = True,
        schema_compatible: bool = True,
    ) -> TrustVerdict:
        reasons = []
        evidence = {}

        score = quality_report.overall_score
        status = quality_report.status

        if not lineage_complete:
            status = max(status, TrustLevel.CAUTION)
            reasons.append("Incomplete lineage.")
            score *= 0.9

        if not provenance_record:
            status = max(status, TrustLevel.CAUTION)
            reasons.append("Missing provenance.")
            score *= 0.8

        if not canonical_confidence:
            status = max(status, TrustLevel.CAUTION)
            reasons.append("Ambiguous canonical identity.")
            score *= 0.9

        if not schema_compatible:
            status = TrustLevel.BLOCKED
            reasons.append("Incompatible schema detected.")
            score = 0.0

        if quality_report.status == TrustLevel.BLOCKED:
            status = TrustLevel.BLOCKED
            reasons.append("Critical quality checks failed.")

        evidence["quality_score"] = f"{quality_report.overall_score * 100:.1f}%"
        evidence["lineage"] = "Complete" if lineage_complete else "Incomplete"
        evidence["schema"] = "Compatible" if schema_compatible else "Incompatible"

        if status == TrustLevel.TRUSTED:
            usage = "Safe for all downstream usage."
        elif status == TrustLevel.CAUTION:
            usage = "Use with caution. Verification required before production use."
        else:
            usage = "Blocked. Do not use for ML training or live trading."

        return TrustVerdict(
            dataset_ref=dataset_ref,
            verdict=status,
            score=max(0.0, score),
            reasons=reasons,
            evidence_breakdown=evidence,
            usage_recommendation=usage,
        )
