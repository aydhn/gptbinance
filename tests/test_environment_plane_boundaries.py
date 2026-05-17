import pytest
from app.environment_plane.boundaries import define_boundary
from app.environment_plane.enums import BoundaryClass

def test_define_boundary():
    boundary = define_boundary(BoundaryClass.TENANT, "Strict tenant isolation")
    assert boundary.boundary_class == BoundaryClass.TENANT
    assert boundary.ambiguity_warnings == "Strict tenant isolation"
