from app.capacity_plane.enums import ResourceClass
from app.capacity_plane.models import CapacityResource
from app.capacity_plane.registry import capacity_registry
from app.capacity_plane.exceptions import InvalidCapacityDefinition


def define_resource(
    resource_id: str,
    class_name: ResourceClass,
    owner: str,
    scope: str,
    total_capacity: float,
    unit: str,
    metadata: dict = None,
) -> CapacityResource:
    if (
        not resource_id
        or "unknown" in resource_id.lower()
        or "vague" in resource_id.lower()
    ):
        raise InvalidCapacityDefinition(
            "Vague or undocumented resource IDs are prohibited."
        )

    resource = CapacityResource(
        resource_id=resource_id,
        class_name=class_name,
        owner=owner,
        scope=scope,
        total_capacity=total_capacity,
        unit=unit,
        metadata=metadata or {},
    )
    capacity_registry.register_resource(resource)
    return resource


def get_all_resources() -> list[CapacityResource]:
    return capacity_registry.list_resources()
