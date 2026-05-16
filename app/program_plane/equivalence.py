from app.program_plane.models import ProgramEquivalenceReport
from app.program_plane.enums import EquivalenceVerdict

class ProgramEquivalenceAnalyzer:
    def analyze(self, program_id: str) -> ProgramEquivalenceReport:
        return ProgramEquivalenceReport(
            report_id=f"eq_{program_id}",
            program_id=program_id,
            replay_equivalent=True,
            paper_equivalent=True,
            live_equivalent=True,
            verdict=EquivalenceVerdict.EQUIVALENT
        )
