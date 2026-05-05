from app.remediation.apply import ApplyExecutor
from app.remediation.compiler import RemediationCompiler
from app.remediation.findings import FindingIntake
from app.remediation.enums import ApplyMode


def test_apply_executor_safe():
    compiler = RemediationCompiler()
    intake = FindingIntake()
    f1 = intake.normalize_finding("F-1", "shadow_state", "low", {})
    pack = compiler.compile_pack(f1, explicit_recipe_id="refresh_venue_shadow_snapshot")

    executor = ApplyExecutor()
    res = executor.execute(pack)
    assert res.success is True
    assert res.mode_used == ApplyMode.DIRECT_SAFE


def test_apply_executor_venue_affecting_generates_request():
    compiler = RemediationCompiler()
    intake = FindingIntake()
    f1 = intake.normalize_finding("F-1", "order_lifecycle", "high", {})
    pack = compiler.compile_pack(f1, explicit_recipe_id="request_orphan_order_review")

    executor = ApplyExecutor()
    res = executor.execute(pack)
    assert res.success is True
    assert res.mode_used == ApplyMode.REQUEST_GENERATION
    assert res.generated_request_id is not None
