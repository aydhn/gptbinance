from app.performance_security_plane.models import ReleaseRecord
from app.performance_security_plane.enums import ReleaseClass

class ReleaseManager:
    def create_release(self, release_id: str, security_id: str, release_type: ReleaseClass) -> ReleaseRecord:
        return ReleaseRecord(
            release_id=release_id,
            security_id=security_id,
            type=release_type,
            lineage_refs=[f"release_{release_id}"]
        )
