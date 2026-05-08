from typing import List
from datetime import datetime, timezone
import hashlib
from app.allocation.models import AllocationIntent, AllocationManifest, TrustVerdict


class ManifestBuilder:
    def build_manifest(
        self, intents: List[AllocationIntent], trust_verdict: TrustVerdict
    ) -> AllocationManifest:
        gross = sum(i.clipped_size for i in intents if i.verdict != "rejected")
        net = gross  # Simplified

        # Calculate lineage hash
        content = f"{[i.intent_id for i in intents]}_{gross}_{net}"
        lineage_hash = hashlib.sha256(content.encode()).hexdigest()[:12]

        return AllocationManifest(
            manifest_id=f"man_{int(datetime.now(timezone.utc).timestamp())}",
            timestamp=datetime.now(timezone.utc),
            intents=intents,
            portfolio_gross_exposure=gross,
            portfolio_net_exposure=net,
            constraints_refs=["global_gross_limit", "global_net_limit"],
            trust_verdict=trust_verdict,
            lineage_hash=lineage_hash,
        )
