from app.migrations.preflight import PreflightEngine
from app.migrations.models import MigrationPlan, MigrationScope
from app.migrations.enums import PreflightVerdict
from datetime import datetime


def test_preflight_engine_pass():
    engine = PreflightEngine()
    plan = MigrationPlan(
        id="plan_1", created_at=datetime.now(), target_scope=MigrationScope()
    )
    report = engine.run_preflight(plan)
    assert report.verdict == PreflightVerdict.PASS
