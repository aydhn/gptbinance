from app.migrations.rollback import RollbackPlanner
from app.migrations.models import (
    MigrationPlan,
    MigrationScope,
    CompatibilityDeclaration,
)
from app.migrations.enums import (
    MigrationDomain,
    MigrationType,
    ApplyClass,
    ReversibilityClass,
    MigrationSeverity,
    RollbackStrategy,
)
from app.migrations.definitions import MigrationDSL
from datetime import datetime


def test_rollback_planner_eligible():
    planner = RollbackPlanner()
    plan = MigrationPlan(
        id="plan_1", created_at=datetime.now(), target_scope=MigrationScope()
    )
    m1 = MigrationDSL.define(
        id="m1",
        name="m1",
        domain=MigrationDomain.CONFIG,
        type=MigrationType.SCHEMA_CHANGE,
        version_from="1",
        version_to="2",
        scope=MigrationScope(),
        compatibility=CompatibilityDeclaration(
            backward_compatible=True,
            forward_compatible=True,
            read_compatible=True,
            write_compatible=True,
            replay_compatible=True,
            ledger_compatible=True,
            mixed_version_safe=True,
        ),
        reversibility=ReversibilityClass.REVERSIBLE,
        severity=MigrationSeverity.LOW,
        apply_class=ApplyClass.LOCAL_METADATA,
    )

    result = planner.plan(plan, [m1])
    assert result.eligible is True
    assert result.strategy == RollbackStrategy.MANUAL_SCRIPT


def test_rollback_planner_not_eligible():
    planner = RollbackPlanner()
    plan = MigrationPlan(
        id="plan_1", created_at=datetime.now(), target_scope=MigrationScope()
    )
    m1 = MigrationDSL.define(
        id="m1",
        name="m1",
        domain=MigrationDomain.CONFIG,
        type=MigrationType.SCHEMA_CHANGE,
        version_from="1",
        version_to="2",
        scope=MigrationScope(),
        compatibility=CompatibilityDeclaration(
            backward_compatible=True,
            forward_compatible=True,
            read_compatible=True,
            write_compatible=True,
            replay_compatible=True,
            ledger_compatible=True,
            mixed_version_safe=True,
        ),
        reversibility=ReversibilityClass.NON_REVERSIBLE,
        severity=MigrationSeverity.LOW,
        apply_class=ApplyClass.LOCAL_METADATA,
    )

    result = planner.plan(plan, [m1])
    assert result.eligible is False
    assert result.strategy == RollbackStrategy.NOT_SUPPORTED
