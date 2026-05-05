from typing import List, Dict, Any
from app.remediation.models import RemediationPack


class RemediationChangeSet:
    def __init__(self, pack: RemediationPack):
        self.pack_id = pack.pack_id
        self.recipe_name = pack.recipe.name
        self.local_metadata_updates: Dict[str, Any] = {}
        self.cache_invalidations: List[str] = []
        self.recompute_requests: List[str] = []
        self.review_requests: List[str] = []

    def add_metadata_update(self, key: str, value: Any):
        self.local_metadata_updates[key] = value

    def add_cache_invalidation(self, cache_key: str):
        self.cache_invalidations.append(cache_key)

    def add_recompute_request(self, target: str):
        self.recompute_requests.append(target)

    def add_review_request(self, context: str):
        self.review_requests.append(context)

    def summarize(self) -> Dict[str, Any]:
        return {
            "pack_id": self.pack_id,
            "recipe_name": self.recipe_name,
            "metadata_updates_count": len(self.local_metadata_updates),
            "cache_invalidations_count": len(self.cache_invalidations),
            "recompute_requests_count": len(self.recompute_requests),
            "review_requests_count": len(self.review_requests),
        }
