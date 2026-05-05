from app.migrations.definitions import MigrationDSL
from app.migrations.models import MigrationScope, CompatibilityDeclaration
from app.migrations.enums import (
    MigrationDomain,
    MigrationType,
    ApplyClass,
    ReversibilityClass,
    MigrationSeverity,
)


# Common reusable recipes
def create_workspace_manifest_upgrade_recipe(
    id: str, version_from: str, version_to: str
) -> MigrationDSL:
    return MigrationDSL.define(
        id=id,
        name=f"Workspace Manifest Upgrade {version_from} to {version_to}",
        domain=MigrationDomain.WORKSPACE,
        type=MigrationType.SCHEMA_CHANGE,
        version_from=version_from,
        version_to=version_to,
        scope=MigrationScope(),
        compatibility=CompatibilityDeclaration(
            backward_compatible=False,
            forward_compatible=True,
            read_compatible=True,
            write_compatible=False,
            replay_compatible=True,
            ledger_compatible=True,
            mixed_version_safe=False,
            notes="Requires synchronized deployment.",
        ),
        reversibility=ReversibilityClass.REVERSIBLE,
        severity=MigrationSeverity.MEDIUM,
        apply_class=ApplyClass.LOCAL_METADATA,
        description="Upgrades workspace manifest to new version schema.",
    )


def create_policy_rule_schema_upgrade(
    id: str, version_from: str, version_to: str
) -> MigrationDSL:
    return MigrationDSL.define(
        id=id,
        name=f"Policy Rule Schema Upgrade {version_from} to {version_to}",
        domain=MigrationDomain.POLICY_KERNEL,
        type=MigrationType.SCHEMA_CHANGE,
        version_from=version_from,
        version_to=version_to,
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
        severity=MigrationSeverity.HIGH,
        apply_class=ApplyClass.LOCAL_METADATA,
        description="Upgrades policy rule schema safely.",
    )
