from typing import List, Optional
from app.migration_plane.models import MigrationDefinition, MigrationTrustVerdict
from app.migration_plane.storage import StorageManager

class MigrationRepository:
    def __init__(self, storage: StorageManager):
        self.storage = storage

    def save_migration(self, migration: MigrationDefinition) -> None:
        self.storage.save("migrations", migration.migration_id, migration)

    def get_migration(self, migration_id: str) -> Optional[MigrationDefinition]:
        return self.storage.get("migrations", migration_id)

    def save_trust_verdict(self, verdict: MigrationTrustVerdict) -> None:
        self.storage.save("trust_verdicts", verdict.migration_id, verdict)

    def get_latest_trust_verdict(self, migration_id: str) -> Optional[MigrationTrustVerdict]:
         return self.storage.get("trust_verdicts", migration_id)
