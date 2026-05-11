import pytest
from app.migration_plane.models import MigrationDefinition, MigrationVersionPair, TransitionContract
from app.migration_plane.enums import MigrationClass, TransitionClass
from app.migration_plane.registry import CanonicalMigrationRegistry
from app.migration_plane.exceptions import InvalidMigrationDefinitionError

def test_registry_registration():
    registry = CanonicalMigrationRegistry()
    migration = MigrationDefinition(
        migration_id="mig_001",
        migration_class=MigrationClass.SCHEMA_EVOLUTION,
        version_pair=MigrationVersionPair(source_version="v1", target_version="v2"),
        transition_contract=TransitionContract(transition_class=TransitionClass.FORWARD_ONLY),
        affected_artefacts=["table_users"],
        description="Test migration"
    )

    registry.register(migration)
    assert registry.get("mig_001") == migration

    with pytest.raises(InvalidMigrationDefinitionError):
        registry.register(migration)

def test_registry_get_not_found():
    registry = CanonicalMigrationRegistry()
    with pytest.raises(InvalidMigrationDefinitionError):
        registry.get("nonexistent")
