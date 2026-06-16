from app.waterfall_plane.models import WaterfallEquivalenceReport
from app.waterfall_plane.enums import EquivalenceVerdict

def evaluate_equivalence(report_id: str, verdict: EquivalenceVerdict) -> WaterfallEquivalenceReport:
    return WaterfallEquivalenceReport(report_id=report_id, verdict=verdict)
