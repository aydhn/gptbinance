from app.remediation.rollback import RollbackPlanner
from app.remediation.compiler import RemediationCompiler
from app.remediation.findings import FindingIntake


def test_rollback_planner_venue_not_eligible():
    compiler = RemediationCompiler()
    intake = FindingIntake()
    f1 = intake.normalize_finding("F-1", "order_lifecycle", "high", {})
    pack = compiler.compile_pack(f1, explicit_recipe_id="request_orphan_order_review")

    planner = RollbackPlanner()
    plan = planner.plan_rollback(pack)

    assert plan.is_eligible is False


def test_rollback_planner_local_eligible():
    compiler = RemediationCompiler()
    intake = FindingIntake()
    f1 = intake.normalize_finding("F-1", "shadow_state", "low", {})
    pack = compiler.compile_pack(f1, explicit_recipe_id="refresh_venue_shadow_snapshot")

    planner = RollbackPlanner()
    plan = planner.plan_rollback(pack)

    assert plan.is_eligible is True
    assert len(plan.steps) > 0
