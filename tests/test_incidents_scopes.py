import pytest
from app.incidents.scopes import ScopeResolver
from app.incidents.enums import IncidentScopeType

def test_scopes():
    scope = ScopeResolver.resolve_blast_radius(IncidentScopeType.SYMBOL, "BTCUSDT")
    assert scope.type == IncidentScopeType.SYMBOL
    assert scope.ref == "BTCUSDT"
