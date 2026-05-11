from typing import Dict, List
from app.migration_plane.models import MigrationDefinition
from app.migration_plane.base import MigrationRegistryBase
from app.migration_plane.exceptions import InvalidMigrationDefinitionError

class CanonicalMigrationRegistry(MigrationRegistryBase):
    def __init__(self):
        self._migrations: Dict[str, MigrationDefinition] = {}

    def register(self, migration: MigrationDefinition) -> None:
        if migration.migration_id in self._migrations:
            raise InvalidMigrationDefinitionError(f"Migration {migration.migration_id} already registered")
        self._migrations[migration.migration_id] = migration

    def get(self, migration_id: str) -> MigrationDefinition:
        if migration_id not in self._migrations:
            raise InvalidMigrationDefinitionError(f"Migration {migration_id} not found")
        return self._migrations[migration_id]

    def list_all(self) -> List[MigrationDefinition]:
        return list(self._migrations.values())
