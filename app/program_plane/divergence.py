from app.program_plane.models import ProgramDivergenceReport

class ProgramDivergenceAnalyzer:
    def analyze(self, program_id: str) -> ProgramDivergenceReport:
        return ProgramDivergenceReport(
            divergence_id=f"div_{program_id}",
            program_id=program_id,
            divergence_severity="low",
            blast_radius="none"
        )
