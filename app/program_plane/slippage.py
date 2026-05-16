from app.program_plane.models import SlippageRecord
from app.program_plane.enums import SlipClass

class SlippageHandler:
    def register_slip(self, program_id: str) -> SlippageRecord:
        return SlippageRecord(
            slippage_id=f"slip_{program_id}",
            program_id=program_id,
            slip_class=SlipClass.MILESTONE_SLIP
        )
