import pytest
from app.migration_plane.storage import StorageManager
from app.migration_plane.repository import MigrationRepository
from app.migration_plane.models import MigrationDefinition, MigrationVersionPair, TransitionContract
from app.migration_plane.enums import MigrationClass, TransitionClass

def test_storage_and_repository():
    storage = StorageManager()
    repo = MigrationRepository(storage)

    migration = MigrationDefinition(
        migration_id="mig_001",
        migration_class=MigrationClass.SCHEMA_EVOLUTION,
        version_pair=MigrationVersionPair(source_version="v1", target_version="v2"),
        transition_contract=TransitionContract(transition_class=TransitionClass.FORWARD_ONLY),
        affected_artefacts=["table_users"],
        description="Test"
    )

    repo.save_migration(migration)
    retrieved = repo.get_migration("mig_001")
    assert retrieved is not None
    assert retrieved.migration_id == "mig_001"

    assert repo.get_migration("nonexistent") is None
