from datetime import datetime, timezone
from app.remediation.models import RemediationFindingRef
from app.remediation.compiler import RemediationCompiler
from app.remediation.blast_radius import BlastRadiusAnalyzer
from app.remediation.apply import ApplyExecutor
from app.remediation.enums import ApplyMode, RemediationClass


def test_compiler_success():
    compiler = RemediationCompiler()
    finding = RemediationFindingRef(
        finding_id="TEST-1",
        source_domain="shadow_state",
        severity="low",
        detected_at=datetime.now(timezone.utc),
    )
    pack = compiler.compile_pack(
        finding, explicit_recipe_id="refresh_venue_shadow_snapshot"
    )
    assert pack.recipe.safety_class == RemediationClass.READ_ONLY
    assert pack.pack_id.startswith("PACK-")


def test_apply_executor_prevents_venue_mutation():
    compiler = RemediationCompiler()
    finding = RemediationFindingRef(
        finding_id="TEST-2",
        source_domain="order_lifecycle",
        severity="high",
        detected_at=datetime.now(timezone.utc),
    )
    pack = compiler.compile_pack(
        finding, explicit_recipe_id="request_orphan_order_review"
    )

    executor = ApplyExecutor()
    result = executor.execute(pack)

    # Must NOT directly apply venue affecting requests
    assert result.mode_used == ApplyMode.REQUEST_GENERATION
    assert result.generated_request_id is not None
    assert "cannot be auto-applied" in result.error_message


def test_blast_radius_critical_on_venue_affecting():
    compiler = RemediationCompiler()
    finding = RemediationFindingRef(
        finding_id="TEST-3",
        source_domain="order_lifecycle",
        severity="high",
        detected_at=datetime.now(timezone.utc),
    )
    pack = compiler.compile_pack(
        finding, explicit_recipe_id="request_orphan_order_review"
    )
    analyzer = BlastRadiusAnalyzer()
    report = analyzer.analyze(pack)

    assert report.severity.value == "critical"
    assert "venue" in report.impacted_domains
