from app.commitment_plane.models import DeadlineRecord
from datetime import datetime

class DeadlineManager:
    @staticmethod
    def create_deadline(deadline_type: str, timestamp: datetime, breach_notes: str = None) -> DeadlineRecord:
        valid_types = ['hard', 'soft', 'customer', 'regulatory']
        if deadline_type not in valid_types:
            raise ValueError(f"Invalid deadline type. Must be one of {valid_types}")

        return DeadlineRecord(
            deadline_type=deadline_type,
            timestamp=timestamp,
            breach_notes=breach_notes,
            lineage_refs=[]
        )
