from app.postmortems.evidence import EvidenceBundleBuilder, EvidenceFreshnessChecker


def test_evidence_bundle():
    builder = EvidenceBundleBuilder()
    bundle = builder.assemble("INC-001")
    assert bundle["incident_id"] == "INC-001"


def test_evidence_freshness():
    checker = EvidenceFreshnessChecker()
    assert checker.is_fresh({}) is True
