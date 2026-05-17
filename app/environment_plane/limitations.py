from app.environment_plane.models import EnvironmentLimitationRecord
from typing import List

def define_limitations(limitations: List[str], burden_notes: str) -> EnvironmentLimitationRecord:
    return EnvironmentLimitationRecord(limitations=limitations, burden_notes=burden_notes)
