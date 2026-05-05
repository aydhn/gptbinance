import pytest
from app.migrations.registry import MigrationRegistry
from app.migrations.exceptions import InvalidMigrationDefinitionError
from app.migrations.definitions import MigrationDSL
from app.migrations.enums import (
    MigrationDomain,
    MigrationType,
    ApplyClass,
    ReversibilityClass,
    MigrationSeverity,
)
from app.migrations.models import MigrationScope, CompatibilityDeclaration


def test_migration_registry_registration():
    registry = MigrationRegistry()
    migration = MigrationDSL.define(
        id="test_mig_1",
        name="Test Mig 1",
        domain=MigrationDomain.CONFIG,
        type=MigrationType.SCHEMA_CHANGE,
        version_from="1.0.0",
        version_to="1.1.0",
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
    registry.register(migration)

    assert registry.get("test_mig_1") == migration
    assert len(registry.list_all()) == 1


def test_migration_registry_duplicate_registration_fails():
    registry = MigrationRegistry()
    migration = MigrationDSL.define(
        id="test_mig_1",
        name="Test Mig 1",
        domain=MigrationDomain.CONFIG,
        type=MigrationType.SCHEMA_CHANGE,
        version_from="1.0.0",
        version_to="1.1.0",
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
    registry.register(migration)

    with pytest.raises(InvalidMigrationDefinitionError):
        registry.register(migration)


def test_migration_registry_get_pending():
    registry = MigrationRegistry()
    migration = MigrationDSL.define(
        id="test_mig_1",
        name="Test Mig 1",
        domain=MigrationDomain.CONFIG,
        type=MigrationType.SCHEMA_CHANGE,
        version_from="1.0.0",
        version_to="1.1.0",
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
    registry.register(migration)

    pending = registry.get_pending({MigrationDomain.CONFIG: "1.0.0"})
    assert len(pending) == 1
    assert pending[0].id == "test_mig_1"

    pending = registry.get_pending({MigrationDomain.CONFIG: "1.1.0"})
    assert len(pending) == 0
