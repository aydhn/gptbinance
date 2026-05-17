from app.environment_plane.models import EnvironmentBoundaryRecord
from app.environment_plane.enums import BoundaryClass

def define_boundary(boundary_class: BoundaryClass, ambiguity_warnings: str) -> EnvironmentBoundaryRecord:
    return EnvironmentBoundaryRecord(boundary_class=boundary_class, ambiguity_warnings=ambiguity_warnings)
