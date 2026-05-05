from app.migrations.models import MigrationScope
from app.migrations.exceptions import MigrationFabricError


class ScopeResolver:
    def resolve(
        self, requested_scope: MigrationScope, definition_scope: MigrationScope
    ) -> MigrationScope:
        # Prevent expanding scope beyond definition
        invalid_workspaces = set(requested_scope.workspaces) - set(
            definition_scope.workspaces
        )
        if invalid_workspaces and definition_scope.workspaces:
            raise MigrationFabricError(
                f"Requested workspaces {invalid_workspaces} are out of migration definition scope."
            )

        invalid_profiles = set(requested_scope.profiles) - set(
            definition_scope.profiles
        )
        if invalid_profiles and definition_scope.profiles:
            raise MigrationFabricError(
                f"Requested profiles {invalid_profiles} are out of migration definition scope."
            )

        return requested_scope
