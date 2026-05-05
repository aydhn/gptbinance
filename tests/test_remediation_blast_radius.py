from app.remediation.blast_radius import BlastRadiusAnalyzer
from app.remediation.compiler import RemediationCompiler
from app.remediation.findings import FindingIntake


def test_blast_radius_venue_affecting():
    compiler = RemediationCompiler()
    intake = FindingIntake()
    finding = intake.normalize_finding("F-1", "order_lifecycle", "high", {})
    pack = compiler.compile_pack(
        finding, explicit_recipe_id="request_orphan_order_review"
    )

    analyzer = BlastRadiusAnalyzer()
    report = analyzer.analyze(pack)
    assert report.severity.value == "critical"
    assert "venue" in report.impacted_domains


def test_blast_radius_read_only():
    compiler = RemediationCompiler()
    intake = FindingIntake()
    finding = intake.normalize_finding("F-1", "shadow_state", "low", {})
    pack = compiler.compile_pack(
        finding, explicit_recipe_id="refresh_venue_shadow_snapshot"
    )

    analyzer = BlastRadiusAnalyzer()
    report = analyzer.analyze(pack)
    assert report.severity.value == "low"
    assert "shadow_state" in report.impacted_domains
