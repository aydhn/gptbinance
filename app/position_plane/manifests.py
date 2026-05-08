import uuid
import hashlib
import json
from typing import List

from app.position_plane.models import (
    PositionState,
    PositionManifest,
    PositionManifestEntry,
    PositionTrustVerdict,
)


class ManifestBuilder:
    @staticmethod
    def build_manifest(
        states: List[PositionState], trust_verdict: PositionTrustVerdict = None
    ) -> PositionManifest:
        entries = []
        for state in states:
            # Simple hash logic for demonstration
            state_dict = {
                "id": state.id,
                "qty": str(state.quantity),
                "basis": str(state.average_entry_price),
            }
            state_hash = hashlib.sha256(
                json.dumps(state_dict, sort_keys=True).encode()
            ).hexdigest()

            entries.append(
                PositionManifestEntry(
                    state_id=state.id,
                    symbol=state.symbol,
                    quantity=state.quantity,
                    hash=state_hash,
                )
            )

        return PositionManifest(
            manifest_id=str(uuid.uuid4()), entries=entries, trust_verdict=trust_verdict
        )
