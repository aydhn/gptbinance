import pytest
from app.migrations.scopes import ScopeResolver
from app.migrations.models import MigrationScope
from app.migrations.exceptions import MigrationFabricError


def test_scope_resolver_allows_valid_narrowing():
    resolver = ScopeResolver()
    def_scope = MigrationScope(workspaces=["ws1", "ws2"], profiles=["dev", "prod"])
    req_scope = MigrationScope(workspaces=["ws1"], profiles=["dev"])

    resolved = resolver.resolve(req_scope, def_scope)
    assert resolved.workspaces == ["ws1"]
    assert resolved.profiles == ["dev"]


def test_scope_resolver_blocks_expansion():
    resolver = ScopeResolver()
    def_scope = MigrationScope(workspaces=["ws1"])
    req_scope = MigrationScope(workspaces=["ws1", "ws2"])

    with pytest.raises(
        MigrationFabricError, match="are out of migration definition scope"
    ):
        resolver.resolve(req_scope, def_scope)
