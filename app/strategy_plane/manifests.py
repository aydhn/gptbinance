import hashlib
import json
from app.strategy_plane.models import (
    StrategyManifest,
    StrategyDefinition,
    StrategyThesis,
    TrustVerdict,
)
from app.strategy_plane.enums import LifecycleState


class StrategyManifestBuilder:
    def build(
        self,
        definition: StrategyDefinition,
        thesis: StrategyThesis,
        lifecycle_state: LifecycleState,
        trust_verdict: TrustVerdict,
    ) -> StrategyManifest:
        # Calculate a simple hash over the definition and thesis
        content = {
            "strategy_id": definition.strategy_id,
            "hypothesis_ref": definition.hypothesis_ref,
            "thesis_ref": thesis.thesis_id,
            "thesis_version": thesis.version,
            "dependencies": definition.dependencies.model_dump(),
            "signal_contracts": [s.model_dump() for s in definition.signal_contracts],
        }

        manifest_hash = hashlib.sha256(
            json.dumps(content, sort_keys=True).encode()
        ).hexdigest()

        return StrategyManifest(
            strategy_id=definition.strategy_id,
            definition=definition,
            thesis=thesis,
            lifecycle_state=lifecycle_state,
            trust_verdict=trust_verdict,
            manifest_hash=manifest_hash,
        )
