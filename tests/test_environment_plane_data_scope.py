import pytest
from app.environment_plane.data_scope import define_data_scope

def test_define_data_scope():
    scope = define_data_scope("Synthetic", "No live data bleed")
    assert scope.scope_description == "Synthetic"
    assert scope.bleed_warnings == "No live data bleed"
