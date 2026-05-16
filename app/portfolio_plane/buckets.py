from typing import Dict, Optional
from app.portfolio_plane.models import InvestmentBucket
from app.portfolio_plane.exceptions import PortfolioStorageError

class BucketManager:
    def __init__(self):
        self._buckets: Dict[str, InvestmentBucket] = {}

    def register(self, bucket: InvestmentBucket):
        if bucket.bucket_id in self._buckets:
            raise PortfolioStorageError(f"Bucket {bucket.bucket_id} already exists")
        self._buckets[bucket.bucket_id] = bucket

    def get(self, bucket_id: str) -> Optional[InvestmentBucket]:
        return self._buckets.get(bucket_id)

    def get_all(self) -> Dict[str, InvestmentBucket]:
        return self._buckets.copy()
