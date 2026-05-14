from typing import Dict, List, Set, Any
from app.continuity_plane.models import ContinuityService

class ContinuityDependencyAnalyzer:
    def __init__(self):
        pass

    def analyze_dependencies(self, service: ContinuityService, all_services: List[ContinuityService]) -> Dict[str, Any]:
        deps = set(service.dependencies)
        missing = [d for d in deps if d not in [s.service_id for s in all_services]]
        return {
            "dependencies": list(deps),
            "missing": missing,
            "has_missing": len(missing) > 0
        }
