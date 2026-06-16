from app.waterfall_plane.models import WaterfallDivergenceReport

def report_divergence(report_id: str, sources: list) -> WaterfallDivergenceReport:
    return WaterfallDivergenceReport(report_id=report_id, divergence_sources=sources)
