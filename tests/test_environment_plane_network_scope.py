import pytest
from app.environment_plane.network_scope import define_network_scope

def test_define_network_scope():
    scope = define_network_scope("Internal-only", "Air-gapped")
    assert scope.scope_description == "Internal-only"
    assert scope.mismatch_cautions == "Air-gapped"
