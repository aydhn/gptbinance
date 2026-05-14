from app.capacity_plane.enums import QuotaClass
from app.capacity_plane.models import CapacityQuota
from app.capacity_plane.registry import capacity_registry
from app.capacity_plane.exceptions import InvalidQuotaDefinition


def define_quota(
    quota_id: str,
    resource_id: str,
    class_name: QuotaClass,
    limit_value: float,
    reset_semantics: str,
    metadata: dict = None,
) -> CapacityQuota:
    if not quota_id:
        raise InvalidQuotaDefinition("Quota ID is required.")

    if not reset_semantics:
        raise InvalidQuotaDefinition(
            "Ambiguous quota semantics: reset_semantics is required."
        )

    quota = CapacityQuota(
        quota_id=quota_id,
        resource_id=resource_id,
        class_name=class_name,
        limit_value=limit_value,
        reset_semantics=reset_semantics,
        metadata=metadata or {},
    )
    capacity_registry.register_quota(quota)
    return quota


def get_all_quotas() -> list[CapacityQuota]:
    return capacity_registry.list_quotas()
