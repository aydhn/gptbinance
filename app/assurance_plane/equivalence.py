from app.assurance_plane.models import AssuranceEquivalenceReport
from app.assurance_plane.enums import EquivalenceVerdict

def evaluate_equivalence(report_id: str, src_env: str, tgt_env: str, verdict: EquivalenceVerdict, divergence_notes: str) -> AssuranceEquivalenceReport:
    return AssuranceEquivalenceReport(
        report_id=report_id,
        source_env=src_env,
        target_env=tgt_env,
        verdict=verdict,
        divergence_notes=divergence_notes
    )
