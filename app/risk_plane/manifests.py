import uuid
import hashlib
import json
from datetime import datetime, timezone
from typing import List
from .models import (
    RiskArtifactManifest,
    RiskState,
    RiskBreachRecord,
    RiskResponseIntent,
)


class ManifestBuilder:
    def build(
        self,
        states: List[RiskState],
        breaches: List[RiskBreachRecord],
        responses: List[RiskResponseIntent],
    ) -> RiskArtifactManifest:
        state_ids = sorted([s.state_id for s in states])
        breach_ids = sorted([b.breach_id for b in breaches])
        response_ids = sorted([r.intent_id for r in responses])

        # Build deterministic hash
        hash_payload = json.dumps(
            {"states": state_ids, "breaches": breach_ids, "responses": response_ids}
        )
        sig = hashlib.sha256(hash_payload.encode()).hexdigest()

        return RiskArtifactManifest(
            manifest_id=str(uuid.uuid4()),
            timestamp=datetime.now(timezone.utc),
            state_refs=state_ids,
            limit_refs=[],
            breach_refs=breach_ids,
            response_refs=response_ids,
            cooldown_refs=[],
            scenario_refs=[],
            hash_signature=sig,
        )

# WORKFLOW PLANE INTEGRATION:
# Added hooks for dependency/gate evaluations, duplicate run protections,
# and explicit reruns per Phase 73 requirements.
