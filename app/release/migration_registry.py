from typing import Dict, List, Any
from app.release.enums import MigrationSeverity


class MigrationDef:
    def __init__(
        self,
        id: str,
        source: str,
        target: str,
        domain: str,
        severity: MigrationSeverity,
    ):
        self.id = id
        self.source = source
        self.target = target
        self.domain = domain
        self.severity = severity


class MigrationRegistry:
    def __init__(self):
        self._migrations: Dict[str, MigrationDef] = {}
        self._register_default_migrations()

    def _register_default_migrations(self):
        # Dummy migrations
        self.register(
            MigrationDef("mig_v1_to_v2", "v1", "v2", "config", MigrationSeverity.LOW)
        )

    def register(self, migration: MigrationDef):
        self._migrations[migration.id] = migration

    def get_path(self, source: str, target: str) -> List[MigrationDef]:
        # Simple lookup for demo
        res = []
        for mig in self._migrations.values():
            if mig.source == source and mig.target == target:
                res.append(mig)
        return res
