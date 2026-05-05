from app.migrations.debt import MigrationDebtGovernance
from app.migrations.models import MigrationScope, CompatibilityDeclaration
from app.migrations.enums import (
    MigrationDomain,
    MigrationType,
    ApplyClass,
    ReversibilityClass,
    MigrationSeverity,
    MigrationStatus,
)
from app.migrations.definitions import MigrationDSL


def test_migration_debt_governance():
    gov = MigrationDebtGovernance()
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
        severity=MigrationSeverity.CRITICAL,
        apply_class=ApplyClass.LOCAL_METADATA,
    )

    gov.record_debt(m1, MigrationStatus.FAILED, "Schema validation failed")

    assert len(gov.get_all_debt()) == 1
    assert gov.is_debt_critical() is True
