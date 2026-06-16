from app.waterfall_plane.models import WaterfallComparisonRecord

def register_comparison(comparison_id: str, details: str) -> WaterfallComparisonRecord:
    return WaterfallComparisonRecord(comparison_id=comparison_id, details=details)
