from app.remediation.dependencies import DependencyAnalyzer
from app.remediation.compiler import RemediationCompiler
from app.remediation.findings import FindingIntake


def test_dependency_analyzer():
    analyzer = DependencyAnalyzer()
    compiler = RemediationCompiler()
    intake = FindingIntake()

    f1 = intake.normalize_finding("F-1", "shadow_state", "low", {"symbol": "BTC"})
    p1 = compiler.compile_pack(f1, explicit_recipe_id="refresh_venue_shadow_snapshot")

    f2 = intake.normalize_finding("F-2", "shadow_state", "high", {"symbol": "BTC"})
    p2 = compiler.compile_pack(f2, explicit_recipe_id="invalidate_stale_cache")

    deps = analyzer.analyze_dependencies([p1, p2])
    assert p1.pack_id in deps[p2.pack_id]  # Recompute depends on refresh


def test_conflict_detection():
    analyzer = DependencyAnalyzer()
    compiler = RemediationCompiler()
    intake = FindingIntake()

    f1 = intake.normalize_finding("F-1", "order_lifecycle", "high", {"symbol": "BTC"})
    p1 = compiler.compile_pack(
        f1, explicit_recipe_id="request_orphan_order_review"
    )  # venue

    f2 = intake.normalize_finding("F-2", "shadow_state", "high", {"symbol": "BTC"})
    p2 = compiler.compile_pack(
        f2, explicit_recipe_id="invalidate_stale_cache"
    )  # local recompute

    conflicts = analyzer.detect_conflicts([p1, p2])
    assert len(conflicts) > 0
