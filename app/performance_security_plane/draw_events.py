from app.performance_security_plane.models import DrawEventRecord

class DrawEventManager:
    def create_draw_event(self, event_id: str, security_id: str, event_type: str, amount: float) -> DrawEventRecord:
        return DrawEventRecord(
            event_id=event_id,
            security_id=security_id,
            type=event_type,
            amount=amount,
            lineage_refs=[f"draw_event_{event_id}"]
        )
