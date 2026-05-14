import pytest
from datetime import datetime, timezone
from app.continuity_plane.trust import TrustedContinuityVerdictEngine
from app.continuity_plane.models import ContinuityTrustVerdict
from app.continuity_plane.enums import ContinuityTrustVerdict as TrustVerdictEnum

def test_trust_engine():
    engine = TrustedContinuityVerdictEngine()
    verdict = ContinuityTrustVerdict(
        service_id="srv_1",
        verdict=TrustVerdictEnum.TRUSTED,
        factors={"backup_status": "ok"},
        timestamp=datetime.now(timezone.utc)
    )
    engine.record_verdict(verdict)

    retrieved = engine.get_verdict("srv_1")
    assert retrieved is not None
    assert retrieved.verdict == TrustVerdictEnum.TRUSTED
