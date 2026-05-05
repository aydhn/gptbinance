import pytest
from app.migrations.dependencies import MigrationDependencyResolver
from app.migrations.definitions import MigrationDSL
from app.migrations.enums import (
    MigrationDomain,
    MigrationType,
    ApplyClass,
    ReversibilityClass,
    MigrationSeverity,
)
from app.migrations.models import (
    MigrationScope,
    CompatibilityDeclaration,
    MigrationDependency,
)
from app.migrations.exceptions import DependencyResolutionError


def create_mock_migration(id: str, deps: list = None) -> MigrationDSL:
    return MigrationDSL.define(
        id=id,
        name=f"Mig {id}",
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
        dependencies=deps or [],
    )


def test_dependency_resolution_linear():
    resolver = MigrationDependencyResolver()
    m1 = create_mock_migration("m1")
    m2 = create_mock_migration("m2", [MigrationDependency(migration_id="m1")])
    m3 = create_mock_migration("m3", [MigrationDependency(migration_id="m2")])

    available = {m.id: m for m in [m1, m2, m3]}
    resolved = resolver.resolve([m1, m2, m3], available)

    assert [m.id for m in resolved] == ["m1", "m2", "m3"]


def test_dependency_resolution_missing():
    resolver = MigrationDependencyResolver()
    m1 = create_mock_migration("m1", [MigrationDependency(migration_id="missing_m0")])
    available = {"m1": m1}

    with pytest.raises(DependencyResolutionError, match="Missing required dependency"):
        resolver.resolve([m1], available)


def test_dependency_resolution_cyclic():
    resolver = MigrationDependencyResolver()
    m1 = create_mock_migration("m1", [MigrationDependency(migration_id="m2")])
    m2 = create_mock_migration("m2", [MigrationDependency(migration_id="m1")])
    available = {"m1": m1, "m2": m2}

    with pytest.raises(DependencyResolutionError, match="Cyclic dependency detected"):
        resolver.resolve([m1, m2], available)
