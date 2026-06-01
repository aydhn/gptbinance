from app.assurance_plane.models import AssuranceRecord
from app.assurance_plane.quality import check_quality

def evaluate_readiness(record: AssuranceRecord) -> dict:
    warnings = check_quality(record)
    return {
        "is_ready": len(warnings) == 0,
        "readiness_class": "clean" if not warnings else "degraded",
        "notes": warnings
    }
