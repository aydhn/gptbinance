from app.postmortems.models import PostmortemRecord
from typing import Dict, Any


class QualityChecker:
    def check(self, postmortem: PostmortemRecord) -> Dict[str, Any]:
        return {"actionability_score": 1.0, "is_quality_sufficient": True}
