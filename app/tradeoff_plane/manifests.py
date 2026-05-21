from datetime import datetime
from typing import Dict, Any, List
import hashlib
import json
from .models import TradeoffObject, TradeoffArtifactManifest

class TradeoffManifestBuilder:
    def build(self, tradeoff_obj: TradeoffObject) -> TradeoffArtifactManifest:
        components = {
            "tradeoff_id": tradeoff_obj.tradeoff_id,
            "tradeoff_class": tradeoff_obj.tradeoff_class.value,
            "owner": tradeoff_obj.owner,
            "scope": tradeoff_obj.scope,
            "objectives_count": str(len(tradeoff_obj.objective_set.objectives)),
            "burdens_count": str(len(tradeoff_obj.burden_posture)),
            "sacrifices_count": str(len(tradeoff_obj.sacrifices))
        }

        # Create a simple hash representation
        content_str = json.dumps(components, sort_keys=True)
        manifest_hash = hashlib.sha256(content_str.encode()).hexdigest()

        components["manifest_hash"] = manifest_hash

        return TradeoffArtifactManifest(
            manifest_id=f"manifest-{tradeoff_obj.tradeoff_id}-{int(datetime.utcnow().timestamp())}",
            tradeoff_id=tradeoff_obj.tradeoff_id,
            components=components
        )

manifest_builder = TradeoffManifestBuilder()
