from app.remediation.preflight import PreflightEngine
from app.remediation.compiler import RemediationCompiler
from app.remediation.findings import FindingIntake


def test_preflight_warnings_venue_affecting():
    compiler = RemediationCompiler()
    intake = FindingIntake()
    f1 = intake.normalize_finding("F-1", "order_lifecycle", "high", {})
    pack = compiler.compile_pack(f1, explicit_recipe_id="request_orphan_order_review")

    engine = PreflightEngine()
    report = engine.run_preflight(pack)

    assert report["passed"] is True
    assert len(report["warnings"]) > 0
    assert "venue-affecting" in report["warnings"][0]
