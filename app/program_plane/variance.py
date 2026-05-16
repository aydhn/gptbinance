from app.program_plane.models import ProgramVarianceRecord

class ProgramVarianceAnalyzer:
    def analyze(self, program_id: str) -> ProgramVarianceRecord:
        return ProgramVarianceRecord(
            variance_id=f"var_{program_id}",
            program_id=program_id,
            plan_vs_actual_days=2
        )
