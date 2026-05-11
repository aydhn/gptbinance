from app.policy_plane.models import PolicyResource
from app.policy_plane.enums import ResourceClass


class ResourceRegistry:
    pass


def create_symbol_resource(resource_id: str) -> PolicyResource:
    return PolicyResource(resource_class=ResourceClass.SYMBOL, resource_id=resource_id)


def create_environment_resource(resource_id: str) -> PolicyResource:
    return PolicyResource(
        resource_class=ResourceClass.ENVIRONMENT, resource_id=resource_id
    )
