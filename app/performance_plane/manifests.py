import uuid
import hashlib
from typing import List
from app.performance_plane.models import (
    PerformanceManifest,
    PerformanceManifestEntry,
    PerformanceWindow,
)


class ManifestBuilder:
    @staticmethod
    def build(
        window: PerformanceWindow, entries: List[PerformanceManifestEntry]
    ) -> PerformanceManifest:
        # Generate a dummy hash
        hash_str = "".join([e.reference_id for e in entries])
        signature = hashlib.sha256(hash_str.encode()).hexdigest()

        return PerformanceManifest(
            manifest_id=str(uuid.uuid4()),
            window=window,
            entries=entries,
            hash_signature=signature,
        )
