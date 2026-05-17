from app.environment_plane.models import EnvironmentCapabilityRecord
from typing import List

def define_capabilities(capabilities: List[str], caveats: str) -> EnvironmentCapabilityRecord:
    return EnvironmentCapabilityRecord(capabilities=capabilities, caveats=caveats)
