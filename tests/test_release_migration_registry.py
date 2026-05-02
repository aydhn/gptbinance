import pytest
from app.release.migration_registry import MigrationRegistry, MigrationDef
from app.release.enums import MigrationSeverity

def test_migration_registry():
    reg = MigrationRegistry()
    reg.register(MigrationDef("test", "a", "b", "config", MigrationSeverity.LOW))
    path = reg.get_path("a", "b")
    assert len(path) == 1
    assert path[0].id == "test"
