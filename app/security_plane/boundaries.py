from app.security_plane.registry import CanonicalSecurityRegistry
from app.security_plane.models import TrustBoundary
from app.security_plane.enums import BoundaryClass

class BoundaryManager:
    def __init__(self, registry: CanonicalSecurityRegistry):
        self.registry = registry

    def define_boundary(self, boundary_id: str, boundary_class: BoundaryClass, desc: str) -> TrustBoundary:
        boundary = TrustBoundary(
            boundary_id=boundary_id,
            boundary_class=boundary_class,
            description=desc
        )
        self.registry.register_boundary(boundary)
        return boundary
