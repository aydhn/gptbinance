from app.migrations.dry_run import DryRunEngine
from app.migrations.models import MigrationPlan, MigrationScope
from datetime import datetime


def test_dry_run_engine_simulate():
    engine = DryRunEngine()
    plan = MigrationPlan(
        id="plan_1", created_at=datetime.now(), target_scope=MigrationScope()
    )
    result = engine.simulate(plan)

    assert result.plan_id == "plan_1"
    assert "config.json" in result.touched_files
    assert not result.is_noop
