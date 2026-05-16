from app.program_plane.models import ProgramTrustVerdict
from app.program_plane.enums import TrustVerdict

class TrustedProgramVerdictEngine:
    def evaluate(self, program_id: str) -> ProgramTrustVerdict:
        return ProgramTrustVerdict(
            verdict_id=f"tv_{program_id}",
            program_id=program_id,
            verdict=TrustVerdict.TRUSTED,
            breakdown={"milestone_clarity": "ok"}
        )
