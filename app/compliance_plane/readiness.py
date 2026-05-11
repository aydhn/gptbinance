from app.compliance_plane.models import AuditReadinessReport
from app.compliance_plane.enums import AuditReadinessClass
from typing import Dict, Any


class AuditReadinessEvaluator:
    def evaluate(self, metrics: Dict[str, float]) -> AuditReadinessReport:
        req_score = metrics.get("req_score", 0.0)
        freshness_score = metrics.get("freshness_score", 0.0)

        readiness_class = AuditReadinessClass.UNPREPARED
        if req_score > 0.9 and freshness_score > 0.9:
            readiness_class = AuditReadinessClass.READY
        elif req_score > 0.7:
            readiness_class = AuditReadinessClass.NEEDS_REVIEW

        return AuditReadinessReport(
            report_id="auto_gen",
            readiness_class=readiness_class,
            requirement_satisfaction_score=req_score,
            evidence_freshness_score=freshness_score,
            attestation_coverage=metrics.get("att_coverage", 0.0),
            certification_coverage=metrics.get("cert_coverage", 0.0),
            exception_burden_score=metrics.get("exc_burden", 0.0),
        )
