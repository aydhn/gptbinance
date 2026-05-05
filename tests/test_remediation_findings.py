from app.remediation.findings import FindingIntake


def test_normalize_finding():
    intake = FindingIntake()
    ref = intake.normalize_finding(
        finding_id="FND-123",
        source_domain="shadow_state",
        severity="high",
        context={"symbol": "BTCUSDT"},
    )
    assert ref.finding_id == "FND-123"
    assert ref.source_domain == "shadow_state"
    assert ref.severity == "high"
    assert ref.context["symbol"] == "BTCUSDT"
    assert not ref.is_stale
