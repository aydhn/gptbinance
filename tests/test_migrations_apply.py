import pytest
from app.migrations.apply import ApplyEngine
from app.migrations.models import MigrationPlan, MigrationScope, MigrationPlanStep
from app.migrations.enums import MigrationStatus
from app.migrations.exceptions import ApplyPolicyViolation
from datetime import datetime


def test_apply_engine_success():
    engine = ApplyEngine()
    plan = MigrationPlan(
        id="plan_1",
        created_at=datetime.now(),
        target_scope=MigrationScope(),
        steps=[MigrationPlanStep(migration_id="m1", order=1)],
    )

    result = engine.execute(plan, preflight_passed=True, dry_run_passed=True)
    assert result.status == MigrationStatus.APPLIED_CLEAN
    assert "m1" in result.applied_migrations


def test_apply_engine_blocked_by_policy():
    engine = ApplyEngine()
    plan = MigrationPlan(
        id="plan_1", created_at=datetime.now(), target_scope=MigrationScope()
    )

    with pytest.raises(ApplyPolicyViolation):
        engine.execute(plan, preflight_passed=False, dry_run_passed=True)
