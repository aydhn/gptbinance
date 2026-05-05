from app.migrations.compatibility import CompatibilityEvaluator
from app.migrations.models import (
    CompatibilityMatrix,
    CompatibilityDeclaration,
    MigrationScope,
)
from app.migrations.enums import (
    MigrationDomain,
    CompatibilityVerdict,
    MigrationType,
    ApplyClass,
    ReversibilityClass,
    MigrationSeverity,
)
from app.migrations.definitions import MigrationDSL


def test_compatibility_evaluator_safe():
    evaluator = CompatibilityEvaluator()
    matrix = CompatibilityMatrix(mixed_version_safety=True)
    migration = MigrationDSL.define(
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

    result = evaluator.evaluate(migration, matrix)
    assert result.verdict == CompatibilityVerdict.SAFE


def test_compatibility_evaluator_caution_on_no_backward_compat():
    evaluator = CompatibilityEvaluator()
    matrix = CompatibilityMatrix(mixed_version_safety=True)
    migration = MigrationDSL.define(
        id="m1",
        name="m1",
        domain=MigrationDomain.CONFIG,
        type=MigrationType.SCHEMA_CHANGE,
        version_from="1",
        version_to="2",
        scope=MigrationScope(),
        compatibility=CompatibilityDeclaration(
            backward_compatible=False,
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

    result = evaluator.evaluate(migration, matrix)
    assert result.verdict == CompatibilityVerdict.SAFE_WITH_CAUTION


def test_compatibility_evaluator_incompatible():
    evaluator = CompatibilityEvaluator()
    matrix = CompatibilityMatrix(mixed_version_safety=True, known_conflicts=["m1"])
    migration = MigrationDSL.define(
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

    result = evaluator.evaluate(migration, matrix)
    assert result.verdict == CompatibilityVerdict.INCOMPATIBLE
