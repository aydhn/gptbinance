
from app.renewal_plane.models import EvidenceFreshnessRecord, EvidenceFreshness

class FreshnessEvaluator:
    def check(self, renewal_id: str) -> EvidenceFreshness:
        return EvidenceFreshness.FRESH
