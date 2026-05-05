from app.migrations.rollforward import RollforwardPlanner
from app.migrations.models import MigrationPlan, MigrationScope
from datetime import datetime


def test_rollforward_planner():
    planner = RollforwardPlanner()
    plan = MigrationPlan(
        id="plan_1", created_at=datetime.now(), target_scope=MigrationScope()
    )

    result = planner.plan(plan)
    assert result.plan_id == "plan_1"
    assert result.quarantine_mode is True
