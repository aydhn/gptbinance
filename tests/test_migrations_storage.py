from app.migrations.storage import MigrationStorageEngine
from app.migrations.models import MigrationScope
from app.migrations.enums import (
    MigrationDomain,
    MigrationType,
    ApplyClass,
    ReversibilityClass,
    MigrationSeverity,
)
from app.migrations.definitions import MigrationDSL
from app.migrations.models import CompatibilityDeclaration


def test_storage_engine():
    engine = MigrationStorageEngine()
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

    engine.save("definitions", m1.id, m1)

    loaded = engine.load("definitions", m1.id)
    assert loaded is not None
    assert loaded["id"] == "m1"
