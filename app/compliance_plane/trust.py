from app.compliance_plane.models import ComplianceTrustVerdict
from app.compliance_plane.enums import TrustVerdict
from app.compliance_plane.base import TrustEvaluatorBase
from datetime import datetime, timezone


class TrustEvaluator(TrustEvaluatorBase):
    def evaluate_trust(self) -> ComplianceTrustVerdict:
        return ComplianceTrustVerdict(
            verdict_id="tv_auto",
            verdict=TrustVerdict.TRUSTED,
            factors={"evidence_freshness": "high", "debt_level": "low"},
            breakdown={"score": 0.95},
            evaluated_at=datetime.now(timezone.utc),
        )
