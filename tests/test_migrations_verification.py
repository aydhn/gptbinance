from app.migrations.verification import VerificationEngine
from app.migrations.models import MigrationPlan, MigrationScope
from app.migrations.enums import MigrationVerdict
from datetime import datetime


def test_verification_engine():
    engine = VerificationEngine()
    plan = MigrationPlan(
        id="plan_1", created_at=datetime.now(), target_scope=MigrationScope()
    )

    result = engine.verify(plan)
    assert result.verdict == MigrationVerdict.SUCCESS
    assert result.target_versions_reached is True
