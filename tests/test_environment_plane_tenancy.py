import pytest
from app.environment_plane.tenancy import define_tenancy
from app.environment_plane.enums import TenancyClass

def test_define_tenancy():
    tenancy = define_tenancy(TenancyClass.SHARED_TENANT, "Risk of reuse")
    assert tenancy.tenancy_class == TenancyClass.SHARED_TENANT
    assert tenancy.reuse_warnings == "Risk of reuse"
