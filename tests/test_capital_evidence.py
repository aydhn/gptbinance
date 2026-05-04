from app.capital.evidence import build_evidence_bundle, check_required_evidence
from app.capital.enums import EvidenceFreshness
from datetime import datetime, timezone, timedelta


def test_evidence_freshness():
    now = datetime.now(timezone.utc)
    old = now - timedelta(hours=2)

    bundle1 = build_evidence_bundle({"a": "1"}, {"a": now})
    assert bundle1.freshness == EvidenceFreshness.FRESH

    bundle2 = build_evidence_bundle({"a": "1"}, {"a": old})
    assert bundle2.freshness == EvidenceFreshness.STALE

    missing = check_required_evidence(bundle1, ["a", "b"])
    assert missing == ["b"]
