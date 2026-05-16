from app.program_plane.models import ProgramDebtRecord

class ProgramDebtTracker:
    def evaluate(self, program_id: str) -> ProgramDebtRecord:
        return ProgramDebtRecord(
            debt_id=f"debt_{program_id}",
            program_id=program_id,
            stale_blocker_debt=False,
            debt_severity="low"
        )
