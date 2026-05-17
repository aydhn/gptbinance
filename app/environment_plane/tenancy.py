from app.environment_plane.models import TenancyRecord
from app.environment_plane.enums import TenancyClass

def define_tenancy(tenancy_class: TenancyClass, reuse_warnings: str) -> TenancyRecord:
    return TenancyRecord(tenancy_class=tenancy_class, reuse_warnings=reuse_warnings)
