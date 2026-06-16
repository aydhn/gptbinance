from app.waterfall_plane.models import SeniorityRecord

def register_seniority(seniority_id: str, description: str) -> SeniorityRecord:
    return SeniorityRecord(seniority_id=seniority_id, description=description)
