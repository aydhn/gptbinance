from typing import Dict, List, Optional
from app.migrations.models import MigrationDefinition
from app.migrations.enums import MigrationDomain
from app.migrations.exceptions import InvalidMigrationDefinitionError


class MigrationRegistry:
    def __init__(self):
        self._migrations: Dict[str, MigrationDefinition] = {}

    def register(self, migration: MigrationDefinition) -> None:
        if migration.id in self._migrations:
            raise InvalidMigrationDefinitionError(
                f"Migration {migration.id} already registered."
            )
        self._migrations[migration.id] = migration

    def get(self, migration_id: str) -> Optional[MigrationDefinition]:
        return self._migrations.get(migration_id)

    def list_all(self) -> List[MigrationDefinition]:
        return list(self._migrations.values())

    def get_by_domain(self, domain: MigrationDomain) -> List[MigrationDefinition]:
        return [m for m in self._migrations.values() if m.domain == domain]

    def get_pending(
        self, current_versions: Dict[MigrationDomain, str]
    ) -> List[MigrationDefinition]:
        pending = []
        for migration in self._migrations.values():
            current_ver = current_versions.get(migration.domain, "0.0.0")
            # simplified version comparison logic
            if current_ver == migration.version_from:
                pending.append(migration)
        return pending


migration_registry = MigrationRegistry()
