from app.performance_security_plane.models import DrawRightRecord
from app.performance_security_plane.enums import DrawClass

class DrawManager:
    def create_draw_right(self, draw_id: str, security_id: str, draw_type: DrawClass) -> DrawRightRecord:
        return DrawRightRecord(
            draw_id=draw_id,
            security_id=security_id,
            type=draw_type,
            lineage_refs=[f"draw_{draw_id}"]
        )
