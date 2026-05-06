from app.postmortems.quality import QualityChecker
from app.postmortems.models import (
    PostmortemRecord,
    PostmortemSeedRef,
    PostmortemVerdict,
)
from datetime import datetime, timezone


def test_quality_checker():
    checker = QualityChecker()
    seed = PostmortemSeedRef(
        incident_id="INC", seed_timestamp=datetime.now(timezone.utc), affected_scopes=[]
    )
    verdict = PostmortemVerdict(summary="test")
    record = PostmortemRecord(postmortem_id="PM-1", seed_ref=seed, verdict=verdict)
    res = checker.check(record)
    assert res["is_quality_sufficient"] is True
