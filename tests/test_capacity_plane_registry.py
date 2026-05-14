import pytest
from app.capacity_plane.registry import CanonicalCapacityRegistry
from app.capacity_plane.models import CapacityResource, CapacityQuota
from app.capacity_plane.enums import ResourceClass, QuotaClass
from app.capacity_plane.exceptions import (
    InvalidCapacityDefinition,
    InvalidQuotaDefinition,
)


def test_capacity_registry_resource():
    registry = CanonicalCapacityRegistry()
    res = CapacityResource(
        resource_id="cpu_live",
        class_name=ResourceClass.COMPUTE,
        owner="trading",
        scope="live",
        total_capacity=100.0,
        unit="cores",
    )
    registry.register_resource(res)

    assert registry.get_resource("cpu_live") is not None
    assert len(registry.list_resources()) == 1

    with pytest.raises(InvalidCapacityDefinition):
        registry.register_resource(res)  # Duplicate

    with pytest.raises(InvalidCapacityDefinition):
        invalid_res = CapacityResource(
            resource_id="",
            class_name=ResourceClass.COMPUTE,
            owner="test",
            scope="test",
            total_capacity=10,
            unit="cores",
        )
        registry.register_resource(invalid_res)


def test_capacity_registry_quota():
    registry = CanonicalCapacityRegistry()
    quota = CapacityQuota(
        quota_id="vendor_api_limit",
        resource_id="vendor_api",
        class_name=QuotaClass.VENDOR_DEFINED,
        limit_value=1000.0,
        reset_semantics="1m",
    )
    registry.register_quota(quota)
    assert registry.get_quota("vendor_api_limit") is not None
    assert len(registry.list_quotas()) == 1
