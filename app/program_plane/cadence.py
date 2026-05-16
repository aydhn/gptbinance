from app.program_plane.models import CadenceRecord
from app.program_plane.enums import CadenceClass

class CadenceManager:
    def track(self, program_id: str) -> CadenceRecord:
        return CadenceRecord(
            cadence_id=f"cad_{program_id}",
            program_id=program_id,
            cadence_class=CadenceClass.WEEKLY_DELIVERY,
            misses=0
        )
